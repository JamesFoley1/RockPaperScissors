from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "Keep it secret keep it safe"


@app.route('/')
def index():
    
    if 'Wins' not in session:
        session['Wins'] = 0
        session['Losses'] = 0
        session['Ties'] = 0

    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    comp = random.choice(['Rock', 'Paper', 'Scissors'])
    print(request.form['choice'])
    print(comp)
    result = {
        'Rock':{'Rock':'Ties', 'Paper':'Losses','Scissors':'Wins'},
        'Paper':{'Rock':'Wins', 'Paper':'Ties','Scissors':'Losses'},
        'Scissors':{'Rock':'Losses', 'Paper':'Wins','Scissors':'Ties'}
    }
    print(result[request.form['choice']][comp])
    session[result[request.form['choice']][comp]] += 1

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":

    app.run(debug=True)