from app import db

class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    manager_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    status = db.Column(db.String(50), default="ativo")
    tarefas = db.relationship("Tarefa", backref="projeto", lazy=True)

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    assigned_to_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    status = db.Column(db.String(50), default="pendente")
    projeto_id = db.Column(db.Integer, db.ForeignKey("projeto.id"))

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(50), default="usuario")
    password = db.Column(db.String(255), nullable=False)  # TODO: Hash the password
    projetos = db.relationship("Projeto", backref="manager", lazy=True)
    tarefas = db.relationship("Tarefa", backref="assigned_to", lazy=True)