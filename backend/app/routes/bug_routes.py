from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

router = APIRouter()


@router.post("/submit")

async def submit_bug(

        description: str = Form(...),

        file: UploadFile = File(None)

):

    uploaded_content = ""

    if file:

        uploaded_content = (

            await file.read()

        ).decode("utf-8")

    return {

        "description": description,

        "filename": file.filename if file else None,

        "preview": uploaded_content[:300]

    }