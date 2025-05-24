from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD Pipeline Working! This is Test to Trigger.🚀" 

if __name__ == '__main__':
    app.run()
