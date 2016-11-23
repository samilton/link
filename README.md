# Link

# Dependencies

* Flask (0.11.1)
* SQLAlchemy (1.1.3)
* Flask-SQLAlchemy (2.1)
* PyYAML (3.12)

# Running

  ./app.py

# Configuration

Configuring Link is achieved by editing conf/link.yml. Right now, only database.uri is used. You set the environment at runtime through:

  LINK_ENV=production ./app.py

This will cause Link to start using `production.*` as its source for configuration. The default environment is `development`. The `test` environment is not used but the idea here would be to be able to completely bootstrap a sqlite database with an appropriate set of data to run any tests we would want to run in a sandbox.


# TODO

* Unit Testing
* Coverage
* Flesh out reset of models
* Flesh out full API

