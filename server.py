from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'
app.visit = 0

@app.route('/')
def index():
   if 'visit' in session:
      session['visit'] = session.get('visit') + 1
   else:
      session['visit'] = 1
   return render_template("index.html")

@app.route('/destroy_session', methods=['POST'])
def destroy():
   session.clear()
   session['visit'] = 0
   return redirect('/')

@app.route('/add_two', methods=['POST'])
def plus():
   if 'visit' in session:
      session['visit'] = session.get('visit') + 2
   return render_template("index.html")

if __name__ == "__main__":
   app.run(debug=True)