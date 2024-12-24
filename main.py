from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - fastapi-coll-534294973cf54472a3373055c5275a2f',debug=False,docs_url='/stupefied-perlman-8780a87ac1d611ef96380242ac12000568/docs',openapi_url='/stupefied-perlman-8780a87ac1d611ef96380242ac12000568/openapi.json')

app.include_router(router, prefix='/stupefied-perlman-8780a87ac1d611ef96380242ac12000568/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()