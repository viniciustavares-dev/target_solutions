from flask import Blueprint, jsonify, request
from app import db
from models import Tarefa
from schemas import TarefaSchema

bp = Blueprint("tarefas", __name__)
tarefa_schema = TarefaSchema()
tarefas_schema = TarefaSchema(many=True)

@bp.route("/", methods=["GET"])
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return jsonify(tarefas_schema.dump(tarefas))

@bp.route("/", methods=["POST"])
def criar_tarefa():
    data = request.get_json()
    tarefa = tarefa_schema.load(data)
    db.session.add(tarefa)
    db.session.commit()
    return jsonify(tarefa_schema.dump(tarefa)), 201

@bp.route("/<int:id>", methods=["GET"])
def obter_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    return jsonify(tarefa_schema.dump(tarefa))

@bp.route("/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    data = request.get_json()
    tarefa = tarefa_schema.load(data, instance=tarefa)
    db.session.commit()
    return jsonify(tarefa_schema.dump(tarefa))

@bp.route("/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return "", 204