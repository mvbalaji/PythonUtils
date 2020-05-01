

import pandas as pd,wget, bs4, requests

for index,row in pd.read_excel("Springer Ebooks.xlsx").iterrows():
    search_url="https://link.springer.com/search?query="+str(row["OpenURL"]).split("=")[-1]+"&facet-content-type=%22Book%22"
    
    for s in bs4.BeautifulSoup(requests.get(search_url).content, 'html5lib').prettify().split("\n"):
        if("/book/10" in s):
            wget.download("https://link.springer.com/content/pdf"+(s.split("href=")[1].split(" ")[0].replace('"',"").replace("book/",""))+".pdf",str(row["Book Title"])+".pdf") 
            break
