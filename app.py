from flask import Flask, render_template

app = Flask(__name__)

menu = ['О сайте', 'О авторе', 'Пример страницы']

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', title='Flask first', menu = menu)


if __name__ == '__main__':
    app.run(debug=True)
