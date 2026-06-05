from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': '欢迎使用 Python 示例服务',
        'endpoints': [
            '/',
            '/examples/basic',
            '/examples/echo?text=hello',
            '/examples/sum',
            '/examples/user/<username>',
            '/health'
        ]
    })

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'python-service'})

@app.route('/examples/basic')
def basic_example():
    return jsonify({
        'description': '这是一个基础示例，返回简单的 JSON 数据',
        'data': {
            'language': 'Python',
            'framework': 'Flask',
            'usage': '示例服务'
        }
    })

@app.route('/examples/echo')
def echo_example():
    text = request.args.get('text', '您好')
    return jsonify({
        'description': '这是一个 echo 示例，展示查询参数读取',
        'input': text,
        'output': f'你发送的内容是: {text}'
    })

@app.route('/examples/sum', methods=['POST'])
def sum_example():
    payload = request.get_json(silent=True) or {}
    numbers = payload.get('numbers')
    if not isinstance(numbers, list):
        return jsonify({
            'error': '请在请求体中提供 numbers 列表，例如 {"numbers": [1,2,3]}'
        }), 400

    total = sum(n for n in numbers if isinstance(n, (int, float)))
    return jsonify({
        'description': '这是一个 POST 示例，计算 numbers 列表的和',
        'numbers': numbers,
        'sum': total
    })

@app.route('/examples/user/<username>')
def user_example(username):
    return jsonify({
        'description': '这是一个路径参数示例',
        'user': {
            'username': username,
            'welcome': f'欢迎, {username}!'
        }
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '未找到该路径，请检查 URL 是否正确'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
