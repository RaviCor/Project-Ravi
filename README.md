flask --app 'app:create_app("config.DevConfig")' run
flask --app 'app:create_app("config.ProdConfig")' run

export FLASK_APP='app:create_app("DevConfig")'
export FLASK_ENV=development
flask run --debug