#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    title = Paragraph(title, styles['h1'])
    paragraph = Paragraph(paragraph.replace('\n','<br/>'), styles['BodyText'])
    report = SimpleDocTemplate(attachment)
    
    report.build([title, paragraph])
