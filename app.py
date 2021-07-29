from flask import Flask, render_template, jsonify, request
import json
from Config import data_label_link, full_labels, tuongquan_link
from models import predict_one_test, run_models
from data_preprocessing import create_pp_data_pics
app = Flask(__name__)


@app.route("/")
def main():
    create_pp_data_pics()
    return render_template("index.html")


@app.route('/dudoan', methods=['POST'])
def duDoan():
    data_req = []
    print(request.get_json())
    for label in full_labels:
        data_req.append(request.get_json()[label])
    model = data_req.pop()
    x = data_req
    y_pred = predict_one_test(x, model)
    print("predict:", y_pred)
    return str(y_pred[0])


@app.route('/getdata')
def getData():
    f = open(data_label_link)
    data = json.load(f)
    f.close()
    return jsonify(data)


@app.route('/gettuongquan')
def getTuongQuan():
    f = open(tuongquan_link)
    data = json.load(f)
    f.close()
    return jsonify(data)


if __name__ == "__main__":
    app.run()
