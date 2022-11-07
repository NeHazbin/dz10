from bs4 import BeautifulSoup
import requests
sourse = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%B3")
main_text=sourse.text
soup = BeautifulSoup(main_text,features="html.parser")
soup = soup.find('div', class_= "temperature")

soup=soup.text

print(soup)
#это работающий код для сайта погоды