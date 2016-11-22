import yaml
import os


def Config(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.abspath(os.path.join(basedir, "..", "conf", "link.yml"))

    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    app.config['LINK'] = cfg[os.getenv("LINK_ENV", "development")]

    return app
