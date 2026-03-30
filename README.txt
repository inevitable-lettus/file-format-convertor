File Format convertor
    A program which helps convert file formats locally - efficiently and safely. 

Formats to convert: 
    JPG <--> PNG
    mp3 <--> mp4
    DOCX <--> PDF

STRUCTURE OF PROGRAM 

file-format-convertor/
├── main.py                   ← app instance, CORS, router registration, lifespan
├── routers/
│   ├── images.py             ← HTTP: receive file, call converter, return response
│   ├── documents.py
│   ├── videos.py
│   └── audio.py
├── converters/
│   ├── image_converter.py    ← Logic: Pillow calls, format handling
│   ├── document_converter.py
│   ├── video_converter.py
│   └── audio_converter.py
├── temp/                     ← Scratch space for in-progress files
├── requirements.txt
└── README.md

Running the application: 
        
        uvicorn main:app --reload

