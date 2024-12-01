<?php

use Dotenv\Dotenv;

/**
 * getSettings returns a settings
 * array
 *
 * @return array
 */
function getSettings()
{
    $dotenv = Dotenv::createImmutable(__DIR__ . "/../");
    $dotenv->load();

    // Fetch database settings
    $host = getenv('POSTGRES_HOST');
    $username = getenv('POSTGRES_USER');
    $database = getenv('POSTGRES_DB');
    $password = getenv('POSTGRES_PASSWORD');
    $port = getenv('POSTGRES_PORT');
    $driver = 'pgsql';

    // Set up the settings for the container
    $settings = [
        'twig' => [
            'cache_path' => './twig-cache',
            'debug' => true,
            'auto_reload' => true,
            'template_path' => __DIR__ . '/../resources/views'
        ],
        'db' => [
            'driver' => $driver,
            'host' => $host,
            'database' => $database,
            'username' => $username,
            'password' => $password,
            'port' => $port,
            'charset' => 'utf8',
            'collation' => 'utf8_unicode_ci'
        ],
        'displayErrorDetails' => true,
        'debug' => true,
    ];

    return $settings;
}
