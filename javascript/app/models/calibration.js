var mysql  = require('mysql');
var connectionParams = require('../../config/connectionParams');
function getConnection() {
  var connection = mysql.createConnection(connectionParams);
  return connection;
}

function Calibration() {
  this.findById = function(calibration_id, callback) {
      // callback is (calibration, err)
      // query the calibrations by id
      var query = 'SELECT * FROM calibrations WHERE CalibrationID = ?';
      var connection = getConnection();
      connection.connect();
      connection.query(query, [calibration_id], function(err, results) {
        if(err) {
          callback(null,err);
        } else {
          callback(results[0]);
        }
      });
      connection.end()
    };
  this.findByFilter = function(params, callback) {
    var query = 'SELECT * FROM calibrations WHERE minAge > ? AND maxAge < ?';
    var connection = getConnection();
    connection.connect();
    connection.query(query, [params.min, params.max], function(err, results) {
      if(err) {
        callback(null,err);
      } else {
        callback(results);
      }
    });
    connection.end();
  };
}

module.exports = new Calibration();