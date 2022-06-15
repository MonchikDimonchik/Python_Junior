# def bar(x):
#     return str(x+x)
#
# bar(4).isdigit()
#
# a = bar(4)
# print(a.isdigit())
#
#
# a = chain_sum(4)
# a()
#
# a = bar(4)
# c = a()
# c()

#
# def bar(x=None):
#     if x is None:
#         return bar
#     else:
#         return x
#
# print(type(bar()))




def chain_sum(arg=None):
    def chain_sum(arg=None):
        if arg is not None:
            summa = summa + arg
            return chain_sum
        return summa

print(chain_sum(3)(5)() == 8)
print(chain_sum(3)() == 3)

