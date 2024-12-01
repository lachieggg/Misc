<?php

namespace LoginApp\Auth;

use LoginApp\Models\User;

class Auth
{
    /**
     * Attempt to log in a user with the given email and password.
     * If the login is successful, the user's session is updated.
     *
     * @param  string $email    The email of the user to log in
     * @param  string $password The password of the user to log in
     * @return boolean Returns true if the login was successful, false otherwise
     */
    public function attempt(string $email, string $password): bool
    {
        // Query for a user with the given email
        $user = User::where('email', $email)->first();
        // Return false if no user is found
        if (!$user) {
            return false;
        }

        // Verify the given password against the user's hashed password
        if (password_verify($password, $user->password)) {
            // Update the user's session if the password is correct
            $_SESSION['user'] = $user->uuid;
            return true;
        }

        // Return false if the password is incorrect
        return false;
    }

    /**
     * Log out the current user
     */
    public function logout(): void
    {
        unset($_SESSION['user']);
    }

    /**
     * Get the current logged in user
     *
     * @return User|null
     */
    public function user(): ?User
    {
        return isset($_SESSION['user']) ? User::where('uuid', $_SESSION['user'])->first() : null;
    }

    /**
     * Check if a user is logged in
     *
     * @return boolean
     */
    public function check(): bool
    {
        $user = $this->user();
        return isset($user);
    }

    /**
     * Check if the current user is an admin.
     * A user is considered an admin if they have the "is_admin" flag set to 1 in the database.
     *
     * @return boolean Returns true if the user is an admin, false otherwise
     */
    public function admin(): bool
    {
        // Check if a user is logged in
        if (isset($_SESSION['user'])) {
            // Query for a user with the current session's user ID who is an admin
            $user = User::where('uuid', $_SESSION['user'])
                ->where('is_admin', 1)
                ->first();

            return isset($user);
        }

        return false;
    }

    /**
     * Check if the current user is deleted.
     * A user is considered deleted if they have the "is_deleted" flag set to 1 in the database.
     *
     * @return boolean Returns true if the user is deleted, false otherwise
     */
    public function deleted(): bool
    {
        // Query for a user with the current session's user ID who is deleted
        $deleted = User::where('uuid', $_SESSION['user'])
            ->where('is_deleted', '=', 1)
            ->first();

        if (isset($deleted)) {
            return true;
        }
        return false;
    }


    /**
     * Check if the current user is verified.
     * A user is considered verified if they are logged in, not deleted, and approved.
     *
     * @return boolean Returns true if the user is verified, false otherwise
     */
    public function isVerified()
    {
        // Check if user is logged in
        if (!$this->user()) {
            return false;
        }

        // Check if user is deleted
        if ($this->deleted()) {
            return false;
        }

        // Check if user is approved
        if (!$this->approved()) {
            return false;
        }

        // If all checks pass, return true
        return true;
    }

    /**
     * Check if the current user is approved.
     * A user is considered approved if they have the "is_approved" flag set to 1 in the database.
     *
     * @return boolean Returns true if the user is approved, false otherwise
     */
    public function approved()
    {
        // Query for a user with the current session's user ID, who is approved and not deleted
        $approvedUser = User::where('uuid', $_SESSION['user'])
            ->where('is_approved', '=', 1)
            ->where('is_deleted', '!=', 1)
            ->first();

        return isset($approvedUser);
    }
}
