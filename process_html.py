import re
import csv
import os
import sys
from bs4 import BeautifulSoup
from tqdm import tqdm

# Function to extract message texts from HTML content
def extract_message_texts(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    messages = soup.find_all('div', class_='text')
    texts = [message.get_text(strip=True) for message in messages]
    return texts

# Function to process all HTML files in a subdirectory
def process_html_files(subdirectory):
    message_texts = []

    html_files = [f for f in os.listdir(subdirectory) if f.endswith('.html')]
    for filename in tqdm(html_files, desc="Processing HTML files"):
        filepath = os.path.join(subdirectory, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()

        message_texts.extend(extract_message_texts(html_content))

    return message_texts

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python process_html.py <subdirectory> [output_format]")
        sys.exit(1)

    subdirectory = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else 'csv'

    message_texts = process_html_files(subdirectory)

    if output_format.lower() == 'csv':
        # Write message texts to a CSV file
        csv_filename = 'filtered_messages.csv'
        with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Message'])
            for message in message_texts:
                csv_writer.writerow([message])
        print(f"Filtered messages have been saved to {csv_filename}")

    elif output_format.lower() == 'txt':
        # Write message texts to a TXT file
        txt_filename = 'filtered_messages.txt'
        with open(txt_filename, 'w', encoding='utf-8') as txtfile:
            for message in message_texts:
                txtfile.write(f'{message}\n')
        print(f"Filtered messages have been saved to {txt_filename}")

    else:
        print("Invalid output_format. Please specify 'csv' or 'txt'.")
