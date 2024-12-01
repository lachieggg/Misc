<?php

namespace LoginApp\Models;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    protected $table = 'users';

    protected $fillable = [
        'uuid',
        'email',
        'name',
        'password',
    ];
}
