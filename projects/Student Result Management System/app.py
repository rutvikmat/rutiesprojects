from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'results_secret'

# In-memory database
students = {}  # { 'student_id': 'name' }
results = []  # [ {'student_id': 'id', 'subject': 'math', 'marks': 90} ]
next_student_id = 1


@app.route('/')
def index():
    # Prepare data for display
    display_results = []
    for res in results:
        student_name = students.get(res['student_id'], 'Unknown')
        display_results.append({
            'name': student_name,
            'subject': res['subject'],
            'marks': res['marks']
        })
    return render_template('index.html', results=display_results)


@app.route('/add_result', methods=['GET', 'POST'])
def add_result():
    global next_student_id
    if request.method == 'POST':
        student_name = request.form['name']
        subject = request.form['subject']
        marks = request.form['marks']

        # Find if student exists, or create a new one
        student_id = None
        for sid, name in students.items():
            if name.lower() == student_name.lower():
                student_id = sid
                break

        if student_id is None:
            student_id = str(next_student_id)
            students[student_id] = student_name
            next_student_id += 1

        results.append({'student_id': student_id, 'subject': subject, 'marks': marks})
        flash('Result added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_result.html')


if __name__ == '__main__':
    app.run(debug=True)