function parseResume() {
    var resumeText = document.getElementById("resumeText").value;
    
    fetch("/parse_resume", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ resume_text: resumeText })
    })
    .then(response => response.json())
    .then(data => {
        displayResult(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function displayResult(data) {
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "";
    
    var heading = document.createElement("h2");
    heading.textContent = "Parsed Resume Details";
    resultDiv.appendChild(heading);

    for (var key in data) {
        var item = document.createElement("p");
        item.innerHTML = "<strong>" + key + ":</strong> " + data[key];
        resultDiv.appendChild(item);
    }
}
