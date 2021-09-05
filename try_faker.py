import time
from fastsql import CRUD
from faker import Faker
fake = Faker("zh_CN")
for _ in range(1500):
    CRUD.fake_shuju(fake.name(), fake.job(), fake.company(), fake.address(), fake.phone_number(),
             fake.date_time(tzinfo=None))




# stockname = []
# stock_number = CRUD.stock_number()
# for val in stock_number[0].values():
#     stockname.append(val)
# print(stockname)
