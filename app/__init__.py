from flask import Flask
from app.routes.oauth import router as oauth
from app.routes.mainpage import router as main
from app.routes.statistics import router as statistics
app = Flask("Stats")

app.register_blueprint(oauth)
app.register_blueprint(main)
app.register_blueprint(statistics)
