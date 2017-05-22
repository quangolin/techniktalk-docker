import os
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.getenv('MONGODB_HOST', 'localhost'),
    27017)

db = client.szdb

@app.route('/')
def index():
    return jsonify({'message':'Hallo ' + os.getenv('USER', 'Fabi') + ' :)'})

@app.route('/appinfo')
def getAppInfo():
    info = {
        'MONGODB_HOST': os.getenv('MONGODB_HOST', 'localhost'),
        'USER': os.getenv('USER', 'Fabi')
    }
    return jsonify(info)

@app.route('/articles')
def getItems():
    articles = []
    for article in db.articles.find():
        article['_id'] = str(article['_id'])
        articles.append(article)
    return jsonify(articles)

@app.route('/addarticle', methods=['POST'])
def addItem():
    article = {
        'title': request.form['title'],
        'abstract': request.form['abstract'],
        'content': request.form['content']
    }
    db.articles.insert_one(article)
    article['_id'] = str(article['_id'])
    return jsonify(article)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
