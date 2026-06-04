"""
counts each character, word and line of a given text file

"""

def char_count():
    with open("trial.txt", "r") as f:
        char_count=0
        lines=f.readlines()
        for line in lines:
            char_count+=len(line.strip("\n"))
    return char_count


def wordcount():
    with open("trial.txt", "r") as f:
        word_count=0
        for lines in f:
            words=lines.split()
            word_count+=len(words)
    return word_count


def linecount():
    count=0
    with open("trial.txt", "r") as f:
        for line in f:
            count+=1
    return count

print("number of characters:",char_count())
print("number of words:",wordcount())
print("number of lines:",linecount())






























