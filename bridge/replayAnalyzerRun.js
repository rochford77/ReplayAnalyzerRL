function analyze_replays(){

    writeOutput('Bridge Connected')
    writeOutput('Contacting Engine')

    var {PythonShell} = require("python-shell");
    var path = require("path")
    var pypath = path.join(__dirname, "/../engine/replayAnalyzer.py")

    var check_spelling = "N"
    var fileFolder = document.getElementById("FolderNameoutput").value
    var spell_check_box_value = document.getElementById("spell_check").checked
    var disable_teams_enable_single_player = document.getElementById("disable_teams").checked

    if(spell_check_box_value == true){
        check_spelling = "Y"
    }
    writeOutput(pypath)

    var options = {
        args : ['-a', fileFolder, '-s', check_spelling, '-m', disable_teams_enable_single_player]
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

