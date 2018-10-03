"""
Models module
"""
from . import db


class ExampleModel(db.Model):
    """
    Example model
    """
    example_string_field: str = db.Column(db.String(20), nullable=True, unique=False)

    def example(self):
        return self.example_string_field
