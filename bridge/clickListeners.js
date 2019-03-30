
window.onload=function(){
    const { dialog } = require('electron')

    document.getElementById("run_button").disabled = true;
    document.getElementById("playlist_filter_select").disabled = true

    document.getElementById("check_python").addEventListener("click", function(){
        try{
            checkPyVersion()
        }
        catch(e){
            dialog.showMessageBox(e.message)
        }
    });

    document.getElementById("run_button").addEventListener("click", function(){
        try{
            analyze_replays()
        }
        catch(e){
            dialog.showMessageBox(e.message)
        }
    });

    document.getElementById("install_req").addEventListener("click", function(){
        try{
            installRequirements()
        }
        catch(e){
            dialog.showMessageBox(e.message)
        }
    });

    document.getElementById("playlist_filter_check").addEventListener("click", function(){
        var select_dropdown = document.getElementById("playlist_filter_select")
        if (select_dropdown.disabled == true){
            document.getElementById("playlist_filter_select").disabled = false
        }else{
            document.getElementById("playlist_filter_select").disabled = true
        }
    });
    
    document.getElementById("select_folder").addEventListener("click", function(){
        try{
            open_dialog()
        }
        catch(e){
            dialog.showMessageBox(e.message)
        }
    });
}