import os
# import logging
import logging

from flask import Flask

# dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'default': {
#             'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#         },
#         'simpleformatter': {
#             'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#         }
#     },
#     'handlers': {
#         'custom_handler': {
#             'class': 'logging.FileHandler',
#             'formatter': 'default',
#             'filename': 'warnings.log',
#             'level': 'WARN',
#         },
#     },
#     'root': {
#         'level': 'WARN',
#         'handlers': ['custom_handler']
#     },
# })



def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""

    """ This function is known as the application factory. Any
    configuration, registration, and other setup the application
    needs will happen inside the function, then the application
    will be returned. """

    """ https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/ """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        app.logger.debug("debug")
        app.logger.info("info")
        app.logger.warning("warning")
        app.logger.error("error")
        app.logger.critical("critical")
        return "<p>Hello, World!</p>"

    @app.before_first_request
    def before_first_request():
        log_level = logging.DEBUG

        # Uncomment following lines if you only want to have logging within a file
        #
        for handler in app.logger.handlers:
            print("FOUND A LOGGER")
            app.logger.removeHandler(handler)

        root = os.path.dirname(os.path.abspath(__file__))
        logdir = os.path.join(root, 'logs')

        if not os.path.exists(logdir):
            os.mkdir(logdir)
        log_file = os.path.join(logdir, 'app.log')
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        app.logger.addHandler(handler)

        # set logging level to lower level - to witness all
        # V1 app.logger.setLevel(log_level)
        # V2 logging.basicConfig(format='CONSOLE: %(levelname)s:%(message)s', level=logging.DEBUG)

        # Format messaging
        # [2022-04-04 17:37:27,433] CRITICAL in hello: critical

        myFormat = '[DUDE ! %(asctime)s] %(levelname)s in %(module)s: %(message)s'
        defaultFormatter = logging.Formatter(myFormat)
        handler.setFormatter(defaultFormatter)
        logging.basicConfig(format=myFormat, level=log_level)

    # register the database commands (is a module within this flaskr package
    # )
    from flaskr import db

    db.init_app(app)

    # apply the blueprints to the app
    from flaskr import auth, blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    app.logger.info("Salut from end of create_app")

    return app
