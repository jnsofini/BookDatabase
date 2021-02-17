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


class Author(db.Model):
    # Author Class/Model
    Author_ID = db.Column(db.String(25), primary_key=True)
    Author_Name = db.Column(db.String(255))

    def __init__(self, id, a_name):
        self.Author_ID = id
        self.Author_Name = a_name


class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('Author_ID', 'Author_Name')


# Init schema
Author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


@app.route('/Author', methods=['POST'])
def add_Author():
    id = request.json['id']
    a_name = request.json['a_name']

    new_Author = Author(id, a_name)
    db.session.add(new_Author)
    db.session.commit()

    return Author_schema.jsonify(new_Author)


@app.route('/Author', methods=['GET'])
def get_authors():
    # Get All Author
    all_authors = Author.query.all()
    return authors_schema.jsonify(all_authors)


@app.route('/Author/<id>', methods=['GET'])
def get_Author(id):
    # Get Single Author
    author = Author.query.get(id)
    return Author_schema.jsonify(author)


@app.route('/Author/<id>', methods=['PUT'])
def update_Author(id):
    # Update a Author
    author = Author.query.get(id)
    id = request.json['id']
    a_name = request.json['a_name']

    Author.Author_ID = id
    Author.a_name = a_name
    db.session.commit()

    return Author_schema.jsonify(author)


@app.route('/Author/<id>', methods=['DELETE'])
def delete_Author(id):
    # Delete Author
    author = Author.query.get(id)
    db.session.delete(author)
    db.session.commit()

    return Author_schema.jsonify(author)


# Book Class
class Book(db.Model):
    # Book Class/Model
    ISBN = db.Column(db.String(25), primary_key=True)
    Title = db.Column(db.String(255))
    Year = db.Column(db.String(255))
    Description = db.Column(db.String(255))
    Publisher = db.Column(db.String(255))
    Number_pages = db.Column(db.Integer)

    def __init__(self, idbook, title, year, descriptionBook, publisher, pages):
        self.ISBN = idbook
        self.Title = title
        self.Year = year 
        self.Description = descriptionBook 
        self.Publisher = publisher 
        self.Number_pages = pages 


class BookSchema(ma.Schema):
    class Meta:
        fields = ('ISBN', 'Title', 'Year', 'Description', 'Publisher', 'Number_pages')


# Init schema
Book_schema = BookSchema()
books_schema = BookSchema(many=True)


@app.route('/Book', methods=['POST'])
def add_Book():
    idbook = request.json['idbook']
    title = request.json['title']
    year = request.json['year']
    descriptionBook = request.json['descriptionBook']
    publisher = request.json['publisher']
    pages = request.json['pages']

    new_Book = Book(idbook, title, year, descriptionBook, publisher, pages)
    db.session.add(new_Book)
    db.session.commit()

    return Book_schema.jsonify(new_Book)


@app.route('/Book', methods=['GET'])
def get_books():
    # Get All Book
    all_books = Book.query.all()
    return books_schema.jsonify(all_books)


@app.route('/Book/<idbook>', methods=['GET'])
def get_Book(idbook):
    # Get Single Book
    book = Book.query.get(idbook)
    return Book_schema.jsonify(book)


@app.route('/Book/<idbook>', methods=['PUT'])
def update_Book(idbook):
    # Update a Book
    book = Book.query.get(idbook)
    idbook = request.json['idbook']
    title = request.json['title']
    year = request.json['year']
    descriptionBook = request.json['descriptionBook']
    publisher = request.json['publisher']
    pages = request.json['pages']

    Book.ISBN = idbook
    Book.title = title
    Book.year = year
    Book.descriptionBook = descriptionBook
    Book.publisher = publisher
    Book.pages = pages
    db.session.commit()

    return Book_schema.jsonify(book)


@app.route('/Book/<idbook>', methods=['DELETE'])
def delete_Book(idbook):
    # Delete Book
    book = Book.query.get(idbook)
    db.session.delete(book)
    db.session.commit()

    return Book_schema.jsonify(book)


# Author_Book Class
class AuthorBook(db.Model):
    # AuthorBook Class/Model
    Author_ID = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.Integer, primary_key=True)

    def __init__(self, idb, isbn):
        self.Author_ID = idb
        self.ISBN = isbn


class AuthorBookSchema(ma.Schema):
    class Meta:
        fields = ('Author_ID', 'ISBN')


# Init schema
AuthorBook_schema = AuthorBookSchema()
authorsBook_schema = AuthorBookSchema(many=True)


