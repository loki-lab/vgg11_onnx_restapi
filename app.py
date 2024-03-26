from flask import Flask, request, jsonify
from static.loader import LoadModel, transform_image

app = Flask(__name__)

classes = ("cat", "dog")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/inference', methods=['POST'])
def inference():

    model = LoadModel(model_path="static/models/vgg_classification_model.onnx",
                      name_output="modelOutput",
                      name_input="modelInput",
                      class_names=classes)

    if request.method == 'POST':
        image = request.files['image']
        image = image.read()
        image = transform_image(image)
        output = model.predict(image)

        return jsonify({"result": str(output)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
