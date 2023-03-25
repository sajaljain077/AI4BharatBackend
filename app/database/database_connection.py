from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemyDatabaseUrl = 'mysql+pymysql://root:root@localhost:3306/language_trans_data_creation'

#TODO: Entire connection string must come from config including db name. If there no need dont store this pieces separate 
# sqlalchemyDatabaseUrl= dbProtocol + "+" + dialectics + "://" + dbUsername + ":" + dbPassword + "@" + mysqlAuroraDBUrl + ":" + str(auroraPort) + "/" + auroraDBName
# sqlalchemyDatabaseUrl = 'mysql+pymysql://root:root@localhost:3306/PlatformTest1'
engine = create_engine(
    sqlalchemyDatabaseUrl, pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()