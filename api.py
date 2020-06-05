from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/test')
def test_app():
    return "testing"

@app.route('/get-json-response')
def test_json_response():
    test={
        'name':'sample','text':'hello'
    }
    return jsonify(test)

@app.route('/post-url',methods=['POST'])
def post_url():
    # test={
    #     'name':'sample','text':'hello'
    # }
    return "test-post-url"

@app.route('/post-json-response',methods=['POST'])
def post_json_resp():
    test={
        'name':'sample','text':'hello'
    }
    return jsonify(test)

@app.route('/get-with-params/<id>/<name>',methods=['GET'])
def post_get_param(id,name):
    test={
        'id':id,'name':name
    }
    return jsonify(test)

@app.route('/post-with-request',methods=['POST'])
def post_post_request():
    data=eval(request.data)
    test={
        'id':data['id'],
        'name':data['name']
    }
    return jsonify(test)

@app.route('/get-post-example',methods=['POST','GET'])
def get_post_ex():
    return "post-get-example"


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5005)