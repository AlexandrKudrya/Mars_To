from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html', title='Заготовка')

@app.route("/training/<prof>")
def training(prof):
    return render_template('training.html', title='Заготовка', prof=prof)

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')