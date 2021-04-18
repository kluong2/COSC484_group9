from datetime import datetime
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    # ema = db.Column(db.String(120),unique = True, nullable = False)

    email = db.Column(db.String(120),unique = True, nullable = False)
    image_file = db.Column(db.String(20),nullable = False, default = 'default.jpg')
    username = db.Column(db.String(20),unique = True, nullable = False)
    password = db.Column(db.String(60),nullable = False)
    posts = db.relationship('Post',backref = 'author', lazy = True)
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

def __repr__(self):
        return f"Post('{self.title}','{self.date_pasted}')"



posts= [
    {
        'author' : 'Henok Assefa',
        'title' : 'cosc 484',
        'content': 'chapter one',
        'date_posted': 'April 11, 2021'
    },
    {
        'author' : 'Abel',
        'title' : 'cosc 484',
        'content': 'chapter two',
        'date_posted': 'April 11, 2021'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html', posts = posts)

@app.route('/login')
def login():
    return render_template ('login.html', posts = posts)

@app.route('/about')
def about():
    return render_template ('about.html', title= 'About')

@app.route('/contactus')
def contactus():
    return render_template ('contact_us.html', title= 'About')

@app.route('/signup')
def signup():
    return render_template ('sign_up.html', posts = posts)

@app.route('/upload')
def upload():
    return render_template ('upload.html', title= 'About')

if __name__ == '__main__':
    app.run(debug=True)
    