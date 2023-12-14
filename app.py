from flask import Flask,render_template,request
import model

app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello_world():
    return render_template("index.html")


@app.route('/',methods=['POST'])
def predict():
    cond = request.form['user_input']
    prediction=model.recommend_drug(cond)
    return render_template('index.html', output=prediction)


if __name__ == '__main__':
    app.run(debug=True)