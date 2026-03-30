from fastapi import APIRouter, UploadFile, File, Query, HTTPException, BackgroundTasks
import uuid 
import shutil
from pathlib import Path
import os

router = APIRouter()

@router.post("/convert")
async def convert_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...), 
    to: str = Query(..., regex="^(jpg|png)$")
):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files allowed")
    
    if not file.filename:
        raise HTTPException(status_code=400, detail="File must have a name")
    
    temp_dir = Path("temp") #saved to temp
    unique_id = uuid.uuid4().hex
    original_suffix = Path(file.filename).suffix

    content_type_map = {
        "image/jpeg": "jpg",
        "image/png": "png",
    }
    input_suffix = content_type_map.get(file.content_type)
    
    input_path = temp_dir / f"{unique_id}{input_suffix}"
    output_path = temp_dir / f"{unique_id}.{to}"

    if not input_suffix:
        raise HTTPException(status_code =400, detail="Unsupported image format")
    
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    from converters.image_converter import convert_image as run_conversion
    run_conversion(input_path, output_path)

    from fastapi.responses import FileResponse

    background_tasks.add_task(os.remove, input_path)
    background_tasks.add_task(os.remove, output_path)

    return FileResponse(
        path=output_path,
        media_type=f"image/{to}",
        filename = f"onverted.{to}",
        background=background_tasks

    )


