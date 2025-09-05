from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory "database"
expenses = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expenses.append({
            'description': description,
            'amount': amount,
            'category': category,
            'date': date
        })
        return redirect(url_for('index'))

    total_expense = sum(item['amount'] for item in expenses)
    return render_template('index.html', expenses=expenses, total=total_expense)


if __name__ == '__main__':
    app.run(debug=True)