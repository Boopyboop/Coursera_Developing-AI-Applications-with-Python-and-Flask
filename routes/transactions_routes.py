from flask import Blueprint, render_template, request, redirect, url_for

# Blueprint definition
transactions_bp = Blueprint('transactions', __name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Home page with list of transactions
@transactions_bp.route('/')
def render_index_page():
    return render_template('transactions.html', transactions=transactions)

# Form to add a transaction
@transactions_bp.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for('transactions.render_index_page'))  # Use blueprint name
    return render_template("form.html")

@transactions_bp.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    """Edit an existing transaction."""
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break

        # Redirect to homepage (where transactions are listed)
        return redirect(url_for("transactions.render_index_page"))

    # GET: Display the form for editing
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

    return {"message": "Transaction not found"}, 404

# routes/transactions_routes.py

@transactions_bp.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    """Delete an existing transaction."""
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    return redirect(url_for("transactions.render_index_page"))
