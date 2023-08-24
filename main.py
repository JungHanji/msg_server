from flask import Flask, request
from threading import Thread

app = Flask(__name__)

mainString = "Hello, world!"

@app.route('/')
def main():
    return mainString

@app.route('/post', methods=["POST"])
def postTest():
	global mainString
	mainString = request.form.get("data")
	return "ok"

def run():
	app.run(host='0.0.0.0', port=900)


def keep_alive():
	t = Thread(target=run)
	t.start()


if __name__ == '__main__':
	keep_alive()