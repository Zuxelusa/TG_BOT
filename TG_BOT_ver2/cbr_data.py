import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data_from_cbr():
    res = requests.get('https://cbr.ru/curreNcy_base/daily/')
    soup = BeautifulSoup(res.text, 'lxml')

    table1 = soup.find("table")

    headers = []
    for i in table1.find_all('th'):
        title = i.text
        headers.append(title)

    mydata = pd.DataFrame(columns = headers)

    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row
    return mydata.iloc[13][-1:]


