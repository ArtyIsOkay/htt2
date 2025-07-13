from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Привет, Flask работает!</h1>"

@app.route("/api/hello")
def hello():
    return {"message": "Hello from Flask API!"}

if __name__ == "__main__":
    app.run(port=8000)  # Запуск на порту 8000