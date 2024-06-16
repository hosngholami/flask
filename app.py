from flask import Flask
from flask import request



app = Flask(__name__)

@app.route("/home", methods=['GET', 'POST'])
def hello():
    return "Hello, World!"


@app.route("/dashbord", methods=["GET", "POST"])
def dashbord():

    name = request.args.get('name')
    family = request.args.get("family")
    
    return f"{name}  {family}"



if __name__ == "__main__":
    app.run(debug=True)