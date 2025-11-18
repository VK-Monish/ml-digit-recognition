from flask import Flask, render_template, request
import torch
from torchvision.transforms import ToTensor
from PIL import Image
from model import ImageClassifier
import os

app = Flask(__name__)

# Load model
model = ImageClassifier()
model.load_state_dict(torch.load("model_state.pt", map_location="cpu"))
model.eval()

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    filename = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            img = Image.open(file).convert("L").resize((28, 28))
            img_tensor = ToTensor()(img).unsqueeze(0)

            with torch.no_grad():
                out = model(img_tensor)
                prediction = torch.argmax(out).item()

            file.save("static/uploaded.png")
            filename = "uploaded.png"

    return render_template("index.html", prediction=prediction, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)

