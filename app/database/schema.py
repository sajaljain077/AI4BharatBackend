from sqlalchemy import DECIMAL, Column, Date, DateTime, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import CHAR, FLOAT, INT, JSON, SMALLINT, TEXT, VARCHAR, BigInteger, Boolean, Enum, TIMESTAMP
from database.database_connection import Base
from sqlalchemy.dialects.mysql import MEDIUMTEXT



class Language(Base):
    __tablename__ = "Language"
    lang_id = Column(INT, primary_key=True, autoincrement=True)
    language = Column(VARCHAR(45))
    PROJECT = relationship("Project", backref="Language")


class Project(Base):
    __tablename__ = "Project"
    project_id = Column(INT, primary_key=True, autoincrement=True)
    project_title = Column(VARCHAR(45))
    project_lang_id = Column(ForeignKey("Language.lang_id"))
    SENTENCE = relationship("Sentence", backref="Project")


class Sentence(Base):
    __tablename__ = "Sentence"
    sen_id = Column(INT, primary_key=True, autoincrement=True)
    project_id = Column(ForeignKey("Project.project_id"))
    original_sentence = Column(TEXT)
    translated_sentence = Column(TEXT)
