# Making a CRUD API for library book systems

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data/library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

print(app.config['SQLALCHEMY_DATABASE_URI'])


class Category(db.Model):
    # category Class/Model
    Category_ID = db.Column(db.String(25), primary_key=True)
    Description = db.Column(db.String(200))

    def __init__(self, id, description):
        self.Category_ID = id
        self.Description = description


class CategorySchema(ma.Schema):
    class Meta:
        fields = ('Category_ID', 'Description')


# Init schema
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@app.route('/category', methods=['POST'])
def add_category():
    id = request.json['id']
    description = request.json['description']

    new_category = Category(id, description)
    db.session.add(new_category)
    db.session.commit()

    return category_schema.jsonify(new_category)


@app.route('/category', methods=['GET'])
def get_categories():
    # Get All category
    all_categories = Category.query.all()
    return categories_schema.jsonify(all_categories)


@app.route('/category/<id>', methods=['GET'])
def get_category(id):
    # Get Single category
    category = Category.query.get(id)
    return category_schema.jsonify(category)


@app.route('/category/<id>', methods=['PUT'])
def update_category(id):
    # Update a category
    category = Category.query.get(id)
    id = request.json['id']
    description = request.json['description']

    category.Category_ID = id
    category.Description = description
    db.session.commit()

    return category_schema.jsonify(category)


@app.route('/category/<id>', methods=['DELETE'])
def delete_category(id):
    # Delete category
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()

    return category_schema.jsonify(category)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
