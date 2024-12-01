<?php

namespace LoginApp\Validation\Rules;

use LoginApp\Models\User;
use Respect\Validation\Rules\AbstractRule;

class EmailAvailable extends AbstractRule
{
    /**
     * @param $input
     */
    public function validate($input)
    {
        return User::where('email', $input)->count() === 0;
    }
}
