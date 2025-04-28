import requests
from bs4 import BeautifulSoup

login_url = "https://mmmut.samarth.edu.in/index.php/site/login"
dashboard_url = "https://mmmut.samarth.edu.in/index.php/examstudent/data-correction/view"

session = requests.Session()

response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')

csrf_token = soup.find('input', {'name': '_csrf'})['value']

login_data = {
    '_csrf': csrf_token,
    'LoginForm[username]': '',
    'LoginForm[password]': ''
}

login_response = session.post(login_url, data=login_data)

if login_response.status_code == 200 and 'dashboard' in login_response.url:
    detailsResponse = session.get(dashboard_url)
    
    detailsPage = BeautifulSoup(detailsResponse.text, 'html.parser')
    card_body = detailsPage.find("div", class_="card-body")

    table = card_body.find("table",class_="table-bordered")
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        key1, value1, key2, value2 = [cell.get_text(strip=True) for cell in cells]
        print(f"{key1}:{value1}")
        print(f"{key2}:{value2}")

    
else:
    print("Login failed")

session.close()