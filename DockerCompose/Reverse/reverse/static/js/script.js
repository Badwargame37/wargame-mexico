function submitPasswords() {
    const passwords = Array.from(document.querySelectorAll('.password-input')).map(input => input.value);
    
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ passwords: passwords }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Congratulations! Your DNS is: ' + data.dns);
            alert('Content from notes.txt: ' + data.content);
        } else {
            alert('Failed: ' + data.reason);
        }
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    const submitButton = document.getElementById('submit-button');
    submitButton.addEventListener('click', submitPasswords);
});
