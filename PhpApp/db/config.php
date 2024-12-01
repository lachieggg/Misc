<?php

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . "/../");
$dotenv->load();

return [
    'paths' => [
        'migrations' => 'db/migrations',
        'seeds' => 'db/seeds',
    ],
    'environments' => [
        'default_database' => 'production',
        'production' => [
            'adapter' => 'pgsql',
            'host' => getenv('POSTGRES_HOST'),
            'name' => getenv('POSTGRES_DB'),
            'user' => getenv('POSTGRES_USER'),
            'pass' => getenv('POSTGRES_PASSWORD'),
            'port' => getenv('POSTGRES_PORT'),
        ],
    ],
];
