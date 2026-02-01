from fastapi import APIRouter

router = APIRouter()


@router.post("/apply/{job_id}")
def apply(job_id: int):
    return {
        "job_id": job_id,
        "status": "Apply-Assist ready",
        "message": "Open link, upload resume, paste cover letter",
    }
