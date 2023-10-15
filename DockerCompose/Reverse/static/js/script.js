function submitPassword() {
    const password = document.getElementById('password').value;
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({password: password}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Félicitations! Votre DNS est: ' + data.dns);
        } else {
            alert('Mot de passe incorrect, essayez à nouveau.');
        }
    });
}
document.addEventListener('DOMContentLoaded', (event) => {
    const submitButton = document.getElementById('submit-button');
    submitButton.addEventListener('click', submitPassword);
});