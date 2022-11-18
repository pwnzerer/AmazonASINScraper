from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.responses import HTMLResponse
import requests
from asin_scraper import get_asin


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/',response_class=HTMLResponse)
async def root(request : Request):
    return templates.TemplateResponse('index.html',{"request": request})

@app.post('/',response_class=HTMLResponse)
async def get_form_data(request : Request,inputasin: str = Form(...)):
    product_details_list = get_asin(inputasin)
    return templates.TemplateResponse('index.html',{"request": request,"title": product_details_list[0],"totalstars": product_details_list[1],"total_reviews": product_details_list[2],"price": product_details_list[3],"prodimage": product_details_list[4]})