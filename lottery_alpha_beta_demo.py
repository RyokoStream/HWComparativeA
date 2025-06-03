from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# グローバル変数として被験者データを保持
participant_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    participant_data.append(data)
    
    if len(participant_data) >= 30:
        return jsonify({'message': '被験者数が上限（30名）に達しました。'})
    
    return jsonify({'message': f"データを受け取りました（現在 {len(participant_data)} 人）"})

@app.route('/save', methods=['POST'])
def save():
    if not participant_data:
        return jsonify({'success': False, 'message': '保存するデータがありません。'})
    
    df = pd.DataFrame(participant_data)
    save_path = os.path.join(os.path.dirname(__file__), 'lottery_data.xlsx')
    df.to_excel(save_path, index=False)
    
    return jsonify({'success': True, 'message': 'Excelファイルを保存しました。'})

if __name__ == '__main__':
    app.run(debug=True)
