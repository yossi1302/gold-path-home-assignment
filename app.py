from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import json
import calc

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

@app.route('/', methods=['GET', 'POST'])
def home():
    is_string = True
    output = ""
    if request.method == 'POST':
        if request.form['v0'] == "" or request.form['alpha0'] == "" or request.form['h0'] == "":
            output = "Please fill in all fields"
        else:
            v0 = float(request.form['v0'])
            alpha = float(request.form['alpha0'])
            h = float(request.form['h0'])
            if v0 <= 0 or alpha < 0 or h < 0:
                output = "Please fill in all fields correctly"
            else:
                output = calc.calc(v0, alpha, h)
            is_string = False
        if type(output) == str:
            is_string = True
        return render_template("index.html", output=output, is_string=is_string)
    return render_template('index.html', output=output, is_string=is_string)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.args.get('v0') and request.args.get('alpha0') and request.args.get('h0'):
        v0 = float(request.args.get('v0'))
        alpha0 = float(request.args.get('alpha0'))
        h0 = float(request.args.get('h0'))
        if v0 <= 0 or alpha0 < 0 or h0 < 0:
            return jsonify({"error": "Please fill in all fields correctly"})
        return json.dumps(calc.calc(v0, alpha0, h0))
    else:
        return json.dumps(calc.calc(1, 1, 1))
if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)