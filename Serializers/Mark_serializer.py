from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields


class MarkSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Mark
        load_instance = True  # Optional: deserialize to model instances

    id = fields.Int(dump_only=True)
    student_id = fields.Int(required=True)
    course_id = fields.Int(required=True)
    mark = fields.Int(required=True)
