import requests
import bs4
import tkinter as tk
from bs4 import BeautifulSoup
from termcolor import colored


def get_corona_detail_of_india():
    url="https://www.mohfw.gov.in/"
    html_data=get_html_data(url)
    #gets the html elements

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div=bs.find("div",class_="col-xs-8 site-stats-count").find("ul").find_all("li")
    list=[]
    print(colored("--INDIA UPDATES--",'red',attrs=['reverse']))
    for item in info_div:
        text = colored(item.find("strong").get_text(),'green',attrs=['bold'])
        list.append(text)
    #gets the data values in order with the current status


    data = bs.find_all("span", class_="mob-show")

    x=data[2].text.strip().split("(")
    print(list[0],":",x[0])
    y = data[5].text.strip().split("(")
    print(list[1], ":", y[0])

    z=data[8].text.strip().split("(")
    print(list[2], ":", z[0])


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail_of_World():
    print(colored("----WORLD UPDATES----",'blue',attrs=['reverse']))
    url = "https://www.worldometers.info/coronavirus/#countries"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    data = s.find_all("div", class_="maincounter-number")
    print(colored(" Coronavirus Cases :",'magenta',attrs=['bold']),data[0].text.strip() )
    print(colored(" Deaths :",'red',attrs=['bold']), data[1].text.strip())
    print(colored(" Recovered :",'cyan',attrs=['bold']), data[2].text.strip())



def main():
    #main function starts from here
    print(colored("    LIVE COVID-19 TRACKER   ",attrs=['bold']))
    get_corona_detail_of_india()
    get_corona_detail_of_World()



if __name__ == "__main__":
    main()
