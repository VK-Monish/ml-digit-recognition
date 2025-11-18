# 🚀 MNIST Digit Classifier Web App
A simple and interactive **web application** that predicts handwritten digits (0–9) using a **PyTorch MNIST model**.  
Upload any digit image and the app instantly tells you the predicted number.

---

## 🧠 About the Project
This project includes:

- A **trained PyTorch CNN model** (`model_state.pt`)
- A **Flask web server** (`app.py`)
- A clean **HTML/CSS frontend**
- Image preprocessing and digit prediction
- Fully working local ML deployment

This is a great starter project for understanding **machine learning + web deployment**.

---

## 📂 Project Structure

```
mnist_website/
│── app.py
│── model.py
│── model_state.pt
│── static/
│     └── style.css
│── templates/
      └── index.html
│── README.md
```

---

## 🛠️ Tech Stack
- **Python**
- **Flask (Backend)**
- **PyTorch (Model Inference)**
- **HTML / CSS (Frontend)**

---

## 🚀 How It Works
1. User uploads an image  
2. Backend converts the image to 28×28 grayscale  
3. Image passed to trained CNN model  
4. Model predicts the digit (0–9)  
5. Website displays the output  

---

## ▶️ Run the App Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

### 2. Install Dependencies
```bash
pip install flask torch torchvision pillow
```

### 3. Run the Web App
```bash
python3 app.py
```

Then open your browser:

```
http://127.0.0.1:5000/
```

Upload an image → get prediction.

---

## 🧪 Model Used
- Dataset: **MNIST**
- Architecture: 3 convolution layers + linear layer  
- Trained for **10 epochs**
- Saved as **model_state.pt**

---

## 🖼️ Screenshot
(Add your own screenshot here)

```
[Upload]

[Predict Button]

Predicted Digit: 7
```

---

## 🌟 Future Improvements
- Deploy online (Render / Railway / Vercel)
- Add webcam digit input
- Add drawing canvas to write digits
- Convert to ONNX for mobile apps
- Add confidence scores & heatmaps
- Improve UI using Tailwind or Bootstrap

---

## 🤝 Contributing
Pull requests and improvements are welcome!

---

## 📜 License
This project is open-source under the **MIT License**.
