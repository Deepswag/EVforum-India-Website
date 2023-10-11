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
    'title': 'EV Mall Gupta Motors',
    'company': ' Zelio',
    'location': ' Jallandhar, India'
}]


@app.route("/")
def EVforum_India():
  return render_template('home.html', jobs=JOBS, company_name='EVforum India')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route("/blog")
def blog():
  return render_template('blog.html')


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/news")
def news():
  return render_template('news.html')


@app.route("/contact")
def contact():
  return render_template('contact.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
