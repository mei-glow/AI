import time
from typing import Annotated, List

from fastapi import FastAPI, File, UploadFile, Request

app = FastAPI()
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(files: List[UploadFile]):
     return [
        {"filename": f.filename, "content_type": f.content_type}
        for f in files
    ]