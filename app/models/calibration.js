var mysql       = require('mysql');


function Calibration() {
  this.findById = function(calibration_id, callback) {
      // callback is (calibration, err)
      callback({id: calibration_id});
    };
};

module.exports = new Calibration();