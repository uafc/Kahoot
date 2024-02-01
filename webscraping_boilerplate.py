from bs4 import BeautifulSoup
import requests

def scrape_questions_and_answers():
    questions_dict = {}  # Using a dictionary for questions and answers
    url = ""
    response = requests.get(url)
    
    #check if scraping is allowed 
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    #write your webscraping logic/code below!

    return dict

def main():
    scraped_data = scrape_questions_and_answers()

main()
