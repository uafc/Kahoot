from bs4 import BeautifulSoup
import requests

def scrape_questions_and_answers():
    questions_dict = {}  # Using a dictionary for questions and answers
    url = "https://abinandn1.github.io/UAFCKahoot/"
    response = requests.get(url)
    
    #check if scraping is allowed 
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")

    question_sections = soup.find_all('div', {'class': 'question_box'})
    for trivia_question in question_sections:
        
        #extract the question
        question = trivia_question.find('h2', {'class': 'question'}).text.strip()

        #extract choices
        answers = trivia_question.find_all('ul', {'class': 'answers'})[0].find_all('li')
        choices = [choice.text.strip() for choice in answers]
        
        #extract correct answer
        correct_answer = trivia_question.find('li', {'class': 'correct_answer'}).text.strip()

        # add question, choices, and correct answer to the dictionary
        questions_dict[question] = [choices, [correct_answer]]

    return questions_dict

def main():
    data = scrape_questions_and_answers()

main()
