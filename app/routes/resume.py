from fastapi import APIRouter, UploadFile
import shutil

from ..resume_parser import parse_resume

router = APIRouter()


@router.post("/resume")
async def upload_resume(file: UploadFile):
    path = f"data/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = parse_resume(path)
    return {"parsed": True, "length": len(text)}
