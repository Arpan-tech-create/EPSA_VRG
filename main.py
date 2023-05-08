from flask import Flask,render_template,jsonify,request

app = Flask(__name__,template_folder='templates')

@app.route('/')
def main():
    return render_template('index.html',data={'data'})

@app.route('/bar1')
def bar1():
    return render_template('bar1.html',data={'data'})
@app.route('/bar2')
def bar2():
    return render_template('bar2.html',data={'data'})
@app.route('/bar3')
def bar3():
    return render_template('bar3.html',data={'data'})
@app.route('/bar4')
def bar4():
    return render_template('bar4.html',data={'data'})
@app.route('/bar5')
def bar5():
    return render_template('bar5.html',data={'data'})
app.run(debug=True,port=5002)