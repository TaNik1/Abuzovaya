from fastapi import FastAPI, Depends
from DataBase.database import SessionLocal
from DataBase.models import Item
from sqlalchemy.orm import Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/{id}")
async def read_item(id: int, db: Session = Depends(get_db)):
    new_item = Item(value=id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"id": new_item.id, "value": new_item.onewin_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
