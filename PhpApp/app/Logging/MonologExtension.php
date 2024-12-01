<?php

namespace LoginApp\Logging;

use Monolog\Logger;
use Twig\Extension\AbstractExtension;

class MonologExtension extends AbstractExtension
{
    /**
     * @var Logger
     */
    private $logger;

    public function __construct(Logger $logger)
    {
        $this->logger = $logger;
    }

    public function getLogger(): Logger
    {
        return $this->logger;
    }
}
