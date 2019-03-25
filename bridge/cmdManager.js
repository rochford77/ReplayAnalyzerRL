function installRequirements(){
    var exec = require('child_process').exec;
    exec('pip install -r ..\\requirements.txt ', function(error, stdout, stderr) {
        var div = document.getElementById("output-container")
        var output = document.createElement("output")
        output.setAttribute('class', 'output-line-item')

        if(stderr == ""){
            output.innerHTML =  stdout 

        }else{
            output.innerHTML = "Error  " + stderr
        }

        div.appendChild(output)
        updateScroll(div)
    });

    exec('npm install python-shell', function(error, stdout, stderr) {
        var div = document.getElementById("output-container")
        var output = document.createElement("output")
        output.setAttribute('class', 'output-line-item')

        if(stderr == ""){
            output.innerHTML =  stdout 

        }else{
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

        }else{
            output.innerHTML = "Error getting Python version " + stderr + ". ATTN: Python 3.6.2 or higher required"
        }

        div.appendChild(output)
        updateScroll(div)

    });
}

