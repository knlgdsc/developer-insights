
from flask import Flask,render_template, jsonify
from src import images

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/engr350-project/api/graphs', methods=['GET'])
def get_all():
    return jsonify(images.get_all())


@app.route('/engr350-project/api/graphs<graph_name>', methods=['GET'])
def get(graph_name):
    return jsonify(images.get_one(graph_name))


@app.route('/engr350-project/api/graphs', methods=['POST'])
def post(graph_name, graph_url):
    return images.create(graph_name, graph_url)


@app.route('/engr350-project/api/graphs<graph_name>', methods=['DELETE'])
def delete(graph_name):
    return images.delete(graph_name)


@app.route('/engr350-project/api/graphs<graph_name>', methods=['PUT'])
def put(graph_name, up_graph_name, graph_url):
    return images.update(graph_name, up_graph_name, graph_url)


if __name__ == "__main__":
    app.run(port=4555, debug=False)


