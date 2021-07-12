from fastapi import FastAPI,UploadFile,File,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import trans_to_xls
from fastapi.templating import Jinja2Templates
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def root():
    return {"hello":"world"}
@app.post("/")
def transfer(data:dict):
    txt_path = data["filename"]
    save_path = txt_path[:txt_path.rfind('.')]+'.xls'
    # return {"txt_path":txt_path,"save_path":save_path}
    trans_to_xls.transfer(txt_path,save_path)
    return {"txt_path":txt_path,"save_path":save_path}
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
    














