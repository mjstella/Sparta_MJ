from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

# from flask import Flask, render_template, jsonify, request
# app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template("index.html")

# @app.route('/test', methods=["GET"])
# def test_get():
#     title_receive = request.args.get("title_give")
#     #title_give를 받지 못했을 때 실행할 것
#     print(title_receive)
#     return jsonify({'result': 'success', 'msg':'이 요청은 GET!'})
#     #출력 이외의 다른 실행 가능

# # @app.route('/mypage')
# # def mypage():  
# #    return 'This is My Page!'

# if __name__ == '__main__':  
#    app.run('0.0.0.0',port=5000,debug=True)

#    # 로컬에서 5000포트에다가 저걸 다 연결해
#    # 기본 페이지는 this is home 이야

# # localhost:5000 브라우저에서 치면 This is Home! 이 뜬다
# # http://localhost:5000/mypage 이렇게 하면 URL이 나눠진 거!