from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

school = int(input('please enter a school ID, e.g. School of Dentistry(202), School of Medicine(101):\n'))
year = int(input('please enter the year of admission:\n'))
number = int(input('please enter the number of students in the class:\n'))
file_name = input('please enter the file name:\n')

names = []

for i in range(1,number+1):
    n = "%03d" % i
    try:
        html = urlopen(f'http://my2.tmu.edu.tw/b{school}{year}{n}')
        soup = BeautifulSoup(html.read())
        profile = soup.find("div", {"id": "profile"})
        name = profile.find_all('div')[1].find('div').text
    except:
        name = None
    names.append(name)
    print(i, name)

df = pd.DataFrame(names, index=list(range(1,number+1)))

df.to_excel(f'{file_name}.xlsx',sheet_name='sheet1')
