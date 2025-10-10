a = 12 #int
b = 12.3334 #float
c = True #bool
d = "s" #str
e = [12, 4, True, "ddd", b]#list
f = (12, 4)#tuple
o = {
    1 : "a",
    2 : "b",
    3 : "text"
}#dict


def func1(a, b):
    return (a+b)*(a-b)


class lolitclass:
    def __init__(self, a, b):
        self.a = a
        self.b =b
        
obj = lolitclass("str", b)


print(type(a), type(b), type(c), type(d),type(e), type(f), type(func1), type(lolitclass), type(obj), type(o))#types
print(obj.a, obj.b)#class_obj
print(func1(12, 3))#func
print(o[1], o[2], o[3])# dict
print(a !=b, c == d)#bool