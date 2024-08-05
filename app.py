# importing the flask module
from flask import Flask , render_template

# object of flask class
app = Flask(__name__)


# First route : the Index 
@app.route('/')
def index():
    return render_template("index.html")


# route for shopping
@app.route('/shop')
def shop():
    return render_template("shop.html")


# route for customization
@app.route('/customize')
def customize():
    return render_template("customize.html")

# route for contact page 
@app.route('/contact')
def contact():
    return render_template("contact.html")

# route for about us page
@app.route('/about')
def about():
    return render_template("about.html")

# route for about us page
@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)