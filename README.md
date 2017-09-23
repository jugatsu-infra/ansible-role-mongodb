Ansible Role: MongoDB
=========

An Ansible Role that installs MongoDB (https://www.mongodb.com).

Requirements
------------

This role only supports Ubuntu 12.x, 14.x, 16.x.

Role Variables
--------------

    mongodb_bind_ip: 127.0.0.1

The IP address that MongoDB binds to in order to listen for connections. Default: `127.0.0.1`

    mongodb_port: 27017

The TCP port on which the MongoDB instance listens for client connections. Default: `27017`

    mongodb_version: 3.4.7

The version of MongoDB to install. Default: `3.4.7`

Example Playbook
----------------

    - hosts: dbservers
      roles:
         - { role: ansible-role-mongodb }

License
-------

BSD
