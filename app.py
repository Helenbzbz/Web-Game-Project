from single import Q1,Q2,Q3,Q4,Q8,Q9,Q10,Q11
from multiple import Q5, Q6, Q7
from flask import Flask, request, render_template, redirect
print(Q1.score('Try to seperate that gril and the person she is attacking'))

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'],endpoint = 'home')
def home():
    if request.method == 'POST':
        return redirect('/Q1')
    else:
        return render_template('home.html')

@app.route('/Q1',methods = ['GET','POST'],endpoint = 'submit1')
def submit1():
    if request.method == 'POST':
        f = open("result.txt", "w")
        f.write(request.form['option'])
        return redirect('/Q2')
    else:
        return render_template('Q1.html',prompt = Q1.prompt)

@app.route('/Q2',methods = ['GET','POST'],endpoint = 'submit2')
def submit2():
    if request.method == 'POST':
        f = open("result.txt", "a+")
        f.write('\n')
        f.write(request.form['option'])
        return redirect('/Q3')
    else:
        return render_template('Q2.html',prompt = Q2.prompt)

@app.route('/Q3',methods = ['GET','POST'],endpoint = 'submit3')
def submit3():
    if request.method == 'POST':
        f = open("result.txt", "a")
        f.write('\n')
        f.write(request.form['option'])
        return redirect('/Q4')
    else:
        return render_template('Q3.html',prompt = Q3.prompt)

@app.route('/Q4',methods = ['GET','POST'],endpoint = 'submit4')
def submit4():
    if request.method == 'POST':
        f = open("result.txt", "a")
        f.write('\n')
        f.write(request.form['option'])
        return redirect('/Q5')
    else:
        return render_template('Q4.html',prompt = Q4.prompt)

@app.route('/Q5',methods = ['GET','POST'],endpoint = 'submit5')
def submit5():
    if request.method == 'POST':
        f = open("result.txt", "a")
        f.write('\n')
        f.write(request.form.getlist('mycheckbox'))
    else:
        return render_template('Q5.html',prompt = Q5.prompt)


if __name__ == "__main__":
    app.run()