# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
        text = f.read().splitlines()
        return text


def count_words():
    # [assignment] Add your code here
    text = read_file_content("story.txt")

    #Create an empty dictionary
    my_dict = dict()

    #remove the spaces and characters in the text
    for line in text:
        line = line.strip()

        #convert all characters in the text to lowercase
        line = line.lower()

        #split each word from the line
        new_words = line.split(" ") 

        for word in new_words:
            if word in my_dict:
                my_dict[word] = my_dict[word] + 1
            else:
                my_dict[word] = 1

    # print the content of my_dict
        for key in list(my_dict.keys()):
            print(key, ":", my_dict[key]) 

#     # return {"as": 10, "would": 20}

count_words()
