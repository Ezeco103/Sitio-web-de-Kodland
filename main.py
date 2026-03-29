from flask import Flask
import random
import string

app = Flask(__name__)


facts_list = [
    "Más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El 60% de los trabajadores responde mensajes laborales tras su jornada.",
    "La adicción tecnológica genera un fuerte estrés al estar fuera de cobertura.",
    "Las redes sociales están diseñadas para maximizar el tiempo de permanencia."
]


@app.route("/")
def home():
    return '''
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
            <h1>Sitio Web de Kodland</h1>
            <p>Explora las diferentes secciones del proyecto:</p>
            <hr>
            <a href="/random_fact" style="font-size: 1.2em;">Dato aleatorio</a>
            <br><br>
            <a href="/secret" style="font-size: 1.2em; color: red;">Página secreta</a>
        </body>
    '''


@app.route("/random_fact")
def random_fact():
    dato = random.choice(facts_list)
    return f'''
        <body style="text-align: center; padding: 50px;">
            <h1>Dato Curioso</h1>
            <p style="font-size: 1.5em; border: 2px solid #3498db; padding: 20px; display: inline-block;">{dato}</p>
            <br><br>
            <a href="/">Volver al inicio</a>
        </body>
    '''


@app.route("/secret")
def secret_page():
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(caracteres) for i in range(12))
    
    return f'''
        <body style="background-color: #1a1a1a; color: white; font-family: sans-serif; text-align: center; padding: 50px;">
            <h1>Zona Secreta</h1>
            
            <div style="background: #333; padding: 20px; border-radius: 10px; margin-bottom: 30px;">
                <h3>Tu contraseña segura generada es:</h3>
                <code style="font-size: 2em; color: #2ecc71;">{password}</code>
                <p><small>(Refresca para generar otra)</small></p>
            </div>

            <hr>

            <h3>El Acertijo del Programador</h3>
            <p>"Soy algo que todos los programadores crean, pero nadie quiere tener..."</p>
            
            <details style="cursor: pointer; background: #e74c3c; padding: 10px; border-radius: 5px; display: inline-block;">
                <summary><b>Ver respuesta</b></summary>
                <p style="font-size: 1.5em;">¡Es un BUG!</p>
            </details>
            
            <br><br>
            <a href="/" style="color: #3498db;">← Salir de la zona secreta</a>
        </body>
    '''

if __name__ == "__main__":
    app.run(debug=True)
