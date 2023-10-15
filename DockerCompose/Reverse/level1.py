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
    password = data.get('password', '')
    # Vérification du mot de passe
    if password == 'Arthur_mange_des_pouples':
        return {"success": True, "dns": "shadow.wargame.esd"}  # Réponse en cas de succès
    else:
        return {"success": False}  # Réponse en cas d'échec

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
