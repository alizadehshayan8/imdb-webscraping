import imp
from pydoc import pager
from matplotlib import projections
import requests
import numpy as np , openpyxl
from bs4 import BeautifulSoup
from time import sleep 
from random import randint


#excel handler
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="TOP 1000 imdb"
sheet.append(["Movie Rank","Movie Name","Year of Release","Rating","genre"])





pages= np.arange(1,1000,100)

for page in pages:
    url=f"https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start={str(page)}&ref_=adv_nxt"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")

    movie_data=soup.find("div" , class_="lister-list").find_all("div", class_="lister-item mode-advanced")
    
    sleep(randint(2,8))
    for store in movie_data:
        #movie name
        name=store.h3.a.text
        
        #movie rank
        rank=store.h3.span.text.strip(".")
        

        #movie year 
        year=store.h3.find("span" , class_="lister-item-year text-muted unbold").text.strip("()")
        
       
        #movie rate
        rate=store.find("div" , class_="ratings-bar").strong.text
        
        
        #movie genre
        genre=store.find("span" , class_="genre").text
        
        
        
        sheet.append([rank , name , year , rate , genre])


excel.save("imdb1000top.xlsx")  
        

        
      
       

    
    
   
    


    