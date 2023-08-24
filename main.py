from flask import Flask, request
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/post')
def postTest():
	return request.form.get("data")

def run():
	app.run(host='0.0.0.0', port=900)


def keep_alive():
	t = Thread(target=run)
	t.start()


if __name__ == '__main__':
	keep_alive()