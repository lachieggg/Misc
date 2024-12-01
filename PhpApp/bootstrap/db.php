<?php

use Illuminate\Database\Capsule\Manager;

/**
 * getCapsule
 *
 * @param array $settings The settings array to be used.
 *
 * @return Manager
 */
function getCapsule(array $settings)
{
    $db = $settings['db'];
    $capsule = new Manager();
    $capsule->addConnection($db);
    $capsule->setAsGlobal();
    $capsule->bootEloquent();

    return $capsule;
}
