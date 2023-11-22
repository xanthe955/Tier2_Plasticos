from fastapi import FastAPI, Request
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Configura la conexión fuera de la función
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tier1"
)

cursor = conn.cursor()

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
    # Configura la conexión y crea un cursor dentro de la función

    try:
        # Resto del código de la función
        # ...
        print('Datos recibidos desde api.py:')
        print(f"Cameras: {update_data.cameras}")
        print(f"Biometric Sensors: {update_data.biometric_sensors}")
        print(f"Baseband: {update_data.baseband}")
        print(f"Power Management: {update_data.power_management}")
        print(f"Processor: {update_data.processor}")
        print(f"NAND: {update_data.nand}")
        print(f"DRAM: {update_data.dram}")
        print(f"Accelerometer: {update_data.accelerometer}")
        print(f"Battery: {update_data.battery}")
        print(f"Microphone: {update_data.microphone}")
        print(f"Speakers: {update_data.speakers}")
        # Realiza las actualizaciones
        update_query = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.cameras} WHERE name = 'Cameras'"
        cursor.execute(update_query)
        update_query1 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.biometric_sensors} WHERE name = 'Biometric Sensors'"
        cursor.execute(update_query1)
        update_query2 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.baseband} WHERE name = 'Baseband'"
        cursor.execute(update_query2)
        update_query3 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.power_management} WHERE name = 'Power Management'"
        cursor.execute(update_query3)
        update_query4 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.processor} WHERE name = 'Processor'"
        cursor.execute(update_query4)
        update_query5 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.nand} WHERE name = 'NAND'"
        cursor.execute(update_query5)
        update_query6 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.dram} WHERE name = 'DRAM'"
        cursor.execute(update_query6)
        update_query7 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.accelerometer} WHERE name = 'Accelerometer'"
        cursor.execute(update_query7)
        update_query8 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.battery} WHERE name = 'Battery'"
        cursor.execute(update_query8)
        update_query9 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.microphone} WHERE name = 'Microphone'"
        cursor.execute(update_query9)
        update_query10 = f"UPDATE tier1.raw_materials SET stock = stock + {update_data.speakers} WHERE name = 'Speakers'"
        cursor.execute(update_query10)
        # Resto de las actualizaciones

        # Confirma los cambios
        conn.commit()
    finally:
        # Cierra la conexión y el cursor en un bloque finally
        cursor.close()
        conn.close()

    return {"mensaje": "Cantidades actualizadas correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
