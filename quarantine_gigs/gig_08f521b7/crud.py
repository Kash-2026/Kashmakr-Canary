from sqlalchemy.orm import Session
from datetime import datetime
try:
    from database import Bookmark, Tag, SessionLocal, engine, Base
except ImportError:
    from model import Bookmark, Tag, SessionLocal, engine, Base

def get_bookmark(db: Session, bookmark_id: int = None, id: int = None):
    bid = bookmark_id if bookmark_id is not None else id
    return db.query(Bookmark).filter(Bookmark.id == bid).first()

def get_bookmark_by_url(db: Session, url: str):
    return db.query(Bookmark).filter(Bookmark.url == url).first()

def get_bookmarks(db: Session, skip: int = 0, limit: int = 100, tag: str = None):
    q = db.query(Bookmark)
    if tag and hasattr(Bookmark, 'tags'):
        try:
            q = q.join(Bookmark.tags).filter(Tag.name == tag)
        except Exception:
            q = q.filter(Bookmark.tags.contains(tag))
    return q.offset(skip).limit(limit).all()

def get_bookmarks_by_tag(db: Session, tag: str, skip: int = 0, limit: int = 100):
    return get_bookmarks(db, skip=skip, limit=limit, tag=tag)

def create_bookmark(db: Session, bookmark):
    b_data = bookmark.model_dump() if hasattr(bookmark, 'dict') else bookmark.model_dump()
    raw_tags = b_data.pop('tags', []) or []
    db_obj = Bookmark(**b_data)
    if hasattr(db_obj, 'tags') and hasattr(db_obj.tags, 'append'):
        for t in raw_tags:
            t_name = t if isinstance(t, str) else str(t)
            db_obj.tags.append(Tag(name=t_name))
    elif hasattr(db_obj, 'tags'):
        db_obj.tags = ','.join(raw_tags) if isinstance(raw_tags, list) else str(raw_tags)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_bookmark(db: Session, bookmark_id: int = None, bookmark = None, id: int = None):
    bid = bookmark_id if bookmark_id is not None else id
    db_obj = get_bookmark(db, bid)
    if not db_obj:
        return None
    b_data = bookmark.model_dump(exclude_unset=True) if hasattr(bookmark, 'dict') else bookmark.model_dump(exclude_unset=True)
    raw_tags = b_data.pop('tags', None)
    for k, v in b_data.items():
        setattr(db_obj, k, v)
    if raw_tags is not None:
        if hasattr(db_obj, 'tags') and hasattr(db_obj.tags, 'clear'):
            db_obj.tags.clear()
            for t in raw_tags:
                db_obj.tags.append(Tag(name=str(t)))
        elif hasattr(db_obj, 'tags'):
            db_obj.tags = ','.join(raw_tags) if isinstance(raw_tags, list) else str(raw_tags)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_bookmark(db: Session, bookmark_id: int = None, id: int = None, url: str = None):
    bid = bookmark_id if bookmark_id is not None else id
    if bid is not None:
        db_obj = get_bookmark(db, bid)
    elif url:
        db_obj = get_bookmark_by_url(db, url)
    else:
        return None
    if not db_obj:
        return None
    tags_copy = [t.name for t in db_obj.tags] if hasattr(db_obj, 'tags') and isinstance(db_obj.tags, list) else []
    db.delete(db_obj)
    db.commit()
    db_obj.tags = tags_copy
    return db_obj
