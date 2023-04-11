# some_list = [1,2,3,4,5]
# new_list = []
# new_list_2 = [item for item in some_list if item > 3 or item ]
# for item in some_list:
#     if item > 3:
#         new_list.append(item)
#
# print(new_list_2)
# print(new_list)
def add_footer_header(sign, quantity):
    def middlevel(func):
        def inner(msg):
            print(sign)
            print(quantity)
            return f"{sign*quantity}{func(msg)}{sign*quantity}"
        return inner
    return middlevel


@add_footer_header("?",20)
def hi(msg):
    return msg

print(hi("Hello"))