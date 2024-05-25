# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/users/')
def create_user(linkedin_id: str, db: Session = Depends(get_db)):
    user = models.User(linkedin_id=linkedin_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"user_id": user.linkedin_id}

@app.post('/posts/')
def create_post(linkedin_id: str, post_id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.linkedin_id == linkedin_id).first()
    if user:
        post = models.Post(post_id=post_id, user_id=linkedin_id)
        db.add(post)
        db.commit()
        db.refresh(post)
        return {"post_id": post.post_id}
    return {"error": "User not found"}

@app.post('/likers/')
def create_liker(post_id: str, liker_id: str, name: str, title: str = None, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    if post:
        liker = models.Liker(liker_id=liker_id, name=name, title=title, post_id=post_id)
        db.add(liker)
        db.commit()
        db.refresh(liker)
        return {"liker_id": liker.liker_id, "name": liker.name, "title": liker.title}
    return {"error": "Post not found"}

@app.get('/activity/{linkedin_id}')
def get_activity(linkedin_id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.linkedin_id == linkedin_id).first()
    if user:
        activity = []
        for post in user.posts:
            likers = [{"liker_id": liker.liker_id, "name": liker.name, "title": liker.title} for liker in post.likers]
            activity.append({"post_id": post.post_id, "likers": likers})
        return activity
    return {"error": "User not found"}