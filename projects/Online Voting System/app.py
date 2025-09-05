from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# In-memory data store for candidates and votes
candidates = {
    'Candidate A': 0,
    'Candidate B': 0,
    'Candidate C': 0
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'voted' not in session:
        session['voted'] = False

    if request.method == 'POST':
        if session.get('voted'):
            flash('You have already voted!', 'error')
        else:
            candidate = request.form['candidate']
            if candidate in candidates:
                candidates[candidate] += 1
                session['voted'] = True
                flash('Thank you for your vote!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', candidates=candidates, has_voted=session['voted'])

if __name__ == '__main__':
    app.run(debug=True)