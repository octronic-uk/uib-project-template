app.service('ApiService',[
    '$http',
    function($http) {
        var helloWorld = function(callback) {
            $http({url: "/api/route", method: "get"}).then(
                function onSuccess(resp)
                {
                    callback(resp);
                },
                function onError(resp)
                {
                    callback(null);
                }
            );
        };
        return this;
    }
]);