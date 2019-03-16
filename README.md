# Canvas-to-Quizlet

![Canvas to Quizlet Logo](https://i.imgur.com/49t1ZZ2.png)

Simple script to convert an HTML file of a completed Canvas quiz to a Quizlet flashcard set. 

This project was started out of need, and served as a good exercise in parsing HTML with Regex (something I'm utilizing in a larger future project.)

## Usage
You should begin with a completed Canvas quiz, where correct answers are marked:

![Canvas Quiz Example](https://i.imgur.com/JzOWMij.png)

Hit Ctrl-S to save the html file of the quiz. Run the script, `canvas-to-quizlet.py`, and when prompted paste the location of the quiz .html file into the Python console. Then paste the location of the desired output .txt file -- if none exists, one will be created. 

Copy the entirety of the .txt file and import into Quizlet by creating a new set and selecting "+ Import from Word, Excel, Google Docs, etc." and pasting. Happy studying!

## Notes
* Regardless of what you answered for a question, only the correct answer will be extracted
* Questions containing an image or table will be removed since Quizlet does not allow them to be imported
* Questions with the answer "All of the above" will be removed
