from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return '''
            <html>
                <body>
                    <h1>Search Engine Proxy</h1>
                    <form method="post" action="/">
                        <input type="text" name="q" placeholder="Search...">
                        <button type="submit">Search</button>
                    </form>
                </body>
            </html>
        '''
    else:
        # 从表单获取查询字符串
        query = request.form.get('q')

        # 使用Google搜索
        params = {
            'q': query,
            'num': 10
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        try:
            response = requests.get('https://www.google.com/search', params=params, headers=headers)
            content_type = response.headers.get('content-type')
            return (response.content, response.status_code, {'Content-Type': content_type})
        except requests.exceptions.RequestException as e:
            return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
