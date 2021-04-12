from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route('/about')
def about():
    return render_template ('about.html', title= 'About')

if __name__ == '__main__':
    app.run(debug=True)