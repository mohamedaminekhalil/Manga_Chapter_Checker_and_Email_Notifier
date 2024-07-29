import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
import smtplib
import ssl
import re

sender = "mamoyeyy@gmail.com"
pwd = "qkrdcvfatyjmyqlq"
recipients = ["mxmxboy0@gmail.com", "twixoontheman@gmail.com"]
OP_URL = "https://tcb-backup.bihar-mirchi.com/mangas/5/one-piece"
JJK_URL = "https://tcb-backup.bihar-mirchi.com/mangas/4/jujutsu-kaisen"


def retrieve_last_chap(URL, manga):
    web_page = requests.get(URL)
    soup = BeautifulSoup(web_page.text, "html.parser")

    a_tag = soup.find('a', class_='block border border-border bg-card mb-3 p-3 rounded')

    link = a_tag['href']

    chapter_text = a_tag.find('div', class_='text-lg font-bold').text
    chapter_text = re.sub(r'\s{2,}', ' ', chapter_text)
    try:
        chapter = int(chapter_text.strip().split()[-1])
    except ValueError:
        chapter = float(chapter_text.strip().split()[-1])
    title = a_tag.find('div', class_='text-gray-500').text
    data = {
        "manga": manga,
        "chapter": chapter,
        "title": title,
        "link": f"https://tcbscans.me{link}"
    }
    return data


def send_email(data):
    sub = f"NEW {data["manga"]} CHAPTER: {data["title"]}"
    msg = f"Chapter {data["chapter"]} is out go check it out!!!\n{data["link"]}"
    body = msg

    # Set up the mail
    new_email = EmailMessage()
    new_email["From"] = sender
    new_email["To"] = ", ".join(recipients)
    new_email["Subject"] = sub
    new_email.set_content(body)
    # For security
    context = ssl.create_default_context()
    # Login and sending the mail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, pwd)
        smtp.sendmail(sender, recipients, new_email.as_string())


if __name__ == "__main__":
    with open(file="chap.txt", mode="r") as f:
        latest_op_chap = f.readline().split(":")[1]
        latest_jjk_chap = f.readline().split(":")[1]
        try:
            latest_op_chap = int(latest_op_chap)
        except ValueError:
            latest_op_chap = float(latest_op_chap)
        try:
            latest_jjk_chap = int(latest_jjk_chap)
        except ValueError:
            latest_jjk_chap = float(latest_jjk_chap)

    op_data = retrieve_last_chap(OP_URL, "ONE PIECE")
    jjk_data = retrieve_last_chap(JJK_URL, "JUJUTSU KAISEN")

    if op_data["chapter"] != latest_op_chap:
        send_email(op_data)
        latest_op_chap = op_data["chapter"]
    else:
        print("not yet op")

    if jjk_data["chapter"] != latest_jjk_chap:
        send_email(jjk_data)
        latest_jjk_chap = jjk_data["chapter"]
    else:
        print("not yet jjk")

    with open(file="chap.txt", mode="w") as f:
        f.writelines(f"op:{latest_op_chap}\njjk:{latest_jjk_chap}")
