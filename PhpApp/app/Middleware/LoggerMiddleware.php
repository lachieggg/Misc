<?php

namespace LoginApp\Middleware;

use Slim\Psr7\Request;
use Slim\Psr7\Response;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\MiddlewareInterface;
use Psr\Http\Server\RequestHandlerInterface;

class LoggerMiddleware extends CustomMiddleware implements MiddlewareInterface
{
    /**
     * @param Slim\Psr7\Request  $request
     * @param Slim\Psr7\Response $response
     * @param callable           $next
     */
    public function __invoke(Request $request, Response $response, callable $next): Response
    {
        $logger = $this->container->get('logger');
        $logger->info('request');
        $logger->info($request->getUri());

        $logger->info('response');
        $logger->info($response->getStatusCode());

        return $next($request, $response);
    }

    /**
     * Process an incoming server request and return a response, optionally delegating
     * to the next middleware component to create the response.
     *
     * @param ServerRequestInterface  $request
     * @param RequestHandlerInterface $handler
     *
     * @return ResponseInterface
     */
    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
    {
        $logger = $this->container->get('logger');
        $logger->info('request');
        $logger->info($request->getUri());

        $response = $handler->handle($request);

        $logger->info('response');
        $logger->info($response->getStatusCode());

        return $response;
    }
}
