import pandas as pd
import os.path
 

pin = pd.read_csv("allpin.csv")

print(pin)

zen = []
zen = []
for index,row in pin.iterrows():
    zip_code = str(int(row['zip']))
    print(zip_code)
    file_name = zip_code + ".txt"
    if(os.path.isfile(file_name)):
        file = open(file_name,'r')
        string = file.read()
        string_list = string.split("\n")
        string_list = list(filter(None, string_list))
        
        vallist = []
        
        vallist.append(zip_code)
        for element in string_list:
            if((element[0].isdigit()) or (element[0]=='$')):
                vallist.append(str(element))
        zen.append(vallist)
                
print(zen)               
df = pd.DataFrame(zen)
print(df)
df.to_csv("demographic.csv")        