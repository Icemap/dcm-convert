from flask import Flask, request
from convert import dcm_to_png
from waitress import serve


app = Flask(__name__)


@app.route('/convert', methods=['GET'])
def convert():
    path = request.args.get("path")
    file_name = request.args.get("file_name")
    gray = request.args.get("gray")
    return dcm_to_png(path, file_name, gray)


if __name__ == '__main__':
    serve(app, listen='*:18080')
