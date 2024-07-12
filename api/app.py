from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurer la connexion à la base de données MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://CloudSA59a2ae44:ijeBbQ&Ays38GbRM@server1107.mysql.database.azure.com/books_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Définir le modèle Book pour représenter la table books
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))
    price = db.Column(db.Float)
    availability = db.Column(db.String(50))
    stars = db.Column(db.Integer)
    category = db.Column(db.String(100))

# Route pour récupérer les livres selon le genre et le nombre voulu
@app.route('/books', methods=['GET'])
def get_books():
    category = request.args.get('category')
    limit = request.args.get('limit', default=10, type=int)


    print(f"Received request for genre: {category} with limit: {limit}")  # Debug

    # Requête pour obtenir les livres
    books = Book.query.filter_by(category=category).limit(limit).all()

    # Convertir les résultats en JSON
    books_list = []
    for book in books:
        books_list.append({
            'title': book.title,
            'link': book.link,
            'price': book.price,
            'availability': book.availability,
            'stars': book.stars,
            'category': book.category
        })

    return jsonify(books_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
