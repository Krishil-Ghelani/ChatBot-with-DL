from chatbot.base import app
from chatbot.base import db
import flask as f

class TableVo(db.Model):
    __tablename__ = "newdatatable"
    category_id = db.Column('category_id', db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column('category_name', db.String(255), nullable=False)
    category_description = db.Column('category_description', db.Text, nullable=False)

    def as_dict(self):
        return {
        'category_id' : self.category_id,
        'category_name' : self.category_name,
        'category_description' : self.category_description
        }

db.create_all()