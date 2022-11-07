import sqlite3
from bs4 import BeautifulSoup
import requests

sourse = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%B3")
main_text=sourse.text

soup = BeautifulSoup(main_text,features="html.parser")
soup = soup.find('div', class_= "temperature")
soup=soup.text

connection = sqlite3.connect("test2.sl3")
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS second_table (time TEXT,data TEXT,temperature TEXT);")
cur.execute("INSERT INTO second_table(time) VALUES('21.00');")
cur.execute("INSERT INTO second_table(data) VALUES('07.11.22');")
cur.execute(f"INSERT INTO second_table(temperature) VALUES({soup});")
connection.commit()
connection.close()



