from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory "database"
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]
next_id = 3

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    global next_id
    title = request.form['title']
    author = request.form['author']
    books.append({'id': next_id, 'title': title, 'author': author})
    next_id += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)