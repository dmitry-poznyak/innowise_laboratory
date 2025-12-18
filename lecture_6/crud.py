from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate):
    db_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False


def update_book(db: Session, book_id: int, updates: BookUpdate):
    book = get_book_by_id(db, book_id)
    if not book:
        return None

    if updates.title is not None:
        book.title = updates.title
    if updates.author is not None:
        book.author = updates.author
    if updates.year is not None:
        book.year = updates.year

    db.commit()
    db.refresh(book)
    return book


def search_books(db: Session, title: str = None, author: str = None, year: int = None):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)

    return query.all()
