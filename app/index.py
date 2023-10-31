from flask import Flask , render_template,request
import dao
app = Flask(__name__)
@app.route("/")

def index():
    key =request.args.get("key")

    product =dao.get_produce(key)
    cates =dao.get_categories()
    return render_template('index.html', categories=cates, produce=product)
if __name__== "__main__":
    app.run(debug=True)