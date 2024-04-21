from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import load_jobs_from_db, select_jobs_from_db

app = Flask(__name__)


@app.route('/')
def home():
  response = load_jobs_from_db()
  jobs = response.data
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  response = load_jobs_from_db()
  jobs = response.data
  return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
  response = select_jobs_from_db(id)
  job = response.data
  if not job:
    return "Not Found" ,404
  return render_template('jobpage.html', job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
