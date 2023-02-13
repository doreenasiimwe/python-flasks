#importing modules
from flask import Flask,jsonify

#initializing the flask class
app = Flask(__name__)

#default route/decorator
@app.route('/')
def default():
    return "Welcome to articles home page"

#articles route/decorator
@app.route('/articles', methods = ['GET'])
def get_articles():
    articles = [
        {
        'id':1000,
        'title':'Love and pain',
        'body':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur venenatis est est, quis elementum mauris efficitur et. Cras massa diam, dapibus vel vestibulum nec, lacinia vitae velit. Vestibulum viverra laoreet ',
        'author':'Michael Jordans'
    },
    {
        'id':2000,
        'title':' Mental Health',
        'body':'mi, eget pharetra sem pretium vel. Nunc egestas felis id faucibus consequat. In malesuada tortor a risus aliquet elementum. Cras fringilla, turpis nec porta condimentum, ex felis sagittis risus, quis bibendum massa .',
        'author':'Adee Joyce'
    },
    {
        'id':3000,
        'title':'Psycology',
        'body':'tellus eget dui. Ut feugiat rutrum sem ac pharetra. Vestibulum mi mauris, placerat vel urna lobortis, elementum consequat nunc. Nunc ut leo in lacus ornare congue. Proin convallis urna gravida nulla ornare, sed consectetur ante vehicula. Proin nec congue risus. Nullam dictum eleifend ante a elementum.',
        'author':'Doreen Victory'
    },
    {
        'id':4000,
        'title':'The Future of AI in Education',
        'body':'Proin non odio turpis. Ut volutpat pretium magna, varius consectetur libero ultrices id. Etiam venenatis, enim vel interdum vehicula, eros risus aliquet dolor, a molestie ligula risus et ligula. Cras egestas imperdiet erat ac volutpat. Donec vel consequat velit, a tristique mi. Nam dapibus, nibh in mattis eleifend, justo ante mattis velit, vitae eleifend libero nulla sit amet purus. Fusce faucibus felis in purus congue varius. Integer nec torto.',
        'author':'Sarah Atim'
    }
    
    ]
    return jsonify(articles)

if __name__=='__main__':
    app.run(debug=True)