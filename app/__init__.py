from flask import Flask
from app.routes.oauth import router as oauth
from app.routes.mainpage import router as main
app = Flask("Stats")

app.register_blueprint(oauth)
app.register_blueprint(main)

