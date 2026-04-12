from flask import Flask, render_template

app = Flask(__name__)

# 首頁 (個人簡介大廳)
@app.route('/')
def home():
    return render_template('index.html')

# 分頁 1：職涯測驗結果
@app.route('/test')
def test():
    return render_template('test.html')

# 分頁 2：MIS 工作分析
@app.route('/job')
def job():
    return render_template('job.html')

# 分頁 3：求職履歷與未來
@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)