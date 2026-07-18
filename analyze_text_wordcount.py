# text_sample = "Python is amazing, simply amazing! Learning Python is fun."
# print(analyze_text(text_sample))
# String Clean-up: Convert the entire string to lowercase. 
# Remove common punctuation marks (., ,, !, ?).
# List Extraction: Split the cleaned text into a list of individual words. Filter out any words that are fewer than 3 characters long.Dictionary Aggregation: Create a dictionary where the keys are the unique words (that passed the length filter) and the values are the number of times each word appears in the text.
# {
#     'python': 2, 
#     'amazing': 2, 
#     'simply': 1, 
#     'learning': 1, 
#     'fun': 1
# }
text_sample = "Python is amazing, simply amazing! Learning Python is fun."

def analyze(text):
    clean = text.lower()
    for ch in ('.', ',', '!', '?'):
        clean = clean.replace(ch,'')
        word={}
    for w in clean.split():
        if len(w)<=(3):
            continue
        if w in word:
            word[w] +=1
        else:
            word[w] = 1
    return(word)
    
print(analyze(text_sample))
    