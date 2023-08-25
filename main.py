from flask import Flask, request, json
from threading import Thread

app = Flask(__name__)

mainString = "Hello, world!"

@app.route('/')
def main():
    return mainString

@app.route('/post', methods=["GET", "POST"])
def postTest():
	jsonstring = str(request.form.to_dict().items[0])
	print("[POST] posted" + jsonstring)
	return "[POST] posted: " + jsonstring

def run():
	app.run(host='0.0.0.0', port=900)


def keep_alive():
	t = Thread(target=run)
	t.start()


if __name__ == '__main__':
	run()
	#keep_alive()