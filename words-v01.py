from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    for word in story_words:
        print(word)

# Python sets the value of dunder name differently, depeding on how our module is being used.
# The key idea we're introducing here is that our module can use this behavior to decide how it should behavior:

if __name__ == '__main__':  # id dunder name is equal to the string dunder main
    fetch_words()           # we execute the function fetch_words()

# On the other hand, if dunder name is not equal to dunder main, the module knows it's being imported into another module,
# no executed, and so only defines the fetch_words function without executing it