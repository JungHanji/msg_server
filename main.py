from flask import Flask, request
from threading import Thread

app = Flask(__name__)

mainString = "Hello, world!"

@app.route('/')
def main():
    return mainString

@app.route('/post', methods=["GET", "POST"])
def postTest():
	print("[POST] posted" + request.get_data())
	return "ok"

def run():
	app.run(host='0.0.0.0', port=900)


def keep_alive():
	t = Thread(target=run)
	t.start()


if __name__ == '__main__':
	run()
	#keep_alive()