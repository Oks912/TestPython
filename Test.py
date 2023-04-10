# # new_list = [1, "test"]
# # a = 2
# #
# #
# # #
# # # for el in new_list:
# # #     try:
# # #         assert el == 1
# # #         print(el + a)
# # #     except TypeError:
# # #         print('error')
# # #     except AssertionError:
# # #         print("an other error")
# #
# # def error_check(i):
# #     try:
# #         assert i == 1
# #         print(i + a)
# #     except TypeError:
# #         print("that was error")
# #     except AssertionError:
# #         print("another error")
# #
# #
# # for i in new_list:
# #     error_check(i)
#
#
# #with open("testy.txt","r") as f:
# #    f.read()
#
import time
import datetime
#
#
# def get_range():
#     # return[ item for item in range(1000)]


# def get_range():
#     a =[]
#     for i in range(1000):
#         a.append(i)
#
#
# start = time.time()
# get_range()
# end = time.time()
#
# print(end-start)


# def get_range():
#     time.sleep(5)
#     return [1,2,3]
#
#
# start = time.time()
# print(get_range())
# get_range()
# end = time.time()
#
# print(end-start)

# print(datetime.date(year=2023, month=3, day=30))
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())




import datetime

date1 = datetime.datetime(year=1980, month=12, day=23, hour=22, minute=34)
date2 = datetime.datetime(year=1980, month=12, day=23, hour=22, minute=25)

print(date1-mdate2)

delta1 = datetime.timedelta(minutes=5)
if date1 - date2> delta1:
     print("not bliznec")
else:
    print("brother or sister")