from flask import Flask, render_template, jsonify, request
import subprocess
import os
import sys
import json
app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "templates", "markers.json")

@app.route('/')
def index():
    data = json.load(open(json_url))
    return render_template("index.html", data=data);

@app.route('/getData', methods=['GET'])
def getData():
    dir1 = request.args.get('dir1')
    dir2 = request.args.get('dir2')
    port = request.args.get('port')
    index = request.args.get('index')
    wd = os.getcwd()
    os.chdir(wd+'/static/'+dir1+'/'+dir2)
    result = subprocess.run(["docker", "compose", "build"], stdout=subprocess.DEVNULL)
    if(result.returncode != 0):
       os.chdir('../../..'); 
       return jsonify({ 'var1': 'Error running docker, return code: '+str(result.returncode) })
    result = subprocess.run(["docker", "compose", "up", "-d"], stdout=subprocess.DEVNULL)
    if(result.returncode != 0):
       os.chdir('../../..'); 
       return jsonify({ 'var1': 'Error running docker, return code: '+str(result.returncode) })
    os.chdir('../../..')
    data = json.load(open(json_url))
    data[int(index)]["style"] = { "initial": { "fill": "#018749"} }
    data[int(index)]["active"] = 1;
    with open(json_url, "w") as jsonFile:
       json.dump(data, jsonFile)
    return jsonify({ 'var1': 'Docker daemon started, return code: '+str(result.returncode)+'<p><a href="http://'+request.host.split(':')[0]+':'+port+'" target="_blank" class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">http://'+request.host.split(':')[0]+':'+port+'</a></p>', 'var2': index})
  
@app.route('/getDataStop', methods=['GET'])
def getDataStop():
    dir1 = request.args.get('dir1')
    dir2 = request.args.get('dir2')
    index = request.args.get('index')
    wd = os.getcwd()
    data = ''
    os.chdir(wd+'/static/'+dir1+'/'+dir2)
    result = subprocess.run(["docker", "compose", "down", "-v"], stdout=subprocess.DEVNULL)
    if(result.returncode != 0):
       os.chdir('../../..'); 
       return jsonify({ 'var1': 'Error stopping docker, return code: '+str(result.returncode) })
    os.chdir('../../..')
    data = json.load(open(json_url))
    data[int(index)]["style"] = { "initial": { "fill": "#35373e"} }
    data[int(index)]["active"] = 0;
    with open(json_url, "w") as jsonFile:
       json.dump(data, jsonFile)
    return jsonify({ 'var1': 'Docker daemon stopped, return code: '+str(result.returncode) })
    
if __name__ == "__main__":
    app.run(ssl_context='adhoc', host="0.0.0.0", port=5000)
