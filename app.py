from flask import Flask, render_template, jsonify 

app = Flask(__name__)

JOBS = [
{
  'id':1,
  'title':'data analyst',
  'location':'bengaluru,india',
  'salary':'10000'
},
  {
  'id':2,
  'title':'data scientist',
  'location':'kerala,india',
  'salary':'20000'
},
  {
  'id':3,
  'title':'frontend developer',
  'location':'delhi,india',
  
},
  {
  'id':4,
  'title':'backend developer',
  'location':'america',
  'salary':'$10000'
}
  
]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs"):
def list_jobs();
jsonify(JOBS)

if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)
