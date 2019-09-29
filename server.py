from flask import Flask, request
from convert import dcm_to_png
from waitress import serve


app = Flask(__name__)


@app.route('/convert', methods=['GET'])
def convert():
    path = request.args.get("path")
    file_name = request.args.get("file_name")
    return dcm_to_png(path, file_name)


if __name__ == '__main__':
    serve(app, listen='*:18080')
