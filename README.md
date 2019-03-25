
### About

#### replayAnalyzer.py 

+ wrapper for [carball](https://github.com/SaltieRL/carball) 
+ This feeds carball in batches of replay files and outputs advanced stats 
+ Stats are grouped by player and team. 

### Requirements

+ [python 3.6.2](https://www.python.org/downloads/release/python-362/)
+ See requirements.txt

`pip install -r requirements.txt`

+ There is also an "install requirements" button in the electron wrapper (Python 3.6.2 required)



### Usage
+ If you want to use the python CLI, cd into the engine and:

`python ./replayAnalyzer.py --folder --spell --playlist`

+ If you want to use the GUI, have node installed, cd into GUI, and:

`npm start`

### SpellChecker
+ The file TeamNameSpellCheckerCustomLanguage.txt can be used to add/prioritize words
+ This is great for ensuring your leagues team names are the first resluts in the list
+ Helps avoid false positives
+ No delimiter needed, just spaces between words
+ This is ignored when not using spell checker
+ 100% Optional
