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

@app.route('/client', methods=["POST"])
def regClient():
    jdict = getDictFromJSON(getlJSTRING(request))
    name = jdict["name"]
    mtype = jdict["type"]
    if(mtype == "reg"):
        if(not isLineInFile(CLIENTS_FILE, name)):
            addToFile(CLIENTS_FILE, name)
            return "Client added"
        else:
            return "Client alredy exist"
    elif mtype == "del":
        if(isLineInFile(CLIENTS_FILE, name)):
            delFromFile(CLIENTS_FILE, name)
            return "Client deleted"
        else:
            return "Client isn`t exist"
    else:
        return f"Bad type: '{mtype}'"

@app.route("/newMsg", methods=["POST"])
def newMsg():
    jdict = getDictFromJSON(getlJSTRING(request))
    
    name = jdict["name"]
    msg = jdict["msg"]
    if(not isLineInFile(CLIENTS_FILE, name)):
        return "Client isn`t exist"
    else:
        addToFile(MSGS_FILE, f"{name}:{msg}")
        return f"[Messege posted] : {msg}"


@app.route("/getMsg", methods=["POST"])
def getMsg():
    jdict = getDictFromJSON(getlJSTRING(request))
    name = jdict["name"]
    if(len(readFileLines(MSGS_FILE))>0):
        sttr = str(parseDLinesWhile(MSGS_FILE, name, ':', True))
        if(sttr!="No such element"): return sttr[1:-1].replace('"',"").replace("'",'')
        else: return "No messeges to get"
    else:
        return "No messeges to get"

@app.route("/cmds", methods=["POST"])
def sysExec():
    jdict = getDictFromJSON(getlJSTRING(request))
    cmd = jdict["cmd"]
    
    if(cmd == "CLEAR_USERS"):
        clearFile(CLIENTS_FILE)
        return 'Successfully cleared clients'
    elif(cmd == "CLEAR_CHAT"):
        clearFile(MSGS_FILE)
        return 'Successfully cleared chat'

    return f"Bad command '{cmd}'"

@app.route("/post", methods=["POST"])
def postTest():
	jsonstring = getDictFromJSON(getlJSTRING(request))
	return "[POST] posted: " + str(jsonstring)

@app.route("/echo", methods=["POST"])
def echoEcho():
    jsonstring = getlJSTRING(request)
    return "[ECHO] echod: " + jsonstring