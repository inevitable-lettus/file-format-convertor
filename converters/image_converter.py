from pathlib import Path
from PIL import Image

def convert_image(input_path: Path, out_path: Path):
    
    with Image.open(input_path) as img:
        
        if out_path.suffix.lower() in {".jpg", ".jpeg"}: #If .jpg and RGBA, program will convert to jpg by flattening image on a white background
            if img.mode in ("RGBA", "LA") or ("transparency" in img.info):
                
                bg = Image.new("RGB", img.size, (255, 255, 255))
                bg.paste(img.convert("RGBA"), mask=img.convert("RGBA").split()[3])
                bg.save(out_path, "JPEG")

            else:
                # if .jpg and RGBA, convert to RGB and save.
                img.convert("RGB").save(out_path, "JPEG")
        
        elif out_path.suffix.lower() == ".png":
            img.save(out_path, "PNG") # if png, just save as png.