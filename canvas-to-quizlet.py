'''
Simple script to quickly and easily convert a completed Canvas quiz (in html format) to a copy/paste-able txt file
to import into Quizlet flashcards. Driven by user input in the console.

Author: Nick Henderson
'''

import re


def convert(file: str) -> dict:
    '''
    Given a string-ified html file, use Regex to extract questions and their respective correct answers.
    Clean and returns a dict of Q&A pairs
    '''
    questions = re.findall(r'"textarea_question_text">([\s\S]*?)<', file)
    answers = re.findall(r'"(.*?)(?:\.*?)(?:. This was the correct answer|. You selected this answer. This was the correct answer.)', file)

    # Zip together questions and answers into a dict for easier manipulation
    raw_pairs = dict(zip(questions, answers))
    pairs = {}

    # Since tables, images, etc. can't be pasted into Quizlet, ignore pairs containing them when copying to a new dict
    # We use the HTML entity "&lt" (<) as an indicator that a question includes a table or image
    # Also remove questions where the correct answer is just "All of the above"
    for pair in raw_pairs:
        if '&lt' not in pair and 'All of the above' not in raw_pairs[pair]:
            pairs[pair] = raw_pairs[pair]

    # Some questions have images as answers. Again, these must be ignored so we keep only questions with text answers
    pairs = {k: v for k, v in pairs.items() if len(v) >= 1}

    return pairs


def write_pairs(pairs: dict, location: str):
    '''Writes question-and-answer pairs to a text file in the Quizlet tab-separated format'''
    with open(location, 'w', encoding="utf8") as f:
        for key in pairs.keys():
            f.write(f"{key}\t{pairs[key]}\n")


def main():
    '''Program driver for user input and instructions'''
    in_location = input("Please enter the address and/or name of your input html file.\n" +
                        "Example - C:/Users/Nick/Downloads/Quiz1.html \n")

    out_location = input("Please enter the address and/or name of your output txt file.\n" +
                         "Example - C:/Users/Nick/Documents/Quiz1_Quizlet.txt \n")

    file = open(in_location, "r", encoding="utf8").read().strip()

    pairs = convert(file)
    write_pairs(pairs, out_location)

    print(f'Flashcards written to {out_location}. To import into Quizlet:')
    print('1. Create a new set')
    print('2. Click "+ Import from Word, Excel, Google Docs, etc."')
    print('3. Paste the entirety of the text file into the box and hit "Import".')
    print('Happy studying!')


if __name__ == "__main__":
    main()


