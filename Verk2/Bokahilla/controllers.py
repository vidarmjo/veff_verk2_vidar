from Bokahilla import app
from Bokahilla import bok as bok
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    booklist = bok.booklist

    return render_template('bokalisti.html', booklist=booklist)

@app.route("/book/<isbn>")
def book(isbn=None):

    matched = isbn

    return render_template('book.html', matched=matched)