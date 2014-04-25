'use strict';

/* Controllers */

angular.module('sproutApp.controllers', [])
    .controller('BaseController', ['$scope', '$window', 'brand', 'SessionService', function ($scope, $window, brand, SessionService) {
        $scope.brand = brand;

        $scope.doLogout = function () {
            SessionService.removeSession();
            $window.location = '/';
        };
    }])
    .controller('HomeController', ['$scope', 'SessionService', function ($scope, SessionService) {
        $scope.session = SessionService.getSession();

        $scope.user = {};

        $scope.$on('event:login-confirmed', function () {
            console.log('event has been broadcast to Home Controller');
            $scope.session = SessionService.getSession();
        });
    }])
    .controller('AddRecipeController', function ($scope, SessionService, Restangular) {
        $scope.recipe = {};
        $scope.status = null;
        $scope.methods = [
            {printed_name: 'Bake', stored_name: 'bake'},
            {printed_name: 'Microwave', stored_name: 'microwave'},
            {printed_name: 'Fry', stored_name: 'fry'},
            {printed_name: 'Dutch Oven', stored_name: 'dutch_oven'}
        ]

        $scope.saveNewRecipe = function () {
            Restangular.all('recipes').customPOST($scope.recipe).then(function () {
                $scope.status = 'The Recipe was successfully created!';
                $scope.recipe = {};
            }, function () {
                $scope.status = "The Recipe couldn't be saved";
            });
        }
    })
    .controller('RecipeDetailsController', function ($scope, SessionService, Restangular, $routeParams) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;
        })
    })
    .controller('EditRecipeController', function ($scope, SessionService, Restangular, $routeParams, $location) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;
        })

        $scope.methods = [
            {printed_name: 'Bake', stored_name: 'bake'},
            {printed_name: 'Microwave', stored_name: 'microwave'},
            {printed_name: 'Fry', stored_name: 'fry'},
            {printed_name: 'Dutch Oven', stored_name: 'dutch_oven'}
        ];
        $scope.editRecipe = function () {
            Restangular.one('recipes', $scope.recipeId).customPUT($scope.recipe).then(function (data) {
                $scope.staus = "The recipe was successfully saved";
                $scope.recipe = data;
            }, function () {
                $scope.staus = "The recipe couldn't be saved";
            });
        }
        $scope.deleteRecipe = function () {
            var response = confirm("Are you sure you want to delete this recipe?");

            if (response == true) {

                Restangular.one('recipes', $scope.recipeId).customDELETE().then(function (data) {
                    $location.path('/recipes');

                }, function () {
                    $scope.status = "The recipe couldn't be deleted.";
                });
            }
        };
    })
    .controller('RecipeController', function ($scope, SessionService, Restangular) {
        $scope.session = SessionService.getSession();

        var recipe1 = {
            name: "Recipe one",
            number: "12"
        };

        var recipe2 = {
            name: "Recipe two",
            number: "24"
        };

//        $scope.recipes = [recipe1, recipe2];

        Restangular.all('recipes').getList().then(function (data) {
            $scope.recipes = data;
        });
    });