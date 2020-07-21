from flask import Flask, render_template, url_for, request

# in order to use the app, you must create an instance of the app 
app = Flask(__name__)
# synatax to create flask instance 

#syntax for decorators 
# create a method to display on the homepage/default page 

# @app.route("/") # define the page where the informatuon is being displayed (route of the page)

# def index_page():
#     return "<h1>Welcome to Flask MVC project</h1>"

# the index_page method will be called at the endpoint (where it is being displayed)

# syntax to run app 

@app.route("/")

def welcome_user():
    return render_template("base.html")


@app.route("/logging/")

def welcome_user():
    return render_template("index.html")
# importing a html file from using render_template - include the name of the file in the brackets 
if __name__ == "__main__":
    app.run(debug=True)