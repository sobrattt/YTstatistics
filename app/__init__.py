from flask import Flask
from app.routes.oauth import router
app = Flask("Stats")

app.register_blueprint(router)

