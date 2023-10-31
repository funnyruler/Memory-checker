import uvicorn
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette import status
from starlette.responses import Response


load_dotenv()
host, port = os.getenv('API_HOST'), int(os.getenv('API_PORT'))
app = FastAPI()


@app.post("/alarm")
async def alarm():
    return Response(status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    uvicorn.run("api:app", host=host, port=port, reload=True)