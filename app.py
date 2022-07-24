from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import json
import calc

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
#main window(part 3 - web aplication)
@app.route('/', methods=['GET', 'POST'])
def home():
    is_string = True
    output = ""
    #checking that the user sent information for the website
    if request.method == 'POST':
        #checking if the input values are empty
        if request.form['v0'] == "" or request.form['alpha0'] == "" or request.form['h0'] == "":
            output = 'Please fill in all fields'
        else:
            #getting the values of the input
            v0 = float(request.form['v0'])
            alpha = float(request.form['alpha0'])
            h = float(request.form['h0'])
            #checking that the values are correct(as explained in the word file)
            if v0 <= 0 or alpha < 0 or h < 0:
                #error message if not
                output = 'Please fill in all fields correctly'
            else:
                output = calc.calc(v0, alpha, h)
                is_string = False
        return render_template('index.html', output=output, is_string=is_string)
    return render_template('index.html', output=output, is_string=is_string)

#api(part 2 -  architecture)
@app.route('/api', methods=['GET', 'POST'])
def api():
    #checking if the input values are not empty
    if request.args.get('v0') and request.args.get('alpha0') and request.args.get('h0'):
        #getting the input values 
        v0 = float(request.args.get('v0'))
        alpha0 = float(request.args.get('alpha0'))
        h0 = float(request.args.get('h0'))
        #check that the values are correct (as explained in the word file)
        if v0 <= 0 or alpha0 < 0 or h0 < 0:
            #error message if the input is not correct
            return jsonify({'error': 'Please fill in all fields correctly'})
        #return json export for the file
        return jsonify(calc.calc(v0, alpha0, h0))
    else:
        #returning default answer if there is no input
        return jsonify(calc.calc(1, 1, 1))
if __name__ == '__main__':
    #running the app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)