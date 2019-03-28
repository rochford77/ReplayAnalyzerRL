function installRequirements(){
    var exec = require('child_process').exec;
    var path = require("path")
    var requirements_path = path.join(__dirname, "/../requirements.txt")
    writeOutput(requirements_path) 

    exec('pip install -r ' + requirements_path, function(error, stdout, stderr) {
        if(stderr == ""){
            writeOutput(stdout)
        }else{
            writeOutput(stdout)
            writeOutput("Error  " + stderr)
        }
    });
}

function checkPyVersion(){
    var exec = require('child_process').exec;
    
    exec('python --version', function(error, stdout, stderr) {
        if(stderr == ""){
            writeOutput("Your Python version is: " + stdout + ". ATTN: Python 3.6.2 or higher required")
        }else{
            writeOutput("Error getting Python version " + stderr + ". ATTN: Python 3.6.2 or higher required")
            writeOutput("Please visit https://www.python.org/downloads/ to install the latest version.")
            writeOutput("DO NOT FORGET TO CHECK THE ADD TO PATH BUTTON SEE: https://imgur.com/UWcWf74")
        }
    });
}

