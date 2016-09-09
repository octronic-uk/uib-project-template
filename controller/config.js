app.config(
	function($stateProvider, $urlRouterProvider) {
		// For any unmatched url, redirect to /state1
		$urlRouterProvider.otherwise("/home");

		// Now set up the states
		$stateProvider.state('home', {
				url: "/home",
				templateUrl: "view/home.html"
		});
	}
);
