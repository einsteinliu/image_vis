from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    # Main page
    return 'Index Page'


@app.route('/change')
def hello():
    # When "http://ip:port is clicked, this function will be called
    # Create a empty file "message"
    with open("message", "w") as fp:
        fp.close()
    return 'Change Image'


if __name__ == "__main__":
    # Run a server
    ip = "192.168.0.101"
    port = 5005
    app.run(host=ip, port=port)
