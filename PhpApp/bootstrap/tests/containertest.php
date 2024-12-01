<?php

use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../../vendor/autoload.php';
require_once __DIR__ . '/../container.php';

class ContainerTest extends TestCase
{
    protected $settings;
    protected $capsule;

    protected function setUp(): void
    {
        $this->settings = [
            'debug' => false,
            'database' => [
                'driver' => 'mysql',
                'host' => 'localhost',
                'database' => 'test_db',
                'username' => 'test_user',
                'password' => 'test_password',
                'charset' => 'utf8mb4',
                'collation' => 'utf8mb4_unicode_ci',
                'prefix' => '',
            ],
        ];
        $this->capsule = new \Illuminate\Database\Capsule\Manager();
    }

    public function testMakeContainer()
    {
        $container = makeContainer($this->settings, $this->capsule);

        $this->assertInstanceOf(\DI\Container::class, $container);

        $this->assertSame($this->settings, $container->get('settings'));

        $this->assertInstanceOf(\Psr\Http\Message\ServerRequestInterface::class, $container->get('request'));

        $this->assertInstanceOf(\Psr\Http\Message\ResponseInterface::class, $container->get('response'));

        $this->assertInstanceOf(\Dotenv\Dotenv::class, $container->get('dotenv'));

        $this->assertInstanceOf(\Illuminate\Database\Capsule\Manager::class, $container->get('db'));
    }
}