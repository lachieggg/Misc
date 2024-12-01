<?php

use LoginApp\Auth\Auth;
use LoginApp\Validation\Validator;
use LoginApp\Controllers\HomeController;
use LoginApp\Controllers\AuthController;
use LoginApp\Controllers\ContactController;
use LoginApp\Middleware\OldInputMiddleware;
use LoginApp\Middleware\ValidationErrorsMiddleware;
use LoginApp\Middleware\LoggerMiddleware;
use Respect\Validation\Validator as RespectValidation;
use Slim\Factory\AppFactory;
use Slim\Handlers\Strategies\RequestResponseArgs;

// Start new session
session_start();

// Require
require __DIR__ . '/log.php';
require __DIR__ . '/container.php';
require __DIR__ . '/settings.php';
require __DIR__ . '/db.php';
require __DIR__ . '/view.php';
require __DIR__ . '/errors.php';
require __DIR__ . '/routes.php';
require __DIR__ . '/../vendor/autoload.php';

// Get application settings
$settings = getSettings();

// Configure Eloquent
$capsule = getCapsule($settings);

// Create container
$container = makeContainer($settings, $capsule);

// Create the app instance
AppFactory::setContainer($container);
$app = AppFactory::create();

// Define the router
$routeCollector = $app->getRouteCollector();
$routeCollector->setDefaultInvocationStrategy(new RequestResponseArgs());
defineRoutes($routeCollector);

// Set container parameters
$container->set('auth', new Auth());
$container->set('validator', new Validator());
$container->set('view', getView($container, $routeCollector));
$container->set('logger', getLogger());

// Controllers
$container->set('HomeController', new HomeController($container));
$container->set('AuthController', new AuthController($container));
$container->set('ContactController', new ContactController($container));

// Add Middleware
$app->add(new ValidationErrorsMiddleware($container));
$app->addMiddleware(new OldInputMiddleware($container));
$app->addMiddleware(new LoggerMiddleware($container));
$app->addRoutingMiddleware();
$app->addErrorMiddleware(true, true, true);

// Add validation engine
RespectValidation::with('\\LoginApp\\Validation\\Rules\\');

// Set some error handlers
setErrorHandlers($app, $container);
