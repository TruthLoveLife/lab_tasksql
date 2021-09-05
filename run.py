import uvicorn
from fastapi import FastAPI
from fastsql import app01, app02

app = FastAPI(
    title='FastAPI Tutorial and Coronavirus Tracker API Docs',
    description='调用数据库接口，分别用连表查询，使用存储系统，触发器，索引，视图',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
    )

app.include_router(app01, prefix='/fastsql', tags=['村里信息调查'])
app.include_router(app02, prefix='/fastsql', tags=['模拟订单过程'])

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)