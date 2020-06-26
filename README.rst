django-fire
===========

.. image:: https://codecov.io/gh/lordpeara/django-fire/branch/stable/graph/badge.svg
    :target: https://codecov.io/gh/lordpeara/django-fire

.. image:: https://readthedocs.org/projects/django-fire/badge/?version=stable
    :target: https://django-fire.readthedocs.io/en/stable/?badge=stable


django-fire is a toolbox for invalidating users password
when user's password is exposed or password hashing algorithm is cracked.


Quickstart
----------

If you need to invalidate your users' password fast, follow the instructions.

1. install packages

.. code-block:: bash

    $ pip install django-fire


2. add django_fire app to your project

.. code-block:: python

    # settings.py
    # ...
    INSTALLED_APPS = (
        # ...
        'django_fire',
        # ...
    )

3. calling command ``firepassword`` invalidate users' password

.. code-block:: bash

    $ python manage.py firepassword --all  # if all your passwords are exposed.
    $ python manage.py firepassword --users 1 2 3  # for specific users
    $ python manage.py firepassword --hashers md5 crypt  # for hashers (NOT IMPLEMENTED)

4. After invalidating passwords, add auth backend to notice users

.. code-block:: python

    # settings.py
    AUTHENTICATION_BACKENDS = [
        # ...
        # Users (whose password invalidated) are failed to login and
        # see announcement for password reset.
        'django_fire.backends.FiredPasswordBackend',
    ]

Documentation
-------------

`See Documentation <https://django-fire.readthedocs.io>`_
