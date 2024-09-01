from flask import Flask ,render_template

app = Flask (__name__)

@app.route ("/")
def home():
    return render_template("index.html")

@app.route ("/ssr")
def ssr():
    return "SSR Sir-\nThere is no need to made like that such notes. Because I have written by all topics properly. So, just read it. Therefore your marks will be increases."


if __name__ =="__main__":
    app.run(debug=False)