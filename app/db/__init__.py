from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# url = f"mysql+pymysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"
url = f"mysql+pymysql://root:admin123!@database-1.cducy0awc26x.ap-northeast-2.rds.amazonaws.com:3306/tredi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        # DB 연결 성공한 경우, DB 세션 시작
        yield db
    finally:
        # DB 세션이 시작된 후, API 호출이 마무리되면 DB 세션을 닫아준다.
        db.close()
