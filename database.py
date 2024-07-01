from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import sessionmaker, declarative_base

from datetime import date

from config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASS

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    genre_id = Column(Integer, ForeignKey('genres.genre_id'))
    price = Column(Float)
    amount = Column(Integer)


class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    name_author = Column(String)


class Genre(Base):
    __tablename__ = 'genres'

    genre_id = Column(Integer, primary_key=True)
    name_genre = Column(String)


class BuyBook(Base):
    __tablename__ = 'buy_books'

    buy_book_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buys.buy_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))
    amount = Column(Integer)


class Buy(Base):
    __tablename__ = 'buys'

    buy_id = Column(Integer, primary_key=True)
    buy_description = Column(String)
    client_id = Column(Integer, ForeignKey('clients.client_id'))


class Client(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True)
    name_client = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    email = Column(String)


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True)
    name_city = Column(String)
    days_delivery = Column(Integer)


class Step(Base):
    __tablename__ = 'steps'

    step_id = Column(Integer, primary_key=True)
    name_step = Column(String)


class BuyStep(Base):
    __tablename__ = 'buy_steps'

    buy_step_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buys.buy_id'))
    step_id = Column(Integer, ForeignKey('steps.step_id'))
    data_step_beg = Column(Date)
    data_step_end = Column(Date)


Base.metadata.create_all(engine)
session = Session()

try:
    author1 = Author(name_author='John Smith')
    session.add(author1)
    session.commit()

    genre1 = Genre(name_genre='Fiction')
    session.add(genre1)
    session.commit()

    book1 = Book(title='Python Programming', author_id=1, genre_id=1, price=29.99, amount=100)
    session.add(book1)
    session.commit()

    city1 = City(name_city='New York', days_delivery=3)
    session.add(city1)
    session.commit()

    client1 = Client(name_client='Alice Brown', city_id=1, email='alice@example.com')
    session.add(client1)
    session.commit()

    step1 = Step(name_step='Order placed')
    session.add(step1)
    session.commit()

    buy1 = Buy(buy_description='First purchase', client_id=1)
    session.add(buy1)
    session.commit()

    buy_book1 = BuyBook(buy_id=1, book_id=1, amount=2)
    session.add(buy_book1)
    session.commit()

    buy_step1 = BuyStep(buy_id=1, step_id=1, data_step_beg=date.today(), data_step_end=None)
    session.add(buy_step1)

    session.commit()
    print("Записи успешно добавлены в базу данных!")

except Exception as e:
    print(f"Произошла ошибка при добавлении записей: {e}")
    session.rollback()

finally:
    session.close()
