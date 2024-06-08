from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

#Modelagem
#Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
#Definição de rota para requisitar cadastro
@app.route('/api/products/add')
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data['name'], price=data['price'], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"})
    
#Definir uma rota raiz (paǵina inicial) e a função que será requisitada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)