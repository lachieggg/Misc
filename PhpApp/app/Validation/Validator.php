<?php

namespace LoginApp\Validation;

use Respect\Validation\Exceptions\NestedValidationException;

class Validator
{
    protected $errors;

    /**
     * Validate a request.
     *
     * @param $request The request to validate
     * @param array                           $rules The validation rules to apply
     */
    public function validate($request, array $rules)
    {
        // Get the request body parameters
        $params = $request->getParsedBody();
        // Iterate over the validation rules
        foreach ($rules as $field => $rule) {
            try {
                // Validate the field using the given rule
                $rule->setName(ucfirst($field))->assert($params[$field]);
            } catch (NestedValidationException $e) {
                // Store any validation errors
                $this->errors[$field] = $e->getMessages();
            }
        }

        // Store the errors in the session
        $_SESSION['errors'] = $this->errors;

        return $this;
    }


    public function failed()
    {
        return !empty($this->errors);
    }
}
