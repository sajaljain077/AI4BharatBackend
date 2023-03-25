from fastapi import FastAPI, APIRouter
from database.database_connection import engine
from database import schema
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from utils.utils import responseModel
from utils.api_register import api_router



app = FastAPI(
    title="Indian Language Conversion Dataset Creation",
)



@app.get("/")
async def root():
    return {"message": "Hello World! This is the dataset collection project"}

@app.get("/health")
async def healthCheck():
    return {"message": "ok"}

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(exc.errors())
    inputValidationError = []
    if exc.errors()[0]['type'] == 'value_error.jsondecode':
        inputValidationError.append("INVALID_INPUT_JSON")
    elif exc.errors()[0]['type'] == 'value_error.missing':
        if exc.errors()[0]['loc'][0] == 'body':
            if len(exc.errors()) == 1 and len(exc.errors()[0]['loc']) == 1:
                inputValidationError.append( "WHOEL_BOSY_IS_MISSING")
            else:
                for i in exc.errors():
                    inputValidationError.append(f"MISSING_JSON_PARAMETER {i['loc'][-1]}")
        elif exc.errors()[0]['loc'][0] == 'query':
            if len(exc.errors()) == 1 and len(exc.errors()[0]['loc']) == 1:
                inputValidationError.append("WHOLE BODY IS MISSING")
            else:
                for i in exc.errors():
                    inputValidationError.append(f"Follwing parameter was missing from query {i['loc'][-1]}")
    else:
        if len(exc.errors()) == 1 and len(exc.errors()[0]['loc']) == 1:
            inputValidationError.append("WHOLE BODY IS MISSING")
        else:
            for i in exc.errors():
                inputValidationError.append(f"Following query paramter was missing {i['loc'][-1]}")

    return responseModel(400, data={}, errors=inputValidationError)

app.include_router(api_router, prefix="/api/v1")
schema.Base.metadata.create_all(engine)