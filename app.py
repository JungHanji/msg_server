from flask import Flask, request, json
from tools import *
from MyDB import *

app = Flask(__name__)

CLIENTS_FILE = "server_data/clients.mdb"
MSGS_FILE = "server_data/msgs.txt"

if(not isExist(CLIENTS_FILE)): createFile(CLIENTS_FILE)
if(not isExist(MSGS_FILE)): createFile(MSGS_FILE)

@app.route('/', methods=['GET', 'POST'])
def main():
    return 'Nothing here'

@app.route('/reg', methods=["POST"])
def regClient():
    jdict = getDictFromJSON(getlJSTRING(request))
    print(jdict)
    name = jdict["name"]
    if(not isLineInFile(CLIENTS_FILE, name)):
        addToFile(CLIENTS_FILE, name)
        return "Client added"
    else:
        return "Client alredy exist"

@app.route("/newMsg", methods=["POST"])
def newMsg():
    jdict = getDictFromJSON(getlJSTRING(request))
    
    name = jdict["name"]
    msg = jdict["msg"]
    if(not isLineInFile(CLIENTS_FILE, name)):
        return "Clients isn`t exist"
    else:
        addToFile(MSGS_FILE, f"{name} {msg}")
        return f"[Messege posted] : {msg}"


@app.route("/getMsg", methods=["POST"])
def getMsg():
    jdict = getDictFromJSON(getlJSTRING(request))
    name = jdict["name"]
    if(len(readFileLines(MSGS_FILE))>0):
        return parseDLinesWhile(MSGS_FILE, name)
    else:
        return "No messeges to get"

@app.route("/post", methods=["POST"])
def postTest():
	jsonstring = getDictFromJSON(getlJSTRING(request))
	print("[POST] posted" + str(jsonstring))
	return "[POST] posted: " + str(jsonstring)