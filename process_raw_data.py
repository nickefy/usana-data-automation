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

# Read in the current raw_data
raw_data = pd.read_csv(RAW_DATA_PATH)
raw_data.columns = ['submission_id', 'submission_date', 'distributor_id','full_name','email_address', 'mobile_number','choose_your_preferred_session','payment_method','terms_and_conditions']

# If last_raw_data.csv doesn't exist, create it (for the first run)
if not os.path.exists(LAST_RAW_DATA_PATH):
    last_raw_data = pd.DataFrame(columns=raw_data.columns)
    last_raw_data.to_csv(LAST_RAW_DATA_PATH, index=False)
else:
    last_raw_data = pd.read_csv(LAST_RAW_DATA_PATH)
    
last_raw_data.columns = ['submission_id', 'submission_date', 'distributor_id','full_name','email_address', 'mobile_number','choose_your_preferred_session','payment_method','terms_and_conditions']

# Detect new entries in the current raw_data that were not in the last run
new_entries = raw_data[~raw_data['submission_id'].isin(last_raw_data['submission_id'])]

if not new_entries.empty:
    print("There are new submissions found compared to the last run. The new submissions are ")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(new_entries)
    # Load shared_data and append new entries with a null sales_order
    # shutil.copyfile(SHARED_DATA_PATH, LAST_SHARED_DATA_PATH)

    print(f"The last_shared_data file has been replaced with the contents of shared_data.")
    shared_data = pd.read_csv(SHARED_DATA_PATH)
    shared_data.columns = ['submission_date', 'distributor_id','full_name','email_address', 'mobile_number','choose_your_preferred_session','payment_method','terms_and_conditions','so_number','dummy_field','remarks','confirmation_email','ticket_collected','dummy_field_2']
    common_columns = raw_data.columns.intersection(shared_data.columns)
    df_combined = pd.concat([shared_data, new_entries[common_columns]], ignore_index=True)
#     shared_data = pd.concat([shared_data, new_entries], ignore_index=True)
    df_combined
    
#     # Save the updated shared_data.csv
    df_combined.to_csv(SHARED_DATA_PATH, index=False)
    shutil.copyfile(RAW_DATA_PATH, LAST_RAW_DATA_PATH)
    print(f"The last_raw_data file has been replaced with the contents of raw_data.")

if new_entries.empty:
    print("There are no new submissions since the last run")
    
    
    
    
#     # Send email notification to customer service
#     msg = MIMEText("New ticket orders detected. Please process payment.")
#     msg['Subject'] = 'New Ticket Orders'
#     msg['From'] = 'your_email@example.com'
#     msg['To'] = 'customer_service@gmail.com'
    
#     # Replace with your email configuration
#     s = smtplib.SMTP('smtp.example.com')
#     s.send_message(msg)
#     s.quit()

#     # Log the update
#     with open(LOG_PATH, 'a') as log_file:
#         log_file.write("New data appended to shared_data.csv and customer service notified.\n")

#     # Update last_raw_data.csv to store the current raw_data for the next run
#     raw_data.to_csv(LAST_RAW_DATA_PATH, index=False)

