import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

pin = pd.read_csv("allpin.csv")
print(pin.head())

count = 0
for index,row in pin.iterrows():
    if(int(row['zip'])>=0):
        
        zip_code = str(int(row['zip']))
        print(zip_code)
        file_name = zip_code + ".txt"
        url = "http://www.unitedstateszipcodes.org/" + zip_code
        r  =  requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.content,"lxml")
                    
        stats = soup.find_all("table" ,{"class" : "table table-hover"})
        for stat in stats:
            data = stat.text
            file1 = open(file_name,'a+')
            file1.write(data)
        
        gender = soup.find_all("table" ,{"class" : "chart-legend table table-striped table-hover table-condensed"})
        for gender_data in gender:
            data1 = gender_data.text          
            file1.write(data1)     
        
        count = count+1
        if(count%20==0):
            time.sleep(50)
