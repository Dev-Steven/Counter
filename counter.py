from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Shhh'

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    else: 
        session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/increment', methods=['POST'])
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    