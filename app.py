from fastapi import FastAPI, Header, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model import base, models, schemas, service
from api import api

Session = base.SessionLocal()
app = FastAPI()
language = ["ko", "en", "ja", "tw"]

# 1. 회사명 자동완성
@app.get('/search')
def company_name_autocomplete(query: str = None, x_wanted_language: str = Header(None), session: Session = Depends(base.get_db)):
    try:
        if not headersLanguageCheck(x_wanted_language):
            raise HTTPException(status_code=400, detail="요청하신 언어는 존재하지 않습니다.")

        company = api._company_name_autocomplete(query, x_wanted_language, session, models)

        return JSONResponse(content = company)
    except MyError as e:
        return e

# 2. 회사 이름으로 회사 검색
@app.get('/companies/{company_name}')
def company_search(company_name: str = None, x_wanted_language: str = Header(None), session: Session = Depends(base.get_db)):
    try:
        if not headersLanguageCheck(x_wanted_language):
            raise HTTPException(status_code=400, detail="요청하신 언어가 존재하지 않습니다.")

        company = api._company_search(company_name, x_wanted_language, session, models)

        if company is None:
            raise HTTPException(status_code=404, detail="요청하신 회사가 존재하지 않습니다.")

        return JSONResponse(content = company)
    except MyError as e:
        return e

# 3. 새로운 회사 추가
@app.post('/companies')
async def new_company(req: Request, x_wanted_language: str = Header(None), session: Session = Depends(base.get_db)):
    req_json = await req.json()
    try:
        if not headersLanguageCheck(x_wanted_language):
            raise HTTPException(status_code=400, detail="요청하신 언어가 존재하지 않습니다.")

        company = api._new_company(req_json, x_wanted_language, session, models, service)

        return JSONResponse(content = company)
        # return JSONResponse(content = companyReturn(service.new_Company(session, db_company), x_wanted_language))

    except MyError as e:
        return e

def headersLanguageCheck(x_wanted_language):
    if x_wanted_language not in language:
        return False
    else:
        return True