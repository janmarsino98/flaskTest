from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "La Seu",
        "salary": "20000"
    },
    {
        "id": 2,
        "title": "Data Engineer",
        "location": "Lleida",
        "salary": "50000"
    },
    {
        "id": 3,
        "title": "Data Analyst",
        "location": "Puigcerdà",
        "salary": "30000"
    },
]

@app.route("/")
def hello_jan():
    return render_template('jan.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)