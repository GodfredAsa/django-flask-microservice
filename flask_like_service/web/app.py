import requests as requests
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@flask_db/"
CORS(app)
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer, primary_key=True)
    # unique constraint ensure the combine product and user id are unique
    UniqueConstraint("user_id", "product_id", "user_product_unique")


@app.route('/')
def index():
    return "Hello World"


@app.route('/api/products/<int:id>/likes', methods=['POST'])
def likes(id):
    req = requests.get("http://docker.for.mac.Localhost:8000/api/user")
    # send event here
    print(req)

    publish("product_liked", req)
    print(req)
    return jsonify(req.json())


@app.route('/api/user', methods=['GET'])
def get_user_id():
    req = requests.get("http://docker.for.mac.Localhost:8000/api/user")
    # send event here
    return jsonify(req.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
