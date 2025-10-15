# app/utils/response_utils.py
from fastapi.responses import JSONResponse
from fastapi import status

def success_response(data, message="Success"):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "message": message, "data": data}
    )

def error_response(message="Error", code=status.HTTP_400_BAD_REQUEST):
    return JSONResponse(
        status_code=code,
        content={"status": "error", "message": message}
    )
