from flask import Blueprint, jsonify, request
from app import db
from models import Projeto
from schemas import ProjetoSchema

bp = Blueprint("projetos", __name__)
projeto_schema = ProjetoSchema()
projetos_schema = ProjetoSchema(many=True)

@bp.route("/", methods=["GET"])
def listar_projetos():
    projetos = Projeto.query.all()
    return jsonify(projetos_schema.dump(projetos))

@bp.route("/", methods=["POST"])
def criar_projeto():
    data = request.get_json()
    projeto = projeto_schema.load(data)
    db.session.add(projeto)
    db.session.commit()
    return jsonify(projeto_schema.dump(projeto)), 201

@bp.route("/<int:id>", methods=["GET"])
def obter_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    return jsonify(projeto_schema.dump(projeto))

@bp.route("/<int:id>", methods=["PUT"])
def atualizar_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    data = request.get_json()
    projeto = projeto_schema.load(data, instance=projeto)
    db.session.commit()
    return jsonify(projeto_schema.dump(projeto))

@bp.route("/<int:id>", methods=["DELETE"])
def deletar_projeto(id):
    projeto = Projeto.query.get_or_404(id)
    db.session.delete(projeto)
    db.session.commit()
    return "", 204