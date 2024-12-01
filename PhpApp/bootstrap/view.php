<?php

use Twig\Loader\FilesystemLoader;
use LoginApp\Logging\MonologExtension;
use Monolog\Logger;
use Twig\Environment;
use Slim\Views\Twig;
use Twig\Extension\DebugExtension;

/**
 * getView
 *
 * @param \DI\Container                            $container The container to be used.
 * @param \Slim\Interfaces\RouteCollectorInterface $router    The router to be used.
 *
 * @return Slim\Views\Twig
 */
function getView(\DI\Container $container, \Slim\Interfaces\RouteCollectorInterface $router)
{
    $settings = $container->get('settings')['twig'];

    $loader = new FilesystemLoader($settings['template_path']);
    $env = new Environment($loader);

    // Set up Monolog
    $logger = new Logger('my_logger');
    // Add Monolog extension to Twig environment
    $monologExtension = new MonologExtension($logger);
    $env->addExtension($monologExtension);

    $env->addGlobal('app', $container);
    $env->addGlobal('router', $router);

    $view = new Twig(
        $loader,
        [
        'cache' => $settings['cache_path'],
        'debug' => $settings['debug'],
        'router' => $router
        ],
        $env
    );

    $view->addExtension(new DebugExtension());

    return $view;
}
