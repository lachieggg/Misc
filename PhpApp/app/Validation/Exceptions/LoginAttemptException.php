<?php

namespace LoginApp\Validation\Exceptions;

use Respect\Validation\Exceptions\ValidationException;

class LoginAttemptException extends ValidationException
{
    public static $defaultTemplates = [
        self::MODE_DEFAULT => [
            self::STANDARD => 'Incorrect email address or password.',
        ],
    ];
}
