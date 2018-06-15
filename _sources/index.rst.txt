.. Dqpy documentation master file, created by
   sphinx-quickstart on Wed Jan 18 23:59:28 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dqpy
====

Danqing's shared Python library, written with love for `the better Danqing <https://danqing.co/>`_.

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

Config
------

The config module helps getting configurations from TOML files stored in the ``config/`` folder. The default file to use is ``config/local.toml``. To use another file, specify the ``DQENV`` environment variable. For example, if ``DQENV=production``, then the ``config/production.toml`` file will be used. Nested keys are comma-separated.

.. automodule:: dq.config
   :members:
   :undoc-members:
   :show-inheritance:

Database
--------

SQL database client. This module provides connectors to the SQL database, with its configs specified (by you) in the config files. Check out the ``config/local.toml`` file for an example configuration.

.. automodule:: dq.database
   :members:
   :undoc-members:
   :show-inheritance:

DBAdmin
-------

This module is designed to be used as a shell script, for creating and dropping the database.

.. code-block:: bash

   dbadmin create  # Create a database with URL at sql.url
   dbadmin drop    # Drop the above database
   dbadmin create another_sql.url  # Create a database with URL at anothersql.url

.. automodule:: dq.dbadmin
   :members:

Email
-----

Module for sending emails.

.. automodule:: dq.email
   :members:
   :undoc-members:
   :show-inheritance:

Entity
------

The entity module provide basic functionalities for Schematics entity classes.

.. automodule:: dq.entity
  :members:
  :undoc-members:
  :show-inheritance:

Errors
------

The errors module contains a bunch of error classes so we don't need to redefine them over and over. They also translate to HTTP errors nicely.

.. automodule:: dq.errors
   :members:
   :undoc-members:
   :show-inheritance:

Logging
-------

The logging module helps format logging messages. It prints the message and pretty-prints the attached data dictionary. Use it as follows:

.. code-block:: python

   import logging
   from dq.logging import error

   logger = logging.getLogger(__name__)
   error(logger, 'An error!', {'key': 'value'})

.. automodule:: dq.logging
   :members:
   :undoc-members:
   :show-inheritance:

ORM
---

The SQL ORM base classes. Your model classes should most likely inherit from ``IDBase`` or ``UUIDBase``, and some other mixins.

.. automodule:: dq.orm
   :members:
   :undoc-members:
   :show-inheritance:

Redis
-----

The Redis client. It reads the config files for Redis configs, which you must specify to use this client. Refer to the ``config/local.toml`` file in this repo for an example.

.. automodule:: dq.redis
   :members:
   :undoc-members:
   :show-inheritance:

Retry
-----

Retry helpers. A function can raise ``RecoverableError`` as needed so that it can be retried. The SQL variant can also be used to retry SQL errors.

.. automodule:: dq.retry
  :members:
  :undoc-members:
  :show-inheritance:

String
------

String utilities that you may find useful.

.. automodule:: dq.string
   :members:
   :undoc-members:
   :show-inheritance:
