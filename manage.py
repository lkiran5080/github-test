""" from dotenv import load_dotenv
load_dotenv('local.env') """

import os
from app import create_app


app = create_app()

if __name__ == '__main__':
    print(os.environ.get('SQLALCHEMY_DATABASE_URI'))
    app.run(debug=True)