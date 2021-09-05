import shortuuid
import time
from fastapi import APIRouter, Depends, HTTPException
from fastsql import CRUD, schemas
app02 = APIRouter()


# @app02.post("/create_order")
# def factory_order(infor:schemas.CreateOrder):
#     s = time.strftime("%Y%m%d", time.localtime())
#     su = shortuuid.ShortUUID(alphabet="0123456789")
#     nid = su.random(length=3)
#     facid = s+nid
#     CRUD.factory_order(facid,infor.name,infor.table,infor.stool,infor.bed,infor.cabinet,
#                               infor.computer_table,infor.phone)
#     return CRUD.search_s_number("ftable", infor.stool)


@app02.post("/create_order")
def factory_order(infor:schemas.CreateOrder):
    stockname, stockcharinfor = [],[]
    stock_number = CRUD.stock_number()
    for val in stock_number[0].values():
        stockname.append(val)
    if stockname[1] < int(infor.table):
        return1 = "桌子还剩下%s，请重新输入" %stockname[1]
        stockcharinfor.append(return1)
    if stockname[2] < int(infor.stool):
        return2 = "凳子库存不足，还剩下%s 请重新输入"%stockname[2]
        stockcharinfor.append(return2)
    if stockname[3] < int(infor.bed):
        return3 = "床库存不足，还剩下%s 请重新输入"%stockname[3]
        stockcharinfor.append(return3)
    if stockname[4] < int(infor.cabinet):
        return4 = "柜子库存不足，还剩下%s 请重新输入"%stockname[4]
        stockcharinfor.append(return4)
    if stockname[5] < int(infor.computer_table):
        return5 = "电脑桌库存不足，还剩下%s 请重新输入"%stockname[5]
        stockcharinfor.append(return5)
    else:
        pass
    if stockcharinfor:
        return stockcharinfor[:]
    else:
        s = time.strftime("%Y%m%d", time.localtime())
        su = shortuuid.ShortUUID(alphabet="0123456789")
        nid = su.random(length=3)
        facid = s + nid
        return CRUD.factory_order(facid, infor.name, infor.table, infor.stool, infor.bed, infor.cabinet,
                           infor.computer_table, infor.phone)


@app02.post("/return_goods")
def factory_return(infor:schemas.CreateOrder):
    s = time.strftime("%Y%m%d", time.localtime())
    su = shortuuid.ShortUUID(alphabet="0123456789")
    nid = su.random(length=3)
    facid = s + nid
    return CRUD.factory_return(facid, infor.name, infor.table, infor.stool, infor.bed, infor.cabinet,
                              infor.computer_table, infor.phone)