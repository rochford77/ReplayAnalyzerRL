function writeOutput(msg){
    var div = document.getElementById("output-container")
    var output = document.createElement("output")
    output.setAttribute('class', 'output-line-item')
    output.innerHTML = msg
    div.appendChild(output)
    updateScroll(div)
}

function updateScroll(element){
    element.scrollTop = element.scrollHeight;
}
