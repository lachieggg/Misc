<?php

use Monolog\Logger;

/**
 * getLogger
 *
 * @return Logger
 */
function getLogger()
{
    $settings = [
        // Path to log directory
        'directory' => __DIR__ . '/../logs/',
        // Log file name
        'filename' => 'login-app.log',
        // Your timezone
        'timezone' => 'Australia/Sydney',
        // Log level
        'level' => 'debug',
        // Handlers
        'handlers' => [],
    ];

    // Create a logger instance
    $logger = new Monolog\Logger($settings['filename']);

    // Set the log directory
    $logDirectory = $settings['directory'];

    // Check if the directory exists, if not create it
    if (!is_dir($logDirectory)) {
        mkdir($logDirectory, 0777, true);
    }

    // Create a stream handler to log to a file
    $stream = new Monolog\Handler\StreamHandler($logDirectory . $settings['filename'], $settings['level']);

    // Set the timezone for the logger
    $dateFormat = "Y-m-d H:i:s";
    $output = "%datetime% %channel%.%level_name%: %message% %context% %extra%\n";
    $formatter = new Monolog\Formatter\LineFormatter($output, $dateFormat);
    $stream->setFormatter($formatter);

    // Add the stream handler to the logger
    $logger->pushHandler($stream);

    return $logger;
}
