from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key = True)
    title = Column('Title', String)
    author = Column('Author', String)
    published = Column('Date Published', Date)
    medium = Column('Medium', String)
    genre = Column('Genre', String)

    def __repr__(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nDate: {self.published}\nMedium: {self.medium}\nGenre: {self.genre}'