
import requests
from bs4 import BeautifulSoup

def query():
    
    user_query = input('Enter your query: ')

    URL = "https://www.google.co.in/search?q=" + user_query + "linkedin"
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # to Get  Owner Name
    Owner_name = soup.find(class_ ='LC20lb MBeuO DKV0Md').get_text()
    print("Owner Name:" ,Owner_name)

    #for Linkedin Profile link
    answer = soup.find(class_="yuRUbf")
    linkedin_Profile_link = answer.find('a').get('href')
    print("Linkedin Profile link:",linkedin_Profile_link)
    

   


while True:
    try:
        query()
    except Exception:
        print('Sorry no result, please be clear')
    user_input = input('To continue press y: ')
    if user_input != 'y':
        break
