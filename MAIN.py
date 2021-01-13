from flask import Flask, render_template
app = Flask (__name__)

l = ['1','2','3','4','5']
@app.route('/')
# def index():
#     return render_template("index.html")
# @app.route('/about') 
def about():
    return render_template("about.html", items = l)

if __name__=="__main__":
    app.run()