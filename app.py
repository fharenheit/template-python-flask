import argparse
import os
import traceback

from flask import Flask, request, Response
from loguru import logger

from generator import generator

loggingPath = os.environ.get("LOGGING_PATH", ".")

logger.add(loggingPath + "/service_{time}.log")

app = Flask(__name__)

logger.info("Now starting Flask Server")


@app.route('/api/generator', methods=['POST'])
def generate():
    json = request.get_json()
    try:
        return Response(generator.generate(json), status=200, mimetype='plain/text')
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
