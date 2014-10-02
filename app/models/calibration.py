import mysql.connector
from config.connection_params import PARAMS
from json import JSONEncoder

connection = mysql.connector.connect(**PARAMS)

class Calibration(dict):
  @classmethod
  def find_by_id(cls, calibration_id):
    cursor = connection.cursor()
    query = "SELECT * FROM calibrations WHERE CalibrationID = %d LIMIT 1" % calibration_id
    cursor.execute(query)
    calibration = None
    for row in cursor:
      calibration = Calibration(column_names=cursor.column_names, values=row)
    cursor.close()
    return calibration
  def __init__(self, column_names=None, values=None):
    d = dict(zip(column_names,values))
    for key in d:
      self[key] = d[key]

class CalibrationEncoder(JSONEncoder):
  def default(self,obj):
    from datetime import date
    from datetime import datetime
    if isinstance(obj, datetime):
      return obj.isoformat()
    elif isinstance(o, date):
      return obj.isoformat()
    else:
      return super(CalibrationEncoder, self).default(obj)