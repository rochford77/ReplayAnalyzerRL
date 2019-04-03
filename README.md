
## About

#### Structure
+ Engine: This folder holds all the python scripts. 
Alone, this contains a python CLI that can be used with no other parts of the project
+ GUI: This contains files specific to the Electron front-end
+ Bridge: This folder contains all the JavaScript connecting the Engine and GUI

#### replayAnalyzer.py 

+ Wrapper for [carball](https://github.com/SaltieRL/carball) 
+ This feeds carball in batches of replay files and outputs advanced stats 
+ Stats are grouped by player and team. 

## Requirements
#### In order to build the application
+ [python 3.6.2](https://www.python.org/downloads/release/python-362/)
+ [node.js](https://nodejs.org/en/)


#### In order for the app to function properly
+ See requirements.txt
+ There is also an "install requirements" button in the electron wrapper (Python 3.6.2 required)
+ [NPM Python-Shell](https://www.npmjs.com/package/python-shell)

`pip install -r requirements.txt`

`npm install python-shell`

## Usage
+ If you want to use the python CLI, cd into the engine and:

`python ./replayAnalyzer.py --abspath --spell --playlist --mode`

+ If you want to use the GUI, have node installed, cd into GUI, and:

`npm start`

+ If you are simply using the .exe installer, have python 3.6.2 or later installed and click the "install requirements" button.

#### SpellChecker
+ The file TeamNameSpellCheckerCustomLanguage.txt can be used to add/prioritize words
+ This is great for ensuring your leagues team names are the first resluts in the list
+ Helps avoid false positives
+ No delimiter needed, just spaces between words
+ This is ignored when not using spell checker
+ 100% Optional

#### Flow of app (rattletrap is a carball dependency):

![FlowImg](https://github.com/rochford77/ReplayAnalyzerRL/blob/master/extras/flow.png)
