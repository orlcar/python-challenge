# PyParagraph

import os
import string
import re

# Regex for splitting sentences taking into account other uses of punctuation
# Regex and function taken from "https://stackoverflow.com/questions/4576077/python-split-text-on-sentences"

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

# Specify file to read
textPath = os.path.join("raw_data", "paragraph_3.txt")

# Open the file
with open(textPath, "r") as textFile:

    # Get text from text file
    paragraph = textFile.read()
    
# ---- Get Sentence Count ----

    # Split paragraph into sentences
    sentence_list = split_into_sentences(paragraph)

    # Get number of senetences in paragraph from sentence list
    sentence_count = len(sentence_list)

# ---- Get Word Count ----

    # Remove punctuation from paragraph using string.punctuation (string of ASCII characters which are considered punctuation)
    for character in string.punctuation:
        paragraph = paragraph.replace(character,"")

    # Remove '/n' newlines from paragraph without punctuation
    trimmed_paragraph = paragraph.split("\n")
    jspace = " "
    trimmed_paragraph = jspace.join(trimmed_paragraph)

    # Create word list for word count from paragraph without punctuation
    word_list = trimmed_paragraph.split()

    # Get word count from word list
    word_count = len(word_list)

# ---- Get Average Letter Count ----

    # Remove spaces from trimmed paragraph
    paragraph_no_space = trimmed_paragraph.replace(" ","")

    # Count letters in paragraph without spaces
    letter_count = len(paragraph_no_space)

    # Calculate average letter count (per word)
    average_letter_count = round((letter_count / word_count), 1)

# ---- Get Average Sentence Length ----

    # Calculate average sentence length (in words)
    average_sentence_length = round((word_count / sentence_count), 1)

# ---- Print paragraph analysis to terminal ----
    print("Paragraph Analysis")
    print("-----------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Letter Count: {average_letter_count}")
    print(f"Average Sentence Length: {average_sentence_length}")