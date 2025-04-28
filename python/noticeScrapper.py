from bs4 import BeautifulSoup
import requests

url = "https://mmmut.ac.in/ExaminationSchedule"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html")

table = soup.find("table", id="ContentPlaceHolder2_ContentPlaceHolder3_GridView1")

rows = table.find_all("tr")
for row in rows:
    td = row.find("td")
    if td:
        span = td.find("span")
        title = span.text

        a = td.find("a")
        url = a.get("href")

        print(f"Title: {title} \nUrl: https://mmmut.ac.in/{url} \n")