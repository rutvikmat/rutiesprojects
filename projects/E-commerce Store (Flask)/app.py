from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'a_very_secret_key'

# In-memory product database
products = {
    '1': {'name': 'Laptop', 'price': 1200, 'image': 'https://via.placeholder.com/150'},
    '2': {'name': 'Smartphone', 'price': 800, 'image': 'https://via.placeholder.com/150'},
    '3': {'name': 'Headphones', 'price': 150, 'image': 'https://via.placeholder.com/150'}
}


@app.route('/')
def index():
    return render_template('products.html', products=products)


@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}

    # Add item to cart or increment its quantity
    cart = session['cart']
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart  # Save changes to session

    flash(f"{products[product_id]['name']} added to cart!", 'success')
    return redirect(url_for('index'))


@app.route('/cart')
def view_cart():
    cart_items = {}
    total_price = 0
    if 'cart' in session:
        for product_id, quantity in session['cart'].items():
            product = products.get(product_id)
            if product:
                total = product['price'] * quantity
                cart_items[product_id] = {
                    'name': product['name'],
                    'price': product['price'],
                    'quantity': quantity,
                    'total': total
                }
                total_price += total
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)


@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    flash('Cart cleared!', 'info')
    return redirect(url_for('view_cart'))


if __name__ == '__main__':
    app.run(debug=True)