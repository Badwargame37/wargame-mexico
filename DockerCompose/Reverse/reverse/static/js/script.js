

function submitPassword() {
    const passwords = [
        document.getElementById('password1').value,
        document.getElementById('password2').value,
        document.getElementById('password3').value,
        document.getElementById('password4').value
    ];

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({passwords: passwords}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Félicitations! Votre DNS est: ' + data.dns);
            console.log('Contenu de notes.txt:', data.content);  // Vous pouvez également l'afficher d'une autre manière
        } else {
            alert('Un ou plusieurs mots de passe sont incorrects, essayez à nouveau.');
        }
    });
}
document.addEventListener('DOMContentLoaded', (event) => {
    const submitButton = document.getElementById('submit-button');
    submitButton.addEventListener('click', submitPassword);
});