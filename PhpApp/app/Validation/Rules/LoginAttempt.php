<?php

namespace LoginApp\Validation\Rules;

use Respect\Validation\Rules\AbstractRule;
use Respect\Validation\Validator as v;

class LoginAttempt extends AbstractRule
{
    /**
     * @param $input
     */
    public function validate($input)
    {
        return true;
    }
}
