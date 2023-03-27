# TelegramMessageExtractor
TelegramMessageExtractor is a Python script that simplifies the process of extracting messages from HTML-formatted Telegram export data. With this tool, you can easily filter out and save message text data in a convenient CSV or TXT format.

## Features
- Extracts message text from HTML-formatted Telegram export files
- Processes all HTML files in a specified subdirectory
- Saves the extracted messages in a CSV or TXT file
- Provides a progress bar to visualize the extraction process

## Prerequisites
- Python 3.x
- BeautifulSoup
- tqdm

## Installation
Clone the repository or download the source code: 
```bash
git clone https://github.com/Sakkov/telegram-data.git
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the script from the command line by specifying the subdirectory containing the HTML files and an optional output format (either 'csv' or 'txt'):

```bash
python process_html.py <subdirectory> [output_format]
```

The extracted messages will be saved in a file named filtered_messages.csv or filtered_messages.txt in the script's directory, depending on the specified output format. If no output format is provided, the script defaults to saving in CSV format.

## Example
If your HTML files are stored in a subdirectory called telegram_export and you want to save the extracted messages in a TXT file, run the script as follows:

```bash
python process_html.py telegram_export txt
```

After processing, the extracted messages will be saved in filtered_messages.txt.

## License
This project is licensed under the MIT License
