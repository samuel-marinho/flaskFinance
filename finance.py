from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route("/expenses")
def expenses_page():
    items = [
        {'id': 1, 'expense': 'Shoes', 'category': 'Personal', 'price': 200},
        {'id': 2, 'expense': 'T-shirt', 'category': 'Personal', 'price': 35},
        {'id': 3, 'expense': 'SSD', 'category': 'Personal', 'price': 200},
        {'id': 4, 'expense': 'Pizza', 'category': 'Market', 'price': 50},
        {'id': 5, 'expense': 'Market', 'category': 'Market', 'price': 200},
    ]
    return render_template('expenses.html', items=items)

app.run(debug=True)