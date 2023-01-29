#Aufgabe 6
import requests
url_datamuse = "https://api.datamuse.com/words?"

def synonym_words(word, num_results):
    """Returns top results for synonym words."""
    words = word.replace(" ", "+")
    url = url_datamuse + "ml=" + words + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_rs = [(rs["word"], rs["score"]) for rs in response]
    return top_rs
    

def rhyme_words(word, num_results):
    """Returns top rhyme words."""
    words = word.replace(" ", "+")
    url = url_datamuse + "rel_rhy=" + words + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_rs = [(rs["word"], rs["score"]) for rs in response]
    return top_rs
    


def antonym_words(word, num_results):
    """Returns antonym words"""
    words = word.replace(" ", "+")
    url = url_datamuse + "rel_ant=" + words + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_rs = [(rs["word"], rs["score"]) for rs in response]
    return top_rs
    

if __name__ == "__main__":
    print(synonym_words("on top of", 5))
    print(rhyme_words("clever", 5))
    print(antonym_words("bright", 5))