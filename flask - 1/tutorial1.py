from flask import Flask
app = Flask (__name__)

@app.route("/")  
def hello():
    return "hello divyansh!"

app.run(debug=True)
