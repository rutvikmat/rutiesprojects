from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import base64
from PIL import Image
import io

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('mnist_model.pkl')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the image data from the request
    image_data = request.json['image']
    # Decode the base64 string
    image_b64 = base64.b64decode(image_data.split(',')[1])

    # Open the image and convert to grayscale
    img = Image.open(io.BytesIO(image_b64)).convert('L')

    # Resize to 28x28 pixels (as required by MNIST)
    img = img.resize((28, 28))

    # Convert image to numpy array and invert colors
    img_array = np.array(img)
    img_array = 255 - img_array

    # Reshape and normalize the array for the model
    img_array = img_array.flatten().reshape(1, -1) / 255.0

    # Make a prediction
    prediction = model.predict(img_array)

    return jsonify({'prediction': str(prediction[0])})


if __name__ == '__main__':
    app.run(debug=True)