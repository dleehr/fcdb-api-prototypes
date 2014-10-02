from flask import Flask
import json
from app.models.calibration import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/calibrations/<int:calibration_id>")
def calibration(calibration_id):
  c = Calibration.find_by_id(calibration_id)
  return json.dumps(c, cls=CalibrationEncoder)

if __name__ == "__main__":
    app.run(debug=True)
