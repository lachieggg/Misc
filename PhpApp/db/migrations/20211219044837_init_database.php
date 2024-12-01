<?php

use Phinx\Migration\AbstractMigration;

final class InitDatabase extends AbstractMigration
{
    /**
     * Initialize the database
     */
    public function change(): void
    {
        // Users
        $users = $this->table('users');
        $users->addColumn('uuid', 'string')
            ->addColumn('email', 'string')
            ->addColumn('name', 'string')
            ->addColumn('password', 'string')
            ->addColumn('is_deleted', 'boolean', ['default' => false])
            ->addColumn('is_approved', 'boolean', ['default' => false])
            ->addColumn('is_admin', 'boolean', ['default' => false])
            ->addColumn('created_at', 'datetime')
            ->addColumn('updated_at', 'datetime')
            ->create();

        $users->addIndex('uuid', array('unique' => true))->save();
        $users->addIndex('email', array('unique' => true))->save();
    }
}
