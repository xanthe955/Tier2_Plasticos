from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, Session

import requests 

app = FastAPI()
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


#Conector a la base de datos 
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/tier1"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

#Obtener tabla de materiales 
raw_materials = Table(
    "raw_materials",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("description", String, index=True),
    Column("props", String, index=True),
    Column("stock", Integer, index=True),
    Column("enabled", Integer, index=True),
)

#Clase para sacar los datos de "Solicitudes"
solicitudes = Table(
    "solicitudes",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("carcasa_color_azul", Integer, index=True),
    Column("carcasa_color_verde", Integer, index=True),
    Column("carcasa_color_amarillo", Integer, index=True),
    Column("carcasa_color_morado", Integer, index=True),
    Column("carcasa_color_rosa", Integer, index=True),
    Column("carcasa_color_cyan", Integer, index=True),
)

Base = declarative_base()

#Clase para sacar los datos de "Raw materials"
class Material(Base):
    __tablename__ = "raw_materials"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    props = Column(String, index=True)
    stock = Column(Integer, index=True)
    enabled = Column(Integer, index=True)
    
    
#Clase para sacar los datos de "Solicitudes"
class Solicitud(Base):
    __tablename__ = "solicitudes"
    id = Column(Integer, primary_key=True, index=True)
    carcasa_color_azul = Column(Integer, index=True)
    carcasa_color_verde = Column(Integer, index=True)
    carcasa_color_amarillo = Column(Integer, index=True)
    carcasa_color_morado = Column(Integer, index=True)
    carcasa_color_rosa = Column(Integer, index=True)
    carcasa_color_cyan = Column(Integer, index=True)
    
Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def index():
    with open("templates/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/clientrequest", response_class=HTMLResponse)
def clientrequest(request: Request):
    with open("templates/clientrequest.html", "r") as file:
        html_content = file.read()
    # Realizar la consulta a la base de datos
    db = Session(engine)
    datos = db.query(Solicitud).all()
    db.close()
    return templates.TemplateResponse(
        "clientrequest.html", {"request": request, "datos": datos}
    )

@app.get("/clientship", response_class=HTMLResponse)
def clientship():
    with open("templates/clientship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/clientsell", response_class=HTMLResponse)
def clientsell():
    with open("templates/clientsell.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2peship", response_class=HTMLResponse)
def t2peship():
    with open("templates/t2peship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pesell", response_class=HTMLResponse)
def t2pesell():
    with open("templates/t2pesell.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)



@app.get("/warehouse", response_class=HTMLResponse)
def t2pewarehouse(request: Request):
    with open("templates/warehouse.html", "r") as file:
        html_content = file.read()

    # Realizar la consulta a la base de datos
    db = Session(engine)
    datos = db.query(Material).all()
    db.close()

    return templates.TemplateResponse(
        "warehouse.html", {"request": request, "datos": datos}
    )


@app.get("/t2pcship", response_class=HTMLResponse)
def t2pcship():
    with open("templates/t2pcship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/t2pcsell", response_class=HTMLResponse)
def t2pcsell():
    with open("templates/t2pcsell.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get("/logship", response_class=HTMLResponse)
def logship():
    with open("templates/logship.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


##################################################################################################################


class UpdateQuantity(BaseModel):
    cameras: int = 0
    biometric_sensors: int = 0
    baseband: int = 0
    power_management: int = 0
    processor: int = 0
    nand: int = 0
    dram: int = 0
    accelerometer: int = 0
    battery: int = 0
    microphone: int = 0
    speakers: int = 0


@app.post("/update-quantities")
def update_quantities(request: Request, update_data: UpdateQuantity):
    data = {
        "cameras": update_data.cameras,
        "biometric_sensors": update_data.biometric_sensors,
        "baseband": update_data.baseband,
        "power_management": update_data.power_management,
        "processor": update_data.processor,
        "nand": update_data.nand,
        "dram": update_data.dram,
        "accelerometer": update_data.accelerometer,
        "battery": update_data.battery,
        "microphone": update_data.microphone,
        "speakers": update_data.speakers,
    }

    main_api_url = "http://localhost:8001/update-quantities"

    response = requests.post(main_api_url, json=data)

    if response.status_code == 200:
        print("Datos enviados con éxito a main.py")
    else:
        print("Error al enviar datos a main.py")


##################################################################################################################


class UpdatePlasticParts(BaseModel):
    carcasa_color_azul: int = 0
    carcasa_color_verde: int = 0
    carcasa_color_amarillo: int = 0
    carcasa_color_morado: int = 0
    carcasa_color_rosa: int = 0
    carcasa_color_cyan: int = 0
    # Agrega más colores según sea necesario


@app.post("/update-plastic-parts")
def update_plastic_parts(request: Request, update_data: UpdatePlasticParts):
    data = {
        "carcasa_color_azul": update_data.carcasa_color_azul,
        "carcasa_color_verde": update_data.carcasa_color_verde,
        "carcasa_color_amarillo": update_data.carcasa_color_amarillo,
        "carcasa_color_morado": update_data.carcasa_color_morado,
        "carcasa_color_rosa": update_data.carcasa_color_rosa,
        "carcasa_color_cyan": update_data.carcasa_color_cyan,
        # Agrega más colores según sea necesario
    }

    main_api_url = "http://localhost:8002/update-plastic-parts"

    response = requests.post(main_api_url, json=data)

    if response.status_code == 200:
        return {"message": "Datos enviados con éxito a main.py en el puerto 8002"}
    else:
        return {"error": "Error al enviar datos a main.py en el puerto 8002"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
