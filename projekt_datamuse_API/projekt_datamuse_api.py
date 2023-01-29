#Aufgabe 1
import requests

#Aufgabe 2
url_datamuse = "https://api.datamuse.com/words?"
mode = input('Please input the mode you want to use (ml,sl,sp,rel_[code]):')
word = input("Please input the words:")
words = word.replace(" ", "+")
url = url_datamuse + mode + "=" + words + "&max=5"


#Aufgabe 3
def synonym_words(word, num_results):
    """Returns top results for synonym words."""
    words = word.replace(" ", "+")
    url = url_datamuse + "ml=" + words + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_rs = [(rs["word"], rs["score"]) for rs in response]
    return top_rs
    
print(synonym_words("on top of", 5))

#Aufgabe 4
def rhyme_words(word, num_results):
    """Returns top rhyme words."""
    words = word.replace(" ", "+")
    url = url_datamuse + "rel_rhy=" + words + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_rs = [(rs["word"], rs["score"]) for rs in response]
    return top_rs
    
print(rhyme_words("grape", 5))

#Aufgabe 5
def antonym_words(word, num_results):
    """Returns antonym words"""
    words = word.replace(" ", "+")
    url = url_datamuse + "rel_ant=" + words + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_rs = [(rs["word"], rs["score"]) for rs in response]
    return top_rs
    
print(antonym_words("bright", 5))

from word_module import *
print(synonym_words("on top of", 5))