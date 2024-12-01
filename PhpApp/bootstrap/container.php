<?php

use DI\Container;
use DI\ContainerBuilder;
use Dotenv\Dotenv;
use Slim\Factory\ServerRequestCreatorFactory;
use Illuminate\Database\Capsule\Manager;

/**
 * makeContainer
 *
 * @param array   $settings The settings array to be used.
 * @param Manager $capsule  The database manager capsule.
 *
 * @return Container
 */
function makeContainer(array $settings, Manager $capsule)
{
    $containerBuilder = new ContainerBuilder();

    // Add the settings to the container
    $containerBuilder->addDefinitions(
        [
        'settings' => $settings,
        'request'  => function () {
            $serverRequestCreator = ServerRequestCreatorFactory::create();
            return $serverRequestCreator->createServerRequestFromGlobals();
        },
        'response' => function () {
            return new \Slim\Psr7\Response();
        },
        ]
    );

    $container = $containerBuilder->build();

    // Dotenv
    $dotenv = Dotenv::createImmutable(__DIR__ . "/../");
    $dotenv->load();
    $container->set('dotenv', $dotenv);

    // Database
    $container->set('db', $capsule);

    return $container;
}
