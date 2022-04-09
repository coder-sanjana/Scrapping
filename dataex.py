import requests #allows us to send http request using python
from bs4 import BeautifulSoup #helps to pull data from html file
import csv #to write the data into excel file
r=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html?mtrref=www.youtube.com&gwh=8C1274F0BC773766761293A39760069E&gwt=pay&assetType=PAYWALL')
soup=BeautifulSoup(r.text, 'html.parser')
#print(soup)
results=soup.find_all('span', attrs={'class':'short-desc'})
#print(len(results))#printing the number of results
a=results[0:5] #getting 5 results as an example from the page

#Writing the data into a csv file#
with open('TOI.csv','w+',newline='') as file:
    write=csv.writer(file)
    write.writerow(['Date','Lie','Explanation','Link'])
    for i in a:
        date=i.find('strong').text
        lie=i.contents[1]
        exp=i.find('a').text[1:-1]
        link=i.find('a')['href']
        write.writerow([date,lie,exp,link])
    file.close()
