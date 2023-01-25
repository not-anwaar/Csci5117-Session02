from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hi', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True) 

