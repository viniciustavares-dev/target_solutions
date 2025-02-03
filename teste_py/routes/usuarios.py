from flask import Blueprint, jsonify, request
from app import db
from models import Usuario
from schemas import UsuarioSchema

bp = Blueprint("usuarios", __name__)
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

@bp.route("/", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify(usuarios_schema.dump(usuarios))

@bp.route("/", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    usuario = usuario_schema.load(data)
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario_schema.dump(usuario)), 201

@bp.route("/<int:id>", methods=["GET"])
def obter_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario_schema.dump(usuario))

@bp.route("/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
    usuario = usuario_schema.load(data, instance=usuario)
    db.session.commit()
    return jsonify(usuario_schema.dump(usuario))

@bp.route("/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return "", 204