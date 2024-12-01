<?php

namespace LoginApp\Validation\Rules;

use Respect\Validation\Rules\AbstractRule;
use Respect\Validation\Validator as v;

class PasswordConfirmation extends AbstractRule
{
    /**
     * @param $input
     */
    public function validate($input)
    {
        return v::keyValue('password', 'equals', 'confirmation')->validate($_POST);
    }
}
