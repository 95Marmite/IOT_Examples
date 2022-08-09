from flask import Flask, render_template, request, Response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('remote_controller.html')

@app.route('/right_left')
def right_left():
    print(request.args.get('value'))
    return Response("{'a':'b'}", status=200, mimetype='application/json')

@app.route('/speed')
def speed():
    print("speed" + request.args.get('value'))
    return Response("{'a':'b'}", status=200, mimetype='application/json')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)