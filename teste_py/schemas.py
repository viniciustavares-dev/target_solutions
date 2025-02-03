from marshmallow import Schema, fields

class ProjetoSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    manager_id = fields.Integer(required=True)
    status = fields.String()

class TarefaSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String()
    assigned_to_id = fields.Integer(required=True)
    status = fields.String()
    projeto_id = fields.Integer(required=True)

class UsuarioSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    role = fields.String()