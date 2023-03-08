from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from myself_as_a_site.const import HUGO_RESOURCE_FOLDER


app = FastAPI()

app.mount(
   "/static",
   StaticFiles(
   directory=f"{HUGO_RESOURCE_FOLDER}/public"),
   name="static"
)

templates = Jinja2Templates(
   directory=f"{HUGO_RESOURCE_FOLDER}/public/templates"
)


@app.get('/')
def root():
   return RedirectResponse('/short-links/')


@app.get('/short-links/', response_class=HTMLResponse)
def short_links(request: Request):
   return templates.TemplateResponse(
      name='index.html',
      context={'request': request},
   )


@app.exception_handler(404)
async def http_exception_handler(request, exc):
   return RedirectResponse('/short-links/', status_code=300)
 