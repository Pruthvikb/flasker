from flask import Flask, render_template

#create flask instance
app = Flask(__name__)

#create a route
@app.route('/')
def index():
    stuff = "This is <strong> bold </strong> Text"
    favorite_pizza = ['pepperoni','4cheese','sausage','mushroom']
    return render_template("index.html", stuff = stuff, favorite_pizza=favorite_pizza)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


# create custom error pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500