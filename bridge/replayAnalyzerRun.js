function analyze_replays(){
    console.log('Bridge Connected')
    console.log('Contacting Engine')

    // Use python shell
    var {PythonShell} = require("python-shell");
    var path = require("path")

    var fileFolder = document.getElementById("FolderNameoutput").value
    var spell_check_box_value = document.getElementById("spell_check").checked
    var check_spelling = "N"

    if(spell_check_box_value == true){
        check_spelling = "Y"
    }

    var options = {
        scriptPath : path.join(__dirname, "/../engine/"),
        args : ['-p', path.join(__dirname, "/../engine/"), '-f', fileFolder, '-s', check_spelling]
    }

    var pyshell = new PythonShell('replayAnalyzer.py', options);

    pyshell.on('message', function (message) {
        // received a message sent from the Python script (a simple "print" statement)
        console.log(message);
        var div = document.getElementById("output-container")
        var output = document.createElement("output")
        output.setAttribute('class', 'output-line-item')
        output.innerHTML = message
        div.appendChild(output)
        updateScroll(div)

    });

    // end the input stream and allow the process to exit
    pyshell.end(function (err) {
        if (err){
            throw err;
        };
        console.log('finished');
    });

}

function updateScroll(element){
    element.scrollTop = element.scrollHeight;
}

