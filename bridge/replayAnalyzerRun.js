function analyze_replays(){

    writeOutput('Bridge Connected')
    writeOutput('Contacting Engine')

    var {PythonShell} = require("python-shell");
    var path = require("path")

    var pypath = path.join(__dirname, "/../engine/replayAnalyzer.py")

    writeOutput(pypath)

    var fileFolder = document.getElementById("FolderNameoutput").value
    var spell_check_box_value = document.getElementById("spell_check").checked
    var check_spelling = "N"

    if(spell_check_box_value == true){
        check_spelling = "Y"
    }
    var options = {
        args : ['-a', fileFolder, '-s', check_spelling]
    }
    var pyshell = new PythonShell(pypath, options);
    pyshell.on('message', function (message) {
        writeOutput(message)
    });
    pyshell.end(function (err) {
        if (err){
            throw err;
        };
        writeOutput('finished');
    });
}

