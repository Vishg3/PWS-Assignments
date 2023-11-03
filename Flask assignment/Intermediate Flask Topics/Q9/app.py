from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

movies = [
    {"id": 1, "title": "Movie 1", "director": "Director 1"},
    {"id": 2, "title": "Movie 2", "director": "Director 2"},
]

# Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

# Get a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        return jsonify(book)
    return "Book not found", 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if 'title' in data and 'author' in data:
        new_id = max([book['id'] for book in books]) + 1
        new_book = {"id": new_id, "title": data['title'], "author": data['author']}
        books.append(new_book)
        return jsonify(new_book), 201
    return "Invalid request", 400

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None and 'title' in data and 'author' in data:
        book['title'] = data['title']
        book['author'] = data['author']
        return jsonify(book)
    return "Book not found or invalid request", 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        books.remove(book)
        return "Book deleted"
    return "Book not found", 404

# Similarly, create routes for CRUD operations on movies

if __name__ == '__main__':
    app.run(debug=True)
