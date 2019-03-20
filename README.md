
### About

#### replayAnalyzer.py 

+ wrapper for [carball](https://github.com/SaltieRL/carball) 
+ This feeds carball in batches of replay files and outputs advanced stats 
+ Stats are grouped by player and team. 

### Requirements

+ [python 3.6.2](https://www.python.org/downloads/release/python-362/)
+ [carball](https://github.com/SaltieRL/carball) 
+ [protobuf](https://developers.google.com/protocol-buffers/)
+ [PySpellChecker](https://pypi.org/project/pyspellchecker/)

`pip install carball`

`pip install protobuf`

`pip install pyspellchecker`

### Usage
`import carball`

`from google.protobuf.json_format import MessageToJson`

`from spellchecker import SpellChecker`

`python ./replayAnalyzer.py -f folder_path -s Y/N`
