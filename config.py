class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:56789@localhost/blog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'
