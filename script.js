const subtitle = document.getElementById("text");

fetch("recording.json")
    .then((response) => response.json())
    .then((data) => {
        subtitle.innerText = data.text;
    });

