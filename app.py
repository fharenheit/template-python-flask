import argparse
import os
import traceback
import yaml

from flask import Flask, request, Response
from loguru import logger

from generator import generator

app = Flask(__name__)

print(os.environ)

def init(config):
    configurationPath = os.environ.get("CONF_PATH", config)
    with open(configurationPath) as f:
        conf = yaml.safe_load(f)

    logger.add(conf['app']['logging-path'])

    logger.info("Now starting Flask Server...")
    logger.info("Configuration Path : {}".format(configurationPath))


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


if __name__.endswith("app"):
    init('application.yml')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flask Server')
    parser.add_argument('--config', help='Configuration File Path', default='application.yml')
    parser.add_argument('--debug', help='Debug Mode', default='True')
    args = parser.parse_args()

    init(args.config)

    app.run(host=args.bind, port=args.port, debug=args.debug)
