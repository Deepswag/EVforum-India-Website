from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def EVforum_India():
  return render_template('home.html', company_name='EVforum India')


@app.route("/blogs")
def blogs():
  return render_template('blogs.html')


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
