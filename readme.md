# Usana Data Automation

This project is used to automate checking incremental data filled in by Jotform, append it in the shared data file that is shared with externals, check if new so_numbers are filled in and aggregate those numbers so that emails can be sent

Your python path is /usr/local/bin/python3

## Steps

0. Open the terminal. cd to the usana-data-automation folder. To run files, use python3 <your-file-name>

1. Download the jotform raw data from the url here https://www.jotform.com/csv/242513533264047 and replace the csv with the raw_data.csv file. You must be logged in jotform to do so.

2. Download the shared_data from the usana onedrive in this url here. https://usanaverse-my.sharepoint.com/:x:/g/personal/celeste_yee_usanainc_com/EXEu-P44EoNKpPGNX5JDBiEBzebuBndx1giJkdysNX49sw?e=5Gj2ky. From menu -> export as csv. Replace the csv with the shared_data.csv

3. run process_raw_data.py

4. new data should be included in the shared_data.csv now. Append new data to the onedrive file to be filled by externals.

5. run process_shared_data.py

6. data that has no so_numbers previously but do now should be included in the send_email.csv file.
