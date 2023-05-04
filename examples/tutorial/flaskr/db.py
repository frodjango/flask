import sqlite3

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        # https://docs.python.org/3/library/sqlite3.html
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        """ This is a nonstandard convenience method for executing multiple
        SQL statements at once. It issues a COMMIT statement first, then
        executes the SQL script it gets as a parameter. This method disregards
        isolation_level; any transaction control must be added to sql_script."""
        db.executescript(f.read().decode("utf8"))


""" @with_appcontext : Wraps a callback so that it’s guaranteed to be executed with the script’s
application context. If callbacks are registered directly to the app.cli object
then they are wrapped with this function by default unless it’s disabled."""

# https://flask.palletsprojects.com/en/2.1.x/api/?highlight=with_appcontext#flask.cli.with_appcontext

""" Since flask init-db is available as an external CLI command """

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    current_app.logger.info("FROM: db.py/init_db_command")
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.logger.info("FROM: db.py/init_app")
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
