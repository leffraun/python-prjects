"""Write a function rearrange_words(sentence) that:

Takes a sentence as input.

Removes punctuation.

Splits into words.

Returns a list of words sorted by length, then alphabetically.

Example Input:  
"Hackerrank is the best platform!"  
Output:  
['is', 'the', 'best', 'platform', 'Hackerrank']
"""


sentence=input("gimme your sentence:")
def rearrange(sentence):
    punc=[",",".","!","@","?"]
    cleaned=[]
    for words in sentence.split():
        for marks in punc:
            words=words.replace(marks,"")
        cleaned.append(words)
    return sorted(cleaned, key=lambda w:(len(w),w.lower()))

print(rearrange(sentence))
