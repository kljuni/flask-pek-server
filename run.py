from sender_app.app import create_app
from sender_app.settings import Config

CONFIG = Config

app = create_app(CONFIG)