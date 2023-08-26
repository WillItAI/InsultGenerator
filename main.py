from flask import Flask
from generate_insult import generate_insult

app = Flask(__name__)

@app.route('/generate-insult')
def generate_insult_route():
    return generate_insult()

if __name__ == '__main__':
    app.run(debug=True)
