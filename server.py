from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/calibrations/<int:calibration_id>")
def calibration(calibration_id):
  return json.dumps({"id":calibration_id})

if __name__ == "__main__":
    app.run(debug=True)