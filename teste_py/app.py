from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_keycloak import Keycloak

load_dotenv()

app = Flask(__name__)

# Configurações do ambiente
app.config.from_object(os.environ.get("FLASK_ENV", "config.DevelopmentConfig"))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configurações do Keycloak
KEYCLOAK_REALM_PUBLIC_KEY = os.environ.get("KEYCLOAK_REALM_PUBLIC_KEY").replace('\\n', '\n') # Tratamento de quebra de linha
KEYCLOAK_AUTH_URL = os.environ.get("KEYCLOAK_AUTH_URL")
KEYCLOAK_CLIENT_ID = os.environ.get("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET = os.environ.get("KEYCLOAK_CLIENT_SECRET")

# Inicializa o Keycloak
keycloak = Keycloak(app, config={
    "realm": KEYCLOAK_REALM_PUBLIC_KEY,
    "auth_server_url": KEYCLOAK_AUTH_URL,
    "client_id": KEYCLOAK_CLIENT_ID,
    "client_secret_key": KEYCLOAK_CLIENT_SECRET
})

# Importa as rotas
from routes import projetos, tarefas, usuarios

# Registra os blueprints
app.register_blueprint(projetos.bp, url_prefix="/projetos")
app.register_blueprint(tarefas.bp, url_prefix="/tarefas")
app.register_blueprint(usuarios.bp, url_prefix="/usuarios")

# Rota de exemplo (protegida)
@app.route("/")
@keycloak.protect(role="usuario") # Protege a rota, exigindo a role "usuario"
def index():
    return "Bem-vindo ao Sistema de Gestão de Projetos!"

# Rotas para tratamento de erro de autorização
@app.errorhandler(403)
def forbidden(e):
    return jsonify({"message": "Acesso negado"}), 403

# Rotas para tratamento de erro de autenticação
@app.errorhandler(401)
def unauthorized(e):
    return jsonify({"message": "Não autenticado"}), 401

if __name__ == "__main__":
    app.run(debug=True)