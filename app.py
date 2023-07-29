import argparse

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/generator')
def generator():

    return 'Hello World!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flask Server')
    parser.add_argument('--bind', help='Binding IP Address', default='0.0.0.0')
    parser.add_argument('--port', help='Binding Port', default='8080')
    parser.add_argument('--debug', help='Binding Port', default='True')
    args = parser.parse_args()

    app.run(host=args.bind, port=args.port, debug=args.debug)
