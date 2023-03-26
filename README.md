# CleverMessageExtractor
CleverMessageExtractor is a Python script that simplifies the process of extracting messages from HTML-formatted Telegram export data. With this tool, you can easily filter out and save message text data in a convenient CSV format.

## Features
Extracts message text from HTML-formatted Telegram export files
Processes all HTML files in a specified subdirectory
Saves the extracted messages in a CSV file
Provides a progress bar to visualize the extraction process
- Prerequisites
- Python 3.x
- BeautifulSoup
- tqdm

## Installation
Clone the repository or download the source code: 
```bash
git clone https://github.com/username/CleverMessageExtractor.git
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the script from the command line by specifying the subdirectory containing the HTML files:

```bash
python process_html.py <subdirectory>
```

The extracted messages will be saved in a CSV file named filtered_messages.csv in the script's directory.

## Example
If your HTML files are stored in a subdirectory called telegram_export, run the script as follows:

```bash
python process_html.py telegram_export
```

After processing, the extracted messages will be saved in filtered_messages.csv.

## License
This project is licensed under the MIT License