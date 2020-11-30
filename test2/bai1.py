import requests
import bs4

data = {'log': 'admin', 'pwd': '123456aA'}

url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'

res = requests.post(url, data=data)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
username = soup.select('#wp-admin-bar-site-name > a')
print(username[0].text.strip())