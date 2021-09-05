import pymysql
import time
import json
taikang_time = time.strftime('%Y-%m-%d')

list_query_taikang = """
select 
	p.personid, p.name, p.sex, p.birthday
from
	person p  
join
	taikang t 
on
	p.name = t.name and t.logornot = 0;
	
"""


list_query_zhapian = """
select 
	p.personid, p.name, p.sex, p.birthday
from
	person p  
join
	antiscam a 
on
	p.name = a.name and a.logornot = 0;
"""

search_totle = """
select * from totle;
"""


def add(name, sex):
   return "insert into taikang(name, sex, logornot,zhucedate) value ("+"\""+name+"\""+","+"\""+sex+"\""+",1,"+"\""+taikang_time+"\""+");"


# 创建操作农村调查的类
class DataModel:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="1",
                               database="lab_task", charset="utf8",
                               cursorclass=pymysql.cursors.DictCursor
                               )
        self.cursor = self.conn.cursor()
#  删除和插入
    def test(self, sql_test):
        self.cursor.execute(sql_test)
        self.conn.commit()
        # result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        # return result

# 查询
    def test_query(self, sql_test):
        self.cursor.execute(sql_test)
        # self.conn.commit()
        result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return result

# 创建操作factory的类
class DataModel2:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="1",
                               database="try_factorydb", charset="utf8",
                               cursorclass=pymysql.cursors.DictCursor
                               )
        self.cursor = self.conn.cursor()
#  删除和插入
    def test(self, sql_test):
        self.cursor.execute(sql_test)
        self.conn.commit()
        # result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        # return result
# 关闭窗口
    def guanbi(self):
        self.cursor.close()
        self.conn.close()
# 不关闭窗口
    def test_query1(self, sql_test):
        self.cursor.execute(sql_test)
        # self.conn.commit()
        result = self.cursor.fetchall()
        #self.cursor.close()
        #self.conn.close()
        return result

# 查询
    def test_query(self, sql_test):
        self.cursor.execute(sql_test)
        # self.conn.commit()
        result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return result


# 查看没有注册云太康的信息
def test_query_taikang():
    query = DataModel()
    result = query.test(list_query_taikang)
    return result


# 查看没有注册防诈骗的信息
def test_query_zhapian():
    query = DataModel()
    result = query.test(list_query_zhapian)
    return result


def add_taikang(Insert_infor):
    Inert = DataModel()
    Inert.test(Insert_infor)


# 判断是否在数据库中
def judge_name(name):
    judge_infor = "SELECT DISTINCT IF(EXISTS(SELECT * FROM person WHERE NAME="+"\""+name+"\""+"),1,0) AS a FROM person;"
    judge = DataModel()
    result = judge.test_query(judge_infor)
    t = result[0]['a']
    return t


# 返回查询结果
def search(name):
    name_infor = "call search(" + "\"" +name+ "\""+");"
    Find = DataModel()
    return Find.test_query(name_infor)


# 返回totle的查询结果
def searchtotle():
    Search_Totle = DataModel()
    return Search_Totle.test_query(search_totle)

# 使用查询存储过程的函数
def use_procedure(procedure:str, Parameter:str):
    sql = "call "+procedure+"(" + Parameter +");"
    search_procedure = DataModel()
    return search_procedure.test_query(sql)


# 使用插入存储过程的函数
# def use_insert_procedure(procedure: str, personid: int, name: str, sex: str, minzu: str, birthday:str, huzhu:int, age:int):
#     sql = "call "+procedure+"(" + "\"" + personid +"\"" +","+ name +","+ sex + "," + minzu + "," + birthday + "," + "\""+ huzhu+"\""+","
#     +"\""+age+"\""+");"
#     search_procedure = DataModel()
#     return search_procedure.test(sql)
# 使用插入存储过程的函数
def use_insert_procedure(procedure: str, personid, name: str, sex: str, minzu: str, birthday:str, huzhu, age):
    sql = "call "+ procedure+"(" + personid +","+"\""+ name + "\"" +","+"\""+ sex +  "\""+ "," +"\""+ minzu +"\""+ "," +"\""+ birthday +"\""+ "," +  huzhu+"," + age +");"
    print(sql)
    search_procedure = DataModel()
    search_procedure.test(sql)
    return "插入成功！"


# 删除函数
def try_delete_infor(procedure: str, infor:str):
    sql = "call " + procedure+ "(" + infor +");"
    search_procedure = DataModel()
    return search_procedure.test(sql)


# 更新函数
def try_update_infor(procedure: str, infor:str):
    sql = "call " + procedure + "(" + infor + ");"
    search_procedure = DataModel()
    search_procedure.test(sql)
    return "更改成功"

# 更新出生日期，并且更改年龄
def try_birth_infor(name:str,infor:str):
    sql = "call alter_birthday("+"\""+name+"\""+","+"\""+infor+"\""+");"
    search_procedure = DataModel()
    search_procedure.test(sql)
    return "修改年龄成功！"


