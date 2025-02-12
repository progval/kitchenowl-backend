from marshmallow import fields, Schema
from app.config import SUPPORTED_LANGUAGES


class OnboardSchema(Schema):
    name = fields.String(
        required=True,
        validate=lambda a: a and not a.isspace()
    )
    username = fields.String(
        required=True,
        validate=lambda a: a and not a.isspace()
    )
    password = fields.String(
        required=True,
        validate=lambda a: a and not a.isspace()
    )
    planner_feature = fields.Boolean()
    expenses_feature = fields.Boolean()
    language = fields.String(
        validate=lambda a: a and not a.isspace() and a in SUPPORTED_LANGUAGES
    )
    device = fields.String(
        required=False,
        validate=lambda a: a and not a.isspace(),
        load_only=True,
    )
