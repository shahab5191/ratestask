from waitress import serve
from src import create_app
from src.config import Config


if __name__ == '__main__':
    app = create_app()
    serve(app, host='0.0.0.0', port=Config().SERVER_PORT)
