<?php

/**
 * setErrorHandlers
 *
 * @param \Slim\App     $app       The slim app object.
 * @param \DI\Container $container The container object.
 *
 * @return void
 */
function setErrorHandlers(\Slim\App $app, \DI\Container $container)
{
    // Define a custom error handler for 404 Not Found errors
    $app->map(
        ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
        '/{routes:.+}',
        function (Slim\Psr7\Request $request, Slim\Psr7\Response $response) {
            $response = $response->withStatus(404, 'Not Found');
            $response->getBody()->write('404 Not Found');
            return $response;
        }
    );

    // Overrides the default Slim Error handler for internal errors
    // and adds a custom handler. This prevents Slim stack traces
    // from being shown to the user.
    $container->set(
        'errorHandler',
        function ($container) {
            return function ($request, $response, $exception) use ($container) {
                $container->get('logger')->error($exception->getTraceAsString());
                return $response->withStatus(500)
                    ->withHeader('Content-Type', 'text/html')
                    ->write('Something went wrong!');
            };
        }
    );
}
