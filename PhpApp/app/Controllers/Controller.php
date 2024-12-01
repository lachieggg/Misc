<?php

namespace LoginApp\Controllers;

class Controller
{
    /**
     * @var $container
     */
    protected $container;
    protected $privacy_mode;

    /**
     * @param $container
     */
    public function __construct($container)
    {
        $this->privacy_mode = true;
        $this->container = $container;
    }

    /**
     * @param $property
     */
    public function __get($property)
    {
        if ($this->container->{$property}) {
            return $this->container->{$property};
        }
    }
}
