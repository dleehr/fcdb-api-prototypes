from flask import Flask, request
import json
from app.models.calibration import *
app = Flask(__name__)

@app.route("/api/calibrations/<int:calibration_id>")
def calibration(calibration_id):
  c = Calibration.find_by_id(calibration_id)
  return json.dumps(c, cls=CalibrationEncoder)

@app.route("/api/calibrations")
def calibrations():
  filter_type = request.args.get('filter','')
  if filter_type == 'age':
    min = request.args.get('min','')
    max = request.args.get('max','')
    calibrations = Calibration.filter_by_age(min,max)
    return json.dumps(calibrations, cls=CalibrationEncoder)

if __name__ == "__main__":
    app.run(debug=True)
