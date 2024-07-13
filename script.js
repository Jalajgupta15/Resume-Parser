document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', document.getElementById('resume').files[0]);

    const response = await fetch('http://localhost:5000/parse_resume', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    if (response.ok) {
        displayResults(result);
        playSound();
    } else {
        alert(result.error);
    }
});

function displayResults(result) {
    const skillsList = document.querySelector('#skills ul');
    const educationList = document.querySelector('#education ul');
    skillsList.innerHTML = '';
    educationList.innerHTML = '';

    result.skills.forEach(skill => {
        const li = document.createElement('li');
        li.textContent = skill;
        skillsList.appendChild(li);
    });

    result.education.forEach(edu => {
        const li = document.createElement('li');
        li.textContent = typeof edu === 'string' ? edu : `${edu[0]} (${edu[1]})`;
        educationList.appendChild(li);
    });
}

function playSound() {
    const audio = new Audio('notification.mp3');
    audio.play();
}
