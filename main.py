from flask import Flask, request, json
from convert import convert

app = Flask(__name__)


@app.route("/data", methods=["POST"])
def get_input():
    data = json.loads(request.data)
    return json.dumps(convert(data))


if __name__ == '__main__':
    app.run(debug=True)
