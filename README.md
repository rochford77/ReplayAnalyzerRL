
### About
#### ReplaySnatcher.js 

+ discord bot
+ can be used to gather replay files from a discord server. 
+ I have it running on my pi.

#### replayAnalyzer.py 

+ wrapper for [carball](https://github.com/SaltieRL/carball) 
+ This feeds carball in batches of replay files and outputs advanced stats 
+Stats are grouped by player and team. 

### Requirements

+ This project requires python 3.6.2, carball, and protobuf.

`pip install carball`

`pip install protobuf`

### Usage
`import carball`

`from google.protobuf.json_format import MessageToJson`

`python ./replayAnalyzer.py`
