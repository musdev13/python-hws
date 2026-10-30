from flask import Flask, render_template, abort
from models.product_model import ProductModel
from product import Product

app = Flask(__name__)
product_model = ProductModel()

@app.route('/')
def index():
    products = product_model.get_all_products()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = product_model.get_product_by_id(product_id)
    if product is None:
        abort(404)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
