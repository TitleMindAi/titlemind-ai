
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return JSONResponse(content={
        "message": "File received",
        "filename": file.filename,
        "extracted_fields": {
            "GRANTOR": "John Doe",
            "GRANTEE": "ABC Oil Co.",
            "INSTRUMENT TYPE": "Warranty Deed",
            "VOLUME": "123",
            "PAGE": "456"
        }
    })
