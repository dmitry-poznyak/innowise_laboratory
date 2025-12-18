from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import crud
from schemas import BookCreate, BookUpdate, BookOut

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()


# -------------------------
# Endpoints
# -------------------------

@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}


@app.post("/books/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@app.get("/books/", response_model=list[BookOut])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}


@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, updates: BookUpdate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated


@app.get("/books/search/", response_model=list[BookOut])
def search_books(
    title: str = None,
    author: str = None,
    year: int = None,
    db: Session = Depends(get_db)
):
    return crud.search_books(db, title, author, year)
