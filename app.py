from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash
from sklearn.naive_bayes import GaussianNB
import numpy as np

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
        _peso = request.form['inputName']
        _altura = request.form['inputName2']

        if _peso and _altura:
          x = np.array([[2.1,2.0],[2.3,1.9],[2.0,2.5],[1.9,2.6],[2.0,2.2],[2.0,2.0]])
          y = np.array([1,1,2,2,2,1])
          clf = GaussianNB()
          clf.fit(x,y)
          GaussianNB(priors = None)
          new_x = float(_peso)
          new_y = float(_altura)
          print(clf.predict([[new_x ,new_y ]]))
          return 'OK'
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run(port=5002)
