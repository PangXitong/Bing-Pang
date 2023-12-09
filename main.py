import requests
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def proxy():
    url = 'https://www.bing.com' + request.full_path
    headers = {'User-Agent': request.headers.get('User-Agent')}
    response = requests.get(url, headers=headers)
    
    # 创建响应对象并设置转发的数据
    resp = make_response(response.content)
    
    # 将bing.com的响应头复制到转发的响应中
    for key, value in response.headers.items():
        resp.headers[key] = value
    
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)