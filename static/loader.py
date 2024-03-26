import onnx
import onnxruntime as ort
from torchvision import transforms
from PIL import Image
import io


class LoadModel:
    def __init__(self, model_path, name_input, name_output, class_names):
        self.model = onnx.load(model_path)
        self.sess = ort.InferenceSession(model_path)
        self.classes = class_names
        self.output_name = name_output
        self.input_name = name_input

    def predict(self, img):
        output = self.sess.run(None, {self.input_name: img.numpy()})
        predicted = self.classes[output[0][0].argmax(0)]
        return predicted


def transform_image(image):
    transform = transforms.Compose([transforms.Resize((224, 224), antialias=True),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,))])

    img = Image.open(io.BytesIO(image))

    return transform(img).unsqueeze(0)
