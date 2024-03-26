docker build . -t vgg11_cat_and_dog_rest_onnx_api
docker run --rm -p 8080:5003 --name cat_and_dog_ai_onnx  vgg11_cat_and_dog_rest_onnx_api