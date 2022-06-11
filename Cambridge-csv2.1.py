import requests
from fake_useragent import UserAgent
from urllib.request import urlopen
from bs4 import BeautifulSoup        
import csv


a=["analyze","anniversary","approximately","attention","circumstance","competitor","complete","conflict","contain","current","deny","enhance","experiment","facilitate","foremost","generously","grant","integral","launch","mandatory","nearly","once","originally","persuade","preparation","productive","purpose","reduce","release","respective","result","search","sequence","specialization","supervisor","target","timely","transition","unexpectedly","unfavorable"]
spam=[]
outputFile=open("output.csv","w",newline="")

ua = UserAgent()
user_agent = ua.random
V_headers = {'user-agent': user_agent}

for x in a:
    quote_page_a = "https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E/"+x
    page_a = requests.get(quote_page_a,headers=V_headers)
    page_a_text = page_a.text
    soup = BeautifulSoup(page_a_text, "html.parser")
    b_tag_a = soup.find_all("div", class_="def ddef_d db")
    for i in range(len(b_tag_a)):
        tag_a=b_tag_a[i].text
        if tag_a.find(":")!=-1:
            spam.append(tag_a)
            spam = list(set(spam))
    spam = [''.join(spam)]
    spam.insert (0, x)
    outputWritter=csv.writer(outputFile)
    outputWritter.writerow(spam)
    del spam[0:len(spam)+1]
outputFile.close() 