@app.route('/AuthorBook', methods=['POST'])
def add_AuthorBook():
    idb = request.json['idb']
    isbn = request.json['isbn']

    new_AuthorBook = AuthorBook(idb, isbn)
    db.session.add(new_AuthorBook)
    db.session.commit()

    return AuthorBook_schema.jsonify(new_AuthorBook)


@app.route('/AuthorBook', methods=['GET'])
def get_authorsBook():
    # Get All AuthorBook
    all_authorsBook = AuthorBook.query.all()
    return authorsBook_schema.jsonify(all_authorsBook)


@app.route('/AuthorBook/<idb>', methods=['GET'])
def get_AuthorBook(idb):
    # Get Single AuthorBook
    authorBook = AuthorBook.query.get(idb)
    return AuthorBook_schema.jsonify(authorBook)


@app.route('/AuthorBook/<idb>', methods=['PUT'])
def update_AuthorBook(idb):
    # Update a Author
    authorBook = AuthorBook.query.get(idb)
    idb = request.json['idb']
    isbn = request.json['isbn']

    AuthorBook.Author_ID = idb
    AuthorBook.isbn = isbn
    db.session.commit()

    return AuthorBook_schema.jsonify(authorBook)


@app.route('/AuthorBook/<idb>', methods=['DELETE'])
def delete_AuthorBook(idb):
    # Delete AuthorBook
    authorBook = AuthorBook.query.get(idb)
    db.session.delete(authorBook)
    db.session.commit()

    return AuthorBook_schema.jsonify(authorBook)



# Category Class
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


# Book_Category Class
class BookCategory(db.Model):
    # BookCategory Class/Model
    Category_ID = db.Column(db.String(25), primary_key=True)
    ISBN = db.Column(db.Integer)

    def __init__(self, idbc, isbn):
        self.Category_ID = idbc
        self.ISBN = isbn


class BookCategorySchema(ma.Schema):
    class Meta:
        fields = ('ISBN', 'Category_ID')


# Init schema
bookcategory_schema = BookCategorySchema()
bookcategories_schema = BookCategorySchema(many=True)


@app.route('/BookCategory', methods=['POST'])
def add_bookcategory():
    idbc = request.json['idbc']
    isbn = request.json['isbn']

    new_bookcategory = BookCategory(idbc, isbn)
    db.session.add(new_bookcategory)
    db.session.commit()

    return bookcategory_schema.jsonify(new_bookcategory)


@app.route('/BookCategory', methods=['GET'])
def get_bookcategories():
    # Get All bookcategory
    all_bookcategories = BookCategory.query.all()
    return bookcategories_schema.jsonify(all_bookcategories)


@app.route('/BookCategory/<idbc>', methods=['GET'])
def get_bookcategory(idbc):
    # Get Single bookcategory
    bookcategory = BookCategory.query.get(idbc)
    return bookcategory_schema.jsonify(bookcategory)


@app.route('/BookCategory/<idbc>', methods=['PUT'])
def update_bookcategory(idbc):
    # Update a bookcategory
    bookcategory = BookCategory.query.get(idbc)
    idbc = request.json['idbc']
    isbn = request.json['isbn']

    bookcategory.Category_ID = idbc
    bookcategory.isbn = isbn
    db.session.commit()

    return bookcategory_schema.jsonify(bookcategory)


@app.route('/BookCategory/<idbc>', methods=['DELETE'])
def delete_bookcategory(idbc):
    # Delete bookcategory
    bookcategory = BookCategory.query.get(idbc)
    db.session.delete(bookcategory)
    db.session.commit()

    return bookcategory_schema.jsonify(bookcategory)


# Borrower Class
class Borrower(db.Model):
    # Borrower Class/Model
    Borrower_ID = db.Column(db.String(25), primary_key=True)
    FirstName = db.Column(db.String(200))
    LastName = db.Column(db.String(200))
    City = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    PhoneNumber = db.Column(db.Integer)
    ISBN = db.Column(db.Integer)

    def __init__(self, b_id, bfName, blName, city, email, pnumber, isbn):
        self.Borrowe_ID = b_id
        self.FirstName = bfName
        self.LastName = blName
        self.City = city
        self.Email = email
        self.PhoneNumber = pnumber
        self.ISBN = isbn


class BorrowerSchema(ma.Schema):
    class Meta:
        fields = ('Borrower_ID', 'FirstName', 'LastName', 'City', 'Email', 'PhoneNumber', 'isbn')


# Init schema
Borrower_schema = BorrowerSchema()
borrowers_schema = BorrowerSchema(many=True)


