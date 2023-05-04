Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> @app.route ('/data_predict', methods=['POST'])
... def predict():
...   age = request.form['age']
...   gender = request.form['gender']
...   tb = request.form['tb']
...   db = request.form['db'] 
...   ab = request.form['ap']
...   aa1 = request.form['aa1']
...   aa2 = request.form['aa2']
...   tp = request.form['tp']
...   a = request.form['a']
...   agr = request.form['agr']
...   
...   data = [[float(age), float(gender), float(db), float(ap), float(aa1), float(aa2), float(tp), float(a), float(agr)]]
...   model = pickle.load(open('liver_analysis.pkl', 'rb'))
...   prediction=model.predict(dta)[0]
...   if(prediction == 1):
...       return render_template('nochance.html', prediction='you have a liver desease proble')
...   else:
...       return render_template('chance.html', prediction='you dont have a liver desease problem')
... if _name_ == '_mani_':
