from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'ABC Motors',
    'company': ' Bajaj Motors',
    'location': ' Bangaluru, India'
}, {
    'id': 2,
    'title': 'XYZ EV Traders',
    'company': ' Tata Motors',
    'location': ' Delhi, India'
}, {
    'id': 3,
    'title': 'Subhash Motors',
    'company': ' Ather India',
    'location': ' Jaipur, India'
}, {
    'id': 4,
    'title': 'Avista EV Trades',
    'company': ' Hero EV Moto',
    'location': ' Jallandhar, India'
}]


@app.route("/")
def EVforum_India():
  return render_template('home.html', jobs=JOBS, company_name='EVforum India')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
