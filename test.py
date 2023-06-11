from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fruit = request.form.get('fruit')  # 폼 데이터에서 'fruit' 값을 가져옵니다.

    return render_template('test.html', selected_fruit=fruit)

if __name__ == '__main__':
    app.run()