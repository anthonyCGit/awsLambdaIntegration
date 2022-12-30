import io

def remove_punctuations(string: str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
    return string


# Cleans up and processes a text for use in our data structure
# This method is specific to the AI assignment text files. You'll have to implement
# your own line processing function to clean up general text.
def get_processed_lines(text: str):
    file = io.StringIO(text)
    lines = []
    line = file.readline()
    while line:
        if line != '\n':
             line = remove_punctuations(line.strip().lower())
             lines.append(line)
        line = file.readline()
    return lines


# Takes a list of lines of text and converts it into a list of words
def get_word_list(lines: list):
    w_list = []
    for line in lines:
        words = line.split()
        w_list.extend(words)
    return w_list
    