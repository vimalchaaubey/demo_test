from flask import Flask, render_template, request

app = Flask(__name__)

PROBLEM_STATEMENTS = [
    "AI for Healthcare",
    "Smart City Solutions",
    "Green Energy Innovations",
    "Blockchain for Education",
    "IoT for Agriculture"
]

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if 'reset' in request.form:
            return render_template('register.html', problem_statements=PROBLEM_STATEMENTS)
        name = request.form.get('name')
        email = request.form.get('email')
        institute = request.form.get('institute')
        branch = request.form.get('branch')
        year = request.form.get('year')
        problem = request.form.get('problem')
        return render_template('register.html',
                               name=name,
                               email=email,
                               institute=institute,
                               branch=branch,
                               year=year,
                               problem=problem,
                               submitted=True,
                               problem_statements=PROBLEM_STATEMENTS)
    return render_template('register.html', problem_statements=PROBLEM_STATEMENTS)

if __name__ == '__main__':
    app.run(debug=True)
