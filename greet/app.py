from flask import Flask
app = Flask(__name__)

@app.route("/welcome")
def hello():
    return """
        <body>
        <h1>Welcome!</h1>
        </body>
    """
@app.route("/welcome/home")
def home():
    return """
        <body>
        <h1>Welcome home</h1>
        </body>
    """
@app.route("/welcome/back")
def back():
    return """
        <body>
        <h1>Welcome back</h1>
        </body>
    """

if __name__ == '__main__':
    app.run()
