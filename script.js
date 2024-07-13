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
    } else {
        alert(result.error);
    }
});

function displayResults(result) {
    const skillsList = document.querySelector('#skills ul');
    const educationList = document.querySelector('#education ul');
    const experienceList = document.querySelector('#experience ul');
    const atsScore = document.querySelector('#ats_score p');

    skillsList.innerHTML = '';
    educationList.innerHTML = '';
    experienceList.innerHTML = '';
    atsScore.innerHTML = '';

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

    result.experience.forEach(exp => {
        const li = document.createElement('li');
        li.innerHTML = `<strong>${exp.title}</strong><br>${exp.details.join('<br>')}`;
        experienceList.appendChild(li);
    });

    atsScore.textContent = `Your ATS score is: ${result.ats_score}`;
    playNotificationSound();
}

function playNotificationSound() {
    const audio = new Audio('notification.mp3');
    audio.play();
}
