<?php

namespace LoginApp\Middleware;

use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Psr\Http\Server\MiddlewareInterface as Middleware;
use Psr\Http\Server\RequestHandlerInterface as RequestHandler;

class ValidationErrorsMiddleware extends CustomMiddleware implements Middleware
{
    /**
     * Process an incoming server request and return a response, optionally delegating
     * to the next middleware component to create the response.
     *
     * @param  Request        $request
     * @param  RequestHandler $handler
     * @return Response
     */
    public function process(Request $request, RequestHandler $handler): Response
    {
        if (isset($_SESSION['errors'])) {
            $this->container->get('view')->getEnvironment()->addGlobal('errors', $_SESSION['errors']);
            unset($_SESSION['errors']);
        }
        return $handler->handle($request);
    }
}
