#!/usr/bin/env python3
""" create a program that asks for date range and returns the apod image(s) of that date range. Requires user to input api key. 
created by Ian David Meyers """

    
import requests
import json
import webbrowser
import time
def main():    
    #get the user input
    
    print("What is your api key? you will need to go to this url to request one: https://api.nasa.gov/")
    api_key = input()
    print("What is the date? i.E. 2017-01-01")
    start_date = input()
    print("What is the end date? i.E. 2017-01-02")
    end_date = input()
#create url from input
    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key +"&start_date=" + start_date + "&end_date=" + end_date
    print(url)      
    #get the data
    response = requests.get(url)
    data = response.json()
    
    #get the image url
    
    for topic in data:
        
        #print("\n The next topic is ")
        #print(topic)
        image_url = topic.get("url")
        #print(image_url)
        #open the url in the browser
        webbrowser.open(image_url)    
        

    
    
    #delay for large time frames
    time.sleep(5)




if __name__ == "__main__":
    main()
