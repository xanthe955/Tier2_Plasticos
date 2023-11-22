from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

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
    print('Datos recibidos desde api.py (Piezas Plásticas):')
    print(f"Carcasa Color Ázul: {update_data.carcasa_color_azul}")
    print(f"Carcasa Color Verde: {update_data.carcasa_color_verde}")
    print(f"Carcasa Color Amarillo: {update_data.carcasa_color_amarillo}")
    print(f"Carcasa Color Morado: {update_data.carcasa_color_morado}")
    print(f"Carcasa Color Rosa: {update_data.carcasa_color_rosa}")
    print(f"Carcasa Color Cyan: {update_data.carcasa_color_cyan}")
    # Agrega más colores según sea necesario
    return {"mensaje": "Cantidades de piezas plásticas actualizadas correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
