from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db.database import reservas, configure, users, personal as db_personal
from datetime import datetime
from bson import ObjectId
from typing import Optional
from config.config import conf

router = APIRouter(prefix="/config")

from datetime import datetime
import numba as nb

class middleware_struct(BaseModel):
    token_id: Optional[str] = None
    token_data: Optional[str] = None


'''
Porque no se usa el parametro data en las rutas?

- Simplemente es para que se pueda ver las variables a usar en la documentación

'''

@router.post('/reset_password')
async def root(request: Request, data: middleware_struct) -> JSONResponse:

    '''
    Enseña las reservas que hizo el **usuario**
    '''
    def code() -> dict:

        try:
            user_id = str(request.state.user_id)
            appointments = users.find_one({ "_id": ObjectId(user_id) }, {'_id': 0, 'reservas': 1})
            print('appointments ->', appointments)

        except Exception as e:
            return Response({
                "info": "Hubo un error a la base de datos",
                "status": "no",
                "type": "DATABASE_ERROR"
            }, 401)
        
        if not appointments:
            return Response({
                "info": "No se encontro el usuario, o esta en el db vació",
                "status": "no",
                "type": "USER_NOT_FOUND"
            }, 200)

        # Convertir objetos datetime a cadenas de texto
        for _, reservas in appointments['reservas'].items():
            print('reservas---->', reservas)
            reservas["date_appointment"] = str(reservas["date_appointment"])

        return Response({
            "info": "Se obtuvo del usuario sus reservas",
            "status": "ok",
            "type": "SUCCESS",
            "data": appointments
        }, 200)



    try:
        def Response(res: dict, status: int) -> JSONResponse:
            res["renew"] = {
                "token": request.state.new_token
            }
            return JSONResponse(res, status)
        
        return code()
        
        

    except Exception as e:
        return JSONResponse({
            "info": f"Error desconocido por el servidor: {e}",
            "status": "no",
            "type": "UNKNOW_ERROR",
            "renew": {
                "token": request.state.new_token
            }
        }, 500)


