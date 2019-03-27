function installRequirements(){
    var exec = require('child_process').exec;
    var path = require("path")

    var requirements_path = path.join(__dirname, "/requirements.txt")


    var div1 = document.getElementById("output-container")
        var output1 = document.createElement("output")
        output1.setAttribute('class', 'output-line-item')
        output1.innerHTML = requirements_path
        div1.appendChild(output1)
        updateScroll(div1)

    exec('pip install -r ' + requirements_path, function(error, stdout, stderr) {
        var div = document.getElementById("output-container")
        var output = document.createElement("output")
        output.setAttribute('class', 'output-line-item')

        if(stderr == ""){
            output.innerHTML =  stdout 

        }else{
            output.innerHTML =  stdout 
            output.innerHTML = "Error  " + stderr
        }

        div.appendChild(output)
        updateScroll(div)
    });
}

function checkPyVersion(){
    var exec = require('child_process').exec;
    exec('python --version', function(error, stdout, stderr) {
        
        var div = document.getElementById("output-container")
        var output = document.createElement("output")
        output.setAttribute('class', 'output-line-item')

        if(stderr == ""){
            output.innerHTML = "Your Python version is: " + stdout + ". ATTN: Python 3.6.2 or higher required"
            div.appendChild(output)
        }else{
            output.innerHTML = "Error getting Python version " + stderr + ". ATTN: Python 3.6.2 or higher required"
            var help1 = document.createElement("output")
            help1.setAttribute('class', 'output-line-item')
            help1.innerHTML = "Please visit https://www.python.org/downloads/ to install the latest version."
            var help2 = document.createElement("output")
            help2.setAttribute('class', 'output-line-item')
            help2.innerHTML = "DO NOT FORGET TO CHECK THE ADD TO PATH BUTTON SEE: https://imgur.com/UWcWf74"
            div.appendChild(output)
            div.appendChild(help1)
            div.appendChild(help2)
        }
        updateScroll(div)
    });
}

