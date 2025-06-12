from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from CreditCard import CreditCard
import logging

app = FastAPI()
credit_card_service = CreditCard()

@app.get("/validateFlag/{creditCardNumber}")
async def validate_flag(creditCardNumber: str):
    """
    REST API endpoint to validate credit card flag.
    Calls CreditCard.validateFlag and returns the result.
    Handles exceptions and returns 500 on error.
    """
    try:
        result = credit_card_service.validateFlag(creditCardNumber)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        logging.exception("Internal server error")
        raise HTTPException(status_code=500, detail="Internal server error")