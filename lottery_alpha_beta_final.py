from flask import Flask, render_template, request
import random
import pandas as pd
import os

app = Flask(__name__)
data_file = os.path.join(os.path.dirname(__file__), 'lottery_results.xlsx')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        participant_id = request.form.get('participant_id')
        if not participant_id:
            return render_template('index.html', error='IDを入力してください。')

        alpha = random.randint(1, 7)
        beta = random.randint(1, 12)

        if os.path.exists(data_file):
            df = pd.read_excel(data_file)
        else:
            df = pd.DataFrame(columns=['id', 'alpha', 'beta'])

        df = df[df['id'] != participant_id]  # 同じIDの上書き防止
        df.loc[len(df)] = [participant_id, alpha, beta]
        df.to_excel(data_file, index=False)

        return render_template('result.html', alpha=alpha, beta=beta, participant_id=participant_id)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
