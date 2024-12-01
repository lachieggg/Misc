<?php

namespace LoginApp\Controllers;

use Slim\Psr7\Request;
use Slim\Psr7\Response;
use Slim\Views\Twig as View;

class HomeController extends Controller
{
    /**
     * @var string
     */
    protected $resume;

    /**
     * @var string
     */
    protected $github;

    /**
     * @var View
     */
    protected $view;

    /**
     * HomeController constructor.
     *
     * @param $container
     */
    public function __construct($container)
    {
        parent::__construct($container);
        $this->resume = getenv('URL') . getenv('RESUME_PATH');
        $this->github = getenv('GITHUB_URL');
        $this->view = $container->get('view');
    }

    /**
     * Render the index page
     *
     * @param Request  $request
     * @param Response $response
     * @return mixed
     */
    public function index(Request $request, Response $response)
    {
        return $this->container->get('view')->render(
            $response,
            'home/home.twig',
            [
                'test' => 'test'
            ]
        );
    }

    /**
     * Render the gallery page
     *
     * @param Request  $request
     * @param Response $response
     * @return mixed
     */
    public function gallery(Request $request, Response $response)
    {
        return $this->container->get('view')->render($response, 'home/gallery.twig');
    }

    /**
     * Redirect to Github URL
     *
     * @param Request  $request
     * @param Response $response
     */
    public function github(Request $request, Response $response)
    {
        header("Location: " . $this->github);
        die();
    }

    /**
     * Redirect to resume URL
     *
     * @param Request  $request
     * @param Response $response
     */
    public function resume(Request $request, Response $response)
    {
        header("Location: " . $this->resume);
        die();
    }

    /**
     * Output the public key file
     *
     * @param Request  $request
     * @param Response $response
     */
    public function publickey(Request $request, Response $response)
    {
        header('Content-Type: text/plain');
        echo file_get_contents('./pgp/public.pem');
        die();
    }


    /**
     * Render the blog page
     *
     * @param Request  $request
     * @param Response $response
     * @return Response
     */
    public function blog(Request $request, Response $response)
    {
        echo file_get_contents("html/blog/blog.html");

        return $response;
    }
}
