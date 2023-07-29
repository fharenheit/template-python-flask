import argparse
import traceback

from flask import Flask, request, Response
from generator import generator

app = Flask(__name__)


@app.route('/api/generator', methods=['POST'])
def generate():
    json = request.get_json()
    try:
        return Response(generator.generate(json), status=200, mimetype='application/json')
    except Exception as e:
        returnValue = {
            'message': traceback.format_exc()
        }
        return Response(returnValue, status=500, mimetype='application/json')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flask Server')
    parser.add_argument('--bind', help='Binding IP Address', default='0.0.0.0')
    parser.add_argument('--port', help='Binding Port', default='8080')
    parser.add_argument('--debug', help='Debug Mode', default='True')
    args = parser.parse_args()

    app.run(host=args.bind, port=args.port, debug=args.debug)
