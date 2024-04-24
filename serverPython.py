from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_python', methods=['POST'])
def execute_python():
    python_code = request.json['code']
    # ここでpython_codeを実行して結果を取得する
    result = execute_python_code(python_code)
    return jsonify({'result': result})

def execute_python_code(code):
    # ここにPythonコードを実行するロジックを記述する
    # 例えば、exec()を使用してコードを実行するか、外部プログラムを呼び出すなど
    # 実際のコードの安全性に注意してください
    result = eval(code)  # 例: eval()を使ってPythonコードを実行する
    return result

if __name__ == '__main__':
    app.run(debug=True)
