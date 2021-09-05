from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastsql import CRUD, schemas
app01 = APIRouter()

# 查询未注册过的个人信息，1 代表未出册过云太康， 0 代表未注册过防诈骗
@app01.get("/getnumber/{number}")
def get_number(number: int):
    """查询未注册过的个人信息，1 代表未出册过云太康， 0 代表未注册过防诈骗"""
    if number == 1:
        return CRUD.test_query_taikang()
    elif number == 0:
        return CRUD.test_query_zhapian()
    else:
        raise HTTPException(status_code=400, detail="Input error")


# 使用触发器，注册云上太康，就会在totle表里面泰康字段加一
@app01.post("/creat_user")
def creat_taikang(user: schemas.CreatUser):
    # print(user.sex)
    taikang = CRUD.add(user.name, user.sex)
    CRUD.add_taikang(taikang)
    return CRUD.searchtotle()


@app01.get("/getname/{name}")
def get_name(name: str):
    if CRUD.judge_name(name):
        return CRUD.search(name)
    else:
        raise HTTPException(status_code=400, detail="can't find username")


def common_parameters_try(infor_int1: str):
    return {"返回值是": infor_int1}

@app01.post("/search_infor")
async def try_search_input(number1: int, infor_str: str):
    """按照数字进行选择应用
    输入1(int) age(int)：查询大于age的人的信息。******
    输入2(int) sex(str)：查询性别的人的信息。******
    输入3(int) app(str)：查询未注册app（antiscam,taikang,vaccine）的人的信息*****
    输入4(int) family(int): 查询家庭信息*****
    输入5(int) name(str): 查询name的全部信息*****
    输入6(int) name(str): 查询这个name的户主的信息*****
    """
    # if number1.
    if number1 == 1:
        return CRUD.use_procedure("search_up_age", infor_str)
    elif number1 == 2:
        return CRUD.use_procedure("search_sex", infor_str)
    elif number1 == 3:
        return CRUD.use_procedure("search_unregister_infor4", infor_str)
    elif number1 == 4:
        return CRUD.use_procedure("search_famliy_infor", infor_str)
    elif number1 == 5:
        return CRUD.use_procedure("search_name_infor", infor_str)
    elif number1 == 6:
        return CRUD.use_procedure("search_huzhu_infor", infor_str)
    else:
        return "输入错误，请重新输入！"


@app01.post("/insert_person_infor2")
async def try_insert_input(person_infor: schemas.InPerson_Mosel):
    """在person的表里面使用函数，增加一个人的信息"""
    return CRUD.use_insert_procedure("insert_person_name3",
                                     person_infor.personid,
                                     person_infor.name,
                                     person_infor.sex,
                                     person_infor.minzu,
                                     person_infor.birthday,
                                     person_infor.huzhu,
                                     person_infor.age)



@app01.post("/delete_infor")
async def delete_input(number2: int,infor2:str):
    """按照数字进行选择应用
    输入1(int) name(str)：删除为name的人的信息。******
    输入2(int) age(str)：删除为age的人的信息。******
    输入3(int) huzhu(str)：删除为huzhu的人的信息。******
    输入4(int) sex(str)：删除为sex的人的信息。******
    输入5(int) personid(str)：删除为id的人的信息。******
    """
    if number2 == 1:
        return CRUD.try_delete_infor("try_delete_name", infor2)
    elif number2 == 2:
        return CRUD.try_delete_infor("try_delete_age", infor2)
    elif number2 == 3:
        return CRUD.try_delete_infor("try_delete_huzhu", infor2)
    elif number2 == 4:
        return CRUD.try_delete_infor("try_delete_sex", infor2)
    elif number2 == 5:
        return CRUD.try_delete_infor("try_delete_personid", infor2)
    else:
        return "输入错误，请重新输入"


@app01.post("/alter_infor")
async def update_input(number3: int,infor3:str):
    """按照数字进行选择应用
        输入1(int) name(str)：更改注册太康的信息。******
        输入2(int) name(str)：更改打疫苗的信息。******
        输入3(int) name(str)：更改注册防诈骗的信息。******
    """
    if number3 == 1:
        return CRUD.try_update_infor("try_update_taikang", infor3)
    elif number3 == 2:
        return CRUD.try_update_infor("try_update_vaccine", infor3)
    elif number3 == 3:
        return CRUD.try_update_infor("try_update_antiscam", infor3)
    else:
        return "输入错误，请重新输入！"

# 修改生日，并且自动更改响应的年龄（使用触发器）
@app01.post("/alter_birthday")
def update_birth(name:str, infor4:str):
    CRUD.try_birth_infor(name, infor4)

# 对fake数据进行操作
@app01.post("/operation_fake")
def operation_fake(number:int, infor:str):
    """1： 代表的是查询姓氏。**********2: 查询职业"""
    if number == 1:
        print(infor)
        return CRUD.operation_nshuju(infor)
    elif number == 2:
        return CRUD.operation_job_shuju(infor)
    else:
        return "输入错误！"