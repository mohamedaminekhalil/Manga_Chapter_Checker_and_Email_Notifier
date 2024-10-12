# Manga Chapter Checker and Email Notifier

A Python automation script that checks for new manga chapters, scrapes data of the latest chapter, sends an email notification, and keeps logs of the email sent. 
The script compares the last saved chapter in a text file to the newly found chapter, and if there's an update, it sends an email and updates the log.

## Features
- Checks for new manga chapters.
- Scrapes relevant data when a new chapter is released.
- Sends email notifications for new chapters.
- Updates a text file with the latest chapter number.
- Logs all sent emails (with title and time) in a CSV file.

## Requirements
- Python 3.x
- BeautifulSoup (for web scraping)
- Requests (for HTTP requests)
- smtplib and email (for sending emails)
- CSV (for logging emails)

## Installation
1. Clone the repository.
2. Install the required packages:
```bash
pip install -r requirements.txt
Update the following files:
config.py: Set the website URL to scrape and email configuration.
last_chapter.txt: Initially set with the latest chapter number.
```
## How It Works
- The script checks the current latest chapter against the number saved in `chap.txt`.
- If a new chapter is found, it scrapes the relevant data and sends an email.
- It then updates `last_chapter.txt` with the new chapter number.
- Each time an email is sent, the details (title and timestamp) are logged in a CSV file `logs.csv`.

## Email Configuration
The script uses the `smtplib` library to send emails. Update the email configuration:
- SMTP server
- Port
- Sender's email address and password
Usage Example

## Usage Example
Run the script:
```bash
python main.py
The script will check for updates and send an email if a new chapter is found.
Email log entries will be added to the CSV file for future reference.
```
## Security Note
- Be cautious when storing email credentials in plain text. Use environment variables or secure storage solutions to protect sensitive data.
Acknowledgments

## Acknowledgments
- Data sourced from [Manga website](https://tcbscans.me).
