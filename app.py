
from models import Base, Book, engine, session



if __name__ == '__main__':
    Base.metadata.create_all(engine)