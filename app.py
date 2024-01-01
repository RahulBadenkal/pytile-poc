import json
import sys
import traceback
from flask import Flask, request, jsonify

from main import get_tiles


app = Flask(__name__)


def get_exception_traceback(exception):
    if sys.version_info >= (3, 10):
        tb = ''.join(traceback.format_exception(exception))
        return tb
    else:
        tb = ''.join(traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__))
        return tb


@app.errorhandler(Exception)
def handle_exception(e):
    res = {
        "status_code": 500,
        "error_message": str(e),
        # "traceback": get_exception_traceback(e)
    }
    print(json.dumps(res))
    return jsonify(res), 500


@app.route('/')
def hello_world():
    res = {"msg": "Hello World!"}
    print(json.dumps(res))
    return jsonify(res), 200


@app.route('/tiles', methods=['POST'])
async def tiles():
    # print("form:", request.form)
    # print("email:", request.form.get("email"))
    # print("password:", request.form.get("password"))

    email = request.form.get('email')
    password = request.form.get('password')

    tiles_data = await get_tiles(email, password)

    res = {
        "tiles": tiles_data
    }
    print(json.dumps(res))
    return jsonify(res), 200


if __name__ == '__main__':
    app.run(debug=True)

