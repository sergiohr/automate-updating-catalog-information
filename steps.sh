#!/bin/bash

# download images and description
sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
tar xf ~/supplier-data.tar.gz
rm ~/supplier-data/images/LICENSE
rm ~/supplier-data/images/README

sudo chmod +x ~/changeImage.py
./changeImage.py


