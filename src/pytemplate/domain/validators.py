from marshmallow import fields, Schema, validates, ValidationError


class BurgerSchema(Schema):
    bread = fields.Str(required=True)
    patty = fields.Str(required=True)
    sauce = fields.Str(required=False)
    toppings = fields.List(fields.Str(), required=False)

    @validates("bread")
    def validate_bread(self, value):
        if not value:
            raise ValidationError("Bread is required.")

    @validates("patty")
    def validate_patty(self, value):
        if not value:
            raise ValidationError("Patty is required.")
