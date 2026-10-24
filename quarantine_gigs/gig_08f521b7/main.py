from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from schemas import Bookmark, BookmarkCreate, BookmarkUpdate
from models import Bookmark as DBBookmark
import crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/bookmarks/", response_model=Bookmark)
def create_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db)):
    db_bookmark = crud.get_bookmark_by_url(db, url=bookmark.url)
    if db_bookmark:
        raise HTTPException(status_code=409, detail="URL already exists")
    return crud.create_bookmark(db=db, bookmark=bookmark)


@app.get("/bookmarks/", response_model=list[Bookmark])
def read_bookmarks(
    skip: int = 0, limit: int = 10, tag: str = None, db: Session = Depends(get_db)
):
    bookmarks = crud.get_bookmarks(db, skip=skip, limit=limit, tag=tag)
    return bookmarks


@app.get("/bookmarks/{bookmark_id}", response_model=Bookmark)
def read_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    db_bookmark = crud.get_bookmark(db, bookmark_id=bookmark_id)
    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return db_bookmark


@app.put("/bookmarks/{bookmark_id}", response_model=Bookmark)
def update_bookmark(
    bookmark_id: int, bookmark: BookmarkUpdate, db: Session = Depends(get_db)
):
    db_bookmark = crud.update_bookmark(db, bookmark_id=bookmark_id, bookmark=bookmark)
    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return db_bookmark


@app.delete("/bookmarks/{bookmark_id}", response_model=Bookmark)
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    db_bookmark = crud.delete_bookmark(db, bookmark_id=bookmark_id)
    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return db_bookmark
