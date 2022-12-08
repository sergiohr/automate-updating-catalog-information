#!/bin/bash

# download images and description
sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
tar xf ~/supplier-data.tar.gz
rm ~/supplier-data/images/LICENSE
rm ~/supplier-data/images/README

sudo chmod +x ~/changeImage.py
./changeImage.py

sudo chmod +x ~/example_upload.py
./example_upload.py

sudo chmod +x ~/supplier_image_upload.py
./supplier_image_upload.py

sudo chmod +x ~/run.py
./run.py

sudo chmod +x ~/report_email.py
./report_email.py

sudo chmod +x ~/health_check.py
./health_check.py

