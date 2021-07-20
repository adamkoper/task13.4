from flask import Flask, request, render_template, redirect, url_for, abort

from forms import BookForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "bububu"


@app.route("/api/v1.0/library/", methods=["GET"])
def books_list():
    form = BookForm()
    error = ""
    return render_template("books.html", form=form, books=books.all(), error=error)


@app.route("/api/v1.0/library/", methods=["POST"])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        books.create(form.data)
    return redirect(url_for('books_list'))


@app.route("/api/v1.0/book/<int:book_id>/", methods=["GET"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = BookForm(data=book)
    return render_template("book.html", form=form, book_id=book_id)


@app.route("/api/v1.0/book/<int:book_id>/", methods=["POST"])
def book_update(book_id):
    book = books.get(book_id - 1)
    form = BookForm(data=book)
    if form.validate_on_submit():
        books.update(book_id - 1, form.data)
    return redirect(url_for('books_list'))


if __name__ == "__main__":
    app.run(debug=True)