#  创建虚拟数据
def fake_shuju(inname,injob,incompany,inaddress,inphone_number,indatetime):
    sql = "insert into fake_shuju(name,job,company,address,phone_number,datetime) values('%s','%s','%s','%s','%s','%s');"%(inname,injob,incompany,inaddress,inphone_number,indatetime)
    print(sql)
    insert_procedure = DataModel()
    insert_procedure.test(sql)

# 对fake数据库进行操作
def operation_nshuju(infor:str):
    print(infor)
    sql = "select * from fake_shuju where name like '%s%%';"%infor
    select_procedure = DataModel()
    return select_procedure.test_query(sql)

def operation_job_shuju(infor:str):
    sql = "select * from fake_shuju where job like '%%%s%%';"%infor
    print(sql)
    select_procedure = DataModel()
    return select_procedure.test_query(sql)

# ###########################对factory的操作#########################
def factory_order(inorder_id:str,inname:str,intable,instoll,inbed,
                  incabinet,incomputer_table,inphone:str):
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # sql1 = "insert into person_id(order_id,name,phone,order_condition,date) " \
    #       "values ("+ "\""+inorder_id+"\""+","+ "\""+inname+"\""+","+"\""+inphone+"\""+","+"\""+"已订购"+"\""+ ","+"\""+time1+"\""+");"
    sql1 = "insert into person_id(order_id,name,phone,order_condition,date) values ('%s','%s','%s','%s','%s');"%(inorder_id,inname,inphone,"已订购",time1)

    # sql2 = "insert into order_infor(order_id,name,ftable,stool,bed,cabinet,computer_table,order_time,order_condition) "+"values("+"\""+inorder_id+"\""+","+ "\""+inname+"\""+","+"\""+intable+"\""+","+"\""+ instoll+"\"" + ","+"\""+inbed+"\""+","+"\""+incabinet+"\""+","+"\""+incomputer_table+"\""+","+"\""+time1+"\""+","+"\""+"订购"+"\""+");"
    sql2 = "insert into order_infor(order_id,name,ftable,stool,bed,cabinet,computer_table,order_time,order_condition) values('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(inorder_id,inname,intable,instoll,inbed,incabinet,incomputer_table,time1,"订购")
    # sql2 = "insert into order_infor(order_id,name,table,stool,bed,cabinet,computer_table,order_time,order_condition) " + "values(" + "\"" + inorder_id + "\"" + "," + "\"" + inname + "\"" + "," + " intable , instoll, inbed , incabinet , incomputer_table," + "\"" + time1 + "\"" + "," + "\"" + "已订购" + "\"" + ");"
    create_procedure1 = DataModel2()
    create_procedure1.test(sql1)
    create_procedure2 = DataModel2()
    create_procedure2.test(sql2)
    return "插入成功！"

# 插入之后再进行查询，暂时不用
def search_s_number(stable: str,number:str):
    sql = "call test_func('%s',@res);"%stable
    sql2 = "select @res;"
    search_stock_number = DataModel2()
    search_stock_number.test_query1(sql)
    s = search_stock_number.test_query1(sql2)
    if s[0]['@res'] < 0:
        sql3 = "update stock set %s = %s +%s;" %(stable, stable, number)
        update_stock_number = DataModel2()
        update_stock_number.test(sql3)
        return "%s库存不足，请重新输入"%stable
    else:
        return "插入成功！"


# def search_s_number(stable: strr):
#     sql = "call test_func('%s',@res);"%stable
#     sql2 = "select @res;"
#     search_stock_number = DataModel2()
#     search_stock_number.test_query1(sql)
#     s = search_stock_number.test_query1(sql2)
#     return s[0]['@res']




# 对stock进行查找功能
def stock_number():
    sql = "select * from stock;"
    search_stock_number = DataModel2()
    return search_stock_number.test_query(sql)



#**************************************用户退货************************

def factory_return(inorder_id:str,inname:str,intable,instoll,inbed,
                  incabinet,incomputer_table,inphone:str):
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql1 = "insert into person_id(order_id,name,phone,order_condition,date) " \
          "values ("+ "\""+inorder_id+"\""+","+ "\""+inname+"\""+","+"\""+inphone+"\""+","+"\""+"已退货"+"\""+ ","+"\""+time1+"\""+");"

    sql2 = "insert into order_infor(order_id,name,ftable,stool,bed,cabinet,computer_table,order_time,order_condition) "+"values("+"\""+inorder_id+"\""+","+ "\""+inname+"\""+","+"\""+intable+"\""+","+"\""+ instoll+"\"" + ","+"\""+inbed+"\""+","+"\""+incabinet+"\""+","+"\""+incomputer_table+"\""+","+"\""+time1+"\""+","+"\""+"退货"+"\""+");"
    # sql2 = "insert into order_infor(order_id,name,table,stool,bed,cabinet,computer_table,order_time,order_condition) " + "values(" + "\"" + inorder_id + "\"" + "," + "\"" + inname + "\"" + "," + " intable , instoll, inbed , incabinet , incomputer_table," + "\"" + time1 + "\"" + "," + "\"" + "已订购" + "\"" + ");"
    print(sql2)
    create_procedure1 = DataModel2()
    create_procedure1.test(sql1)
    create_procedure2 = DataModel2()
    create_procedure2.test(sql2)
    return "退货成功！"




