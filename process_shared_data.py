import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
import shutil

# File paths
RAW_DATA_PATH = 'data/raw_data.csv'
LAST_RAW_DATA_PATH = 'data/last_raw_data.csv'  # Stores previous run's raw data
SHARED_DATA_PATH = 'data/shared_data.csv'
LAST_SHARED_DATA_PATH = 'data/last_shared_data.csv'
LOG_PATH = '../logs/process_log.txt'

shared_data = pd.read_csv(SHARED_DATA_PATH)
last_shared_data = pd.read_csv(LAST_SHARED_DATA_PATH)
last_shared_data['so_number'] = last_shared_data['so_number'].str.strip()
shared_data['so_number'] = shared_data['so_number'].str.strip()
new_so_numbers = shared_data[~shared_data['so_number'].isin(last_shared_data['so_number'])]
# Group by Full Name, Email Address, Mobile Number, and Choose Your Preferred Session and count the rows for each group
grouped_data = new_so_numbers.groupby(
    ['full_name', 'email_address', 'mobile_number', 'choose_your_preferred_session','so_number']
).size().reset_index(name='Total Rows')

grouped_data.to_csv('send_email.csv')

shutil.copyfile(SHARED_DATA_PATH, LAST_SHARED_DATA_PATH)

# Display the grouped and summed data
print(grouped_data)