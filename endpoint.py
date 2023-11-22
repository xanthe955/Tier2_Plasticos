from fastapi import FastAPI, Request
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/tier1"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class PlasticPart(Base):
    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True, index=True)
    carcasa_color_azul = Column(Integer, default=0)
    carcasa_color_verde = Column(Integer, default=0)
    carcasa_color_amarillo = Column(Integer, default=0)
    carcasa_color_morado = Column(Integer, default=0)
    carcasa_color_rosa = Column(Integer, default=0)
    carcasa_color_cyan = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)
app = FastAPI()

class UpdatePlasticParts(BaseModel):
    carcasa_color_azul: int = 0
    carcasa_color_verde: int = 0
    carcasa_color_amarillo: int = 0
    carcasa_color_morado: int = 0
    carcasa_color_rosa: int = 0
    carcasa_color_cyan: int = 0

@app.post("/update-plastic-parts")
def update_plastic_parts(request: Request, update_data: UpdatePlasticParts):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        plastic_part = PlasticPart(
            carcasa_color_azul=update_data.carcasa_color_azul,
            carcasa_color_verde=update_data.carcasa_color_verde,
            carcasa_color_amarillo=update_data.carcasa_color_amarillo,
            carcasa_color_morado=update_data.carcasa_color_morado,
            carcasa_color_rosa=update_data.carcasa_color_rosa,
            carcasa_color_cyan=update_data.carcasa_color_cyan,
        )

        db.add(plastic_part)
        db.commit()
        db.refresh(plastic_part)

        print('Datos recibidos desde api.py (Piezas Plásticas):')
        print(f"Carcasa Color Ázul: {update_data.carcasa_color_azul}")
        print(f"Carcasa Color Verde: {update_data.carcasa_color_verde}")
        print(f"Carcasa Color Amarillo: {update_data.carcasa_color_amarillo}")
        print(f"Carcasa Color Morado: {update_data.carcasa_color_morado}")
        print(f"Carcasa Color Rosa: {update_data.carcasa_color_rosa}")
        print(f"Carcasa Color Cyan: {update_data.carcasa_color_cyan}")

        return {"mensaje": "Cantidades de piezas plásticas actualizadas correctamente"}
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
