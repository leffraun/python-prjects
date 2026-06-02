"""Write a function char_frequency(text) that:

Counts frequency of each character (ignore spaces).

Returns a dictionary sorted by frequency (highest first).

Example Input:
"hello world"
Output:
{'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
"""



text=input("enter sentence to count the number of occurences of each letter in it:")

def char_frequency (text):
    occurences={} #where we store count
    for word in text.lower():
        if word!=" ":
            if word in occurences:
                occurences[word]+=1
            else:
                occurences[word]=1

    return sorted(occurences.items(), key=lambda w: w[1], reverse=True)

print(char_frequency(text))
