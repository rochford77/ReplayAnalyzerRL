window.onload=function(){
    document.getElementById("run_button").disabled = true;
    document.getElementById("check_python").addEventListener("click", function(){
        checkPyVersion()
    });

    document.getElementById("run_button").addEventListener("click", function(){
        analyze_replays()
    });

    document.getElementById("install_req").addEventListener("click", function(){
        installRequirements()
    });
    
    document.getElementById("select_folder").addEventListener("click", function(){
        open_dialog()
    });
}