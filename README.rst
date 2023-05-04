Commentaires de Fro (May 2023)

le venv est dans le folder /Users/frodjango/code/FlaskExample/flask/examples/tutorial


0) source venv/bin/activate

as per May 2023

click              8.1.2
Flask              2.1.1
flaskr             1.0.0   /Users/frodjango/code/FlaskExample/flask/examples/tutorial
importlib-metadata 4.11.3
itsdangerous       2.1.2
Jinja2             3.1.1
MarkupSafe         2.1.1
pip                21.2.4
setuptools         58.1.0
Werkzeug           2.1.1
zipp               3.8.0

1) allez à /Users/frodjango/code/FlaskExample/flask/examples/tutorial
2) flask run

option for next step

3) open and read the following

/Users/frodjango/code/FlaskExample/flask/examples/tutorial/README.rst

when you'll learn on the ENV settings

.. export FLASK_APP=flaskr
.. export FLASK_ENV=development
.. flask init-db
.. flask run










Flask
=====

Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.

.. _WSGI: https://wsgi.readthedocs.io/
.. _Werkzeug: https://werkzeug.palletsprojects.com/
.. _Jinja: https://jinja.palletsprojects.com/


Installing
----------

Install and update using `pip`_:

.. code-block:: text

    $ pip install -U Flask

.. _pip: https://pip.pypa.io/en/stable/getting-started/


A Simple Example
----------------

.. code-block:: python

    # save this as app.py
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"

.. code-block:: text

    $ flask run
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Contributing
------------

For guidance on setting up a development environment and how to make a
contribution to Flask, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/pallets/flask/blob/main/CONTRIBUTING.rst


Donate
------

The Pallets organization develops and supports Flask and the libraries
it uses. In order to grow the community of contributors and users, and
allow the maintainers to devote more time to the projects, `please
donate today`_.

.. _please donate today: https://palletsprojects.com/donate


Links
-----

-   Documentation: https://flask.palletsprojects.com/
-   Changes: https://flask.palletsprojects.com/changes/
-   PyPI Releases: https://pypi.org/project/Flask/
-   Source Code: https://github.com/pallets/flask/
-   Issue Tracker: https://github.com/pallets/flask/issues/
-   Website: https://palletsprojects.com/p/flask/
-   Twitter: https://twitter.com/PalletsTeam
-   Chat: https://discord.gg/pallets
