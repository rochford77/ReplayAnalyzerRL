function open_dialog(){
    const { dialog } = require('electron').remote
    dialog.showOpenDialog({
        title:"Select a folder",
        properties: ["openDirectory"]
    }, (folderPaths) => {
        // folderPaths is an array that contains all the selected paths
        if(folderPaths === undefined){
            console.log("No destination folder selected");
            document.getElementById("run_button").disabled = true;
            return
        }else{
            var div = document.getElementById("output-container")
            var output = document.createElement("output")

            output.setAttribute('class', 'output-line-item')
            output.innerHTML = "Your selected path is:  " + folderPaths 
            div.appendChild(output)
            updateScroll(div)

            document.getElementById("FolderNameoutput").innerHTML = folderPaths
            document.getElementById("run_button").disabled = false;
        }
    });;
}

