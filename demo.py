#retrieving current stock prices for a set of stock names from yahoo finance website.
#the is a simple web crawler that scraps the data and saves it
#to store the prices we write it in a csvfile


import requests
from bs4 import BeautifulSoup   #scrapping library
import csv, time, threading     #time provides use the current time and threading provides us feautures to control the flow of execution
n = 4

#empt list to store the names of the stocks
name=[]

#open a file where stock_names have been stored
file = open("stock_names.csv","r")
#read the file and simultaneously store the values in list
for line in file:
    name.append(line.strip())
    #print(line) #print this line to check if values are correctly appended
print(name) #print to check the list

base="https://in.finance.yahoo.com/quote/"  #the base you url to access the site
static = "?p=" #search index in the url.This stays common to all urls so it is names static
exchange = ".NS" #this states the market we are getting our data from. eg. BSE, NSE

url=[] #store urls in this list
#prepare the urls in correct format
for n in name:
    final = base+n+exchange+static+n+exchange
    url.append(final)
print(url) #check the urls

#function to get prices of our stocks
def getPrice():
    l = time.localtime() #get the current_time
    current_time = time.strftime("%H:%M:%S", l)
    threading.Timer(3.0, getPrice).start() #thread to stop and start the process over a specific interval of time

    for u in url:
        x = u.split("=") #this variable gets the stock name from url by splitting at '='
        r = requests.get(u) #performing the requests to the site
        data = (BeautifulSoup(r.text,"html.parser")) #getting the page in our scrapper
        value = data.find("div", {'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find("span").text #traversing through document to get our value
        #write the price received in a new csv file
        with open("stock_prices.csv",'a',newline='') as csvfile:
            stockwriter = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            stockwriter.writerow([current_time,x[1],value])
getPrice()

#finish