@app.route('/Borrower', methods=['POST'])
def add_Borrower():
    b_id = request.json['b_id']
    bfName = request.json['bfName']
    blName = request.json['blName']
    city = request.json['city']
    email = request.json['email']
    pnumber = request.json['pnumber']
    isbn = request.json['isbn']

    new_borrower = Borrower(b_id, bfName, blName, city, email, pnumber, isbn)
    db.session.add(new_borrower)
    db.session.commit()

    return Borrower_schema.jsonify(new_borrower)


@app.route('/Borrower', methods=['GET'])
def get_borrowers():
    # Get All Borrowers
    all_borrowers = Borrower.query.all()
    return borrowers_schema.jsonify(all_borrowers)


@app.route('/Borrower/<b_id>', methods=['GET'])
def get_Borrower(b_id):
    # Get Single Borrower
    borrower = Borrower.query.get(b_id)
    return Borrower_schema.jsonify(borrower)


@app.route('/Borrower/<b_id>', methods=['PUT'])
def update_Borrower(b_id):
    # Update a Borrower
    borrower = Borrower.query.get(b_id)
    b_id = request.json['b_id']
    bfName = request.json['bfName']
    blName = request.json['blName']
    city = request.json['city']
    email = request.json['email']
    pnumber = request.json['pnumber']
    isbn = request.json['isbn']

    borrower.Borrower_ID = b_id
    borrower.FirstName = bfName
    borrower.LastName = blName
    borrower.City = city
    borrower.Email = email
    borrower.PhoneNumber = pnumber
    borrower.ISBN = isbn
    db.session.commit()

    return Borrower_schema.jsonify(borrower)


@app.route('/Borrower/<b_id>', methods=['DELETE'])
def delete_Borrower(b_id):
    # Delete Borrower
    borrower = Borrower.query.get(b_id)
    db.session.delete(borrower)
    db.session.commit()

    return Borrower_schema.jsonify(borrower)



# Lender Class
class Lender(db.Model):
    # Lender Class/Model
    Lender_ID = db.Column(db.String(25), primary_key=True)
    FirstName = db.Column(db.String(200))
    LastName = db.Column(db.String(200))
    City = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    PhoneNumber = db.Column(db.Integer)
    ISBN = db.Column(db.Integer)

    def __init__(self, l_id, lfName, llName, city, email, pnumber, isbn):
        self.Lender_ID = l_id
        self.FirstName = lfName
        self.LastName = llName
        self.City = city
        self.Email = email
        self.PhoneNumber = pnumber
        self.ISBN = isbn


class LenderSchema(ma.Schema):
    class Meta:
        fields = ('Lender_ID', 'FirstName', 'LastName', 'City', 'Email', 'PhoneNumber', 'isbn')


# Init schema
Lender_schema = LenderSchema()
lenders_schema = LenderSchema(many=True)


@app.route('/Lender', methods=['POST'])
def add_Lender():
    l_id = request.json['l_id']
    lfName = request.json['lfName']
    llName = request.json['llName']
    city = request.json['city']
    email = request.json['email']
    pnumber = request.json['pnumber']
    isbn = request.json['isbn']

    new_lender = Lender(l_id, lfName, llName, city, email, pnumber, isbn)
    db.session.add(new_lender)
    db.session.commit()

    return Lender_schema.jsonify(new_lender)


@app.route('/Lender', methods=['GET'])
def get_lenders():
    # Get All Lenders
    all_lenders = Lender.query.all()
    return lenders_schema.jsonify(all_lenders)


@app.route('/Lender/<l_id>', methods=['GET'])
def get_Lender(l_id):
    # Get Single Lender
    lender = Lender.query.get(l_id)
    return Lender_schema.jsonify(lender)


@app.route('/Lender/<l_id>', methods=['PUT'])
def update_Lender(l_id):
    # Update a Lender
    lender = Lender.query.get(l_id)
    l_id = request.json['l_id']
    lfName = request.json['lfName']
    llName = request.json['llName']
    city = request.json['city']
    email = request.json['city']
    pnumber = request.json['pnumber']
    isbn = request.json['isbn']

    lender.Lender_ID = l_id
    lender.FirstName = lfName
    lender.LastName = llName
    lender.City = city
    lender.Email = email
    lender.PhoneNumber = pnumber
    lender.ISBN = isbn
    db.session.commit()

    return Lender_schema.jsonify(lender)


@app.route('/Lender/<l_id>', methods=['DELETE'])
def delete_Lender(l_id):
    # Delete Lender
    lender = Lender.query.get(l_id)
    db.session.delete(lender)
    db.session.commit()

    return Lender_schema.jsonify(lender)

# Run Server
if __name__ == "__main__":
    app.run(debug=True)