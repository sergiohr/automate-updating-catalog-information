#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
import emails

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def check_diskUsage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_memoryUsage():
    """Verifies that there's enough free memory"""
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500


def check_cpuUsage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80


def send_email(subject):
    user = os.getenv('USER')
    sender = "automation@example.com"
    recipient = "{}@example.com".format(user)
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email('localhost', message)
    
if __name__ == "__main__":
    if not check_cpuUsage():
        subject = "Error - CPU usage is over 80%"
        send_email(subject)

    if not check_memoryUsage():
        subject = "Error - Available memory is less than 500MB"
        send_email(subject)

    if not check_diskUsage('/'):
        subject = "Error - Available disk space is less than 20%"
        send_email(subject)

    if not check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        send_email(subject)
