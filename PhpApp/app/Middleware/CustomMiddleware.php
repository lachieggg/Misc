<?php

namespace LoginApp\Middleware;

class CustomMiddleware
{
    protected $container;

    /**
     * @param $container
     */
    public function __construct($container)
    {
        $this->container = $container;
    }
}
