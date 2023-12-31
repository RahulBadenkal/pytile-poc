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
    return jsonify({
        "status_code": 500,
        "error_message": str(e),
        "traceback": get_exception_traceback(e)
    }), 500


@app.route('/')
def hello_world():
    return {"msg": "Hello World!"}


@app.route('/tiles', methods=['POST'])
async def tiles():
    email = request.form.get('email')
    password = request.form.get('password')

    tiles_data = await get_tiles(email, password)

    return jsonify({
        "tiles": tiles_data
    })


if __name__ == '__main__':
    app.run(debug=True)

    # Sample call
    # curl -X POST http://127.0.0.1:5000/tiles -d "email=rahulbadenkal@gmail.com&password=rahul@4900"
