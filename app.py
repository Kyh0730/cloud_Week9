from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/subject')
def subject():
    return render_template('subject.html')

@app.route('/rationale')
def rationale():
    return render_template('rationale.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/environment')
def environment():
    return render_template('environment.html')

@app.route('/team')
def team():
    return render_template('team.html')

# API routes
@app.route('/api/<page_name>')
def api(page_name):
    # JSON 파일에서 해당 페이지 데이터 읽기
    import json, os
    file_path = f"data/{page_name}.json"
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "No data found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
