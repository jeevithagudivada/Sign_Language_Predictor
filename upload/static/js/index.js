'use strict';

(function() {
  
  
  //define app
  angular.module('app', []);

  angular.module('app').controller('mainCtrl', [ '$scope', function( $scope){
    $scope.section = 2;
    $scope.changeSec = function(num){
        $scope.section = num;
    };
 
	}]);

})();