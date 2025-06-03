from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # ID 50〜60 までのデモデータを生成（ランダムに毎回変化）
    data = []
    for i in range(50, 61):
        alpha = random.randint(1, 7)
        beta = random.randint(1, 12)
        data.append({'id': i, 'alpha': alpha, 'beta': beta})
    return render_template("index_demo.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
