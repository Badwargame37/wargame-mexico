from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)
app.secret_key = 'une_clé_secrète_très_sûre'  # Assurez-vous de générer une clé secrète forte et unique

@app.route('/')
def index():
    return render_template('index.html')  # Renvoie le fichier HTML index.html

@app.route('/download')
def download():
    return send_from_directory(directory='.', path='Challenge.zip')  # Sert le fichier challX.zip

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    passwords = data.get('passwords', [])  # Supposons que 'passwords' soit une liste

    # Mots de passe hashés pour comparaison
    valid_passwords = [
        'Flag123',
        'internet',
        '500379d15e1f3c1ca605168b62f367cbdab8abde2b64f236972903f9ff3f63a5',
        'tequiero'
    ]

    # Vérifier tous les mots de passe
    if all(p in valid_passwords for p in passwords):
        with open('arch.txt', 'r') as f:
            content = f.read()
        return {"success": True, "content": content, "dns": "bastion.esd37.com"}
    else:
        return {"success": False}

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)
