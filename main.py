import os
from app import create_app, db

app = create_app()

db_uri = app.config['SQLALCHEMY_DATABASE_URI']
if db_uri.startswith('sqlite:///'):
    db_path = db_uri.split('///')[-1]
    if db_path:
        db_dir = os.path.dirname(db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
