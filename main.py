from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def proxy():
    if request.method == 'OPTIONS':
        # 处理预检请求
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
        }
        return '', 200, headers
    else:
        # 转发请求并处理响应
        headers = {
            'Access-Control-Allow-Origin': '*'
        }
        try:
            response = requests.request(
                method=request.method,
                url='https://www.bing.com' + request.full_path,
                headers={k: v for k, v in request.headers if k != 'Host'},
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False
            )
            content_type = response.headers.get('content-type')
            return (response.content, response.status_code, {'Content-Type': content_type, 'Access-Control-Allow-Origin': '*'})
        except requests.exceptions.RequestException as e:
            return str(e), 500, headers

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
