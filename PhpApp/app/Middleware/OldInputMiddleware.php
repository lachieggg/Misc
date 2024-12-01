<?php

namespace LoginApp\Middleware;

use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\MiddlewareInterface;
use Psr\Http\Server\RequestHandlerInterface;

class OldInputMiddleware extends CustomMiddleware implements MiddlewareInterface
{
    /**
     * @var \Slim\Interfaces\RouterInterface
     */
    protected $router;

    /**
     * @var \Slim\Interfaces\FlashInterface
     */
    protected $flash;

    /**
     * @var \Slim\Views\Twig
     */
    protected $view;

    /**
     * Process a request.
     *
     * @param ServerRequestInterface  $request The request object
     * @param RequestHandlerInterface $handler The request handler
     *
     * @return ResponseInterface The response object
     */
    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
    {
        // Check if there are old input values in the session
        if (isset($_SESSION['old_input'])) {
            // Add the old input values to the view environment
            $this->container->view->getEnvironment()->addGlobal('old_input', $_SESSION['old_input']);
            // Update the old input values in the session
            $_SESSION['old_input'] = $request->getParsedBody();
        }

        // Process the request and return the response
        return $handler->handle($request);
    }
}
