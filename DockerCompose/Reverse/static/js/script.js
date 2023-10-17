async function submitPasswords() {
    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;
    const password3 = document.getElementById('password3').value;
    const password4 = document.getElementById('password4').value;

    const response = await fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            passwords: [password1, password2, password3, password4]
        }),
    });
    
    const data = await response.json();
    
    if (data.success) {
        alert('Congratulations! Your DNS is: ' + data.dns);
        alert('Content from notes.txt: ' + data.content);
    } else {
        alert('Failed: ' + data.reason);
    }
}
