def string(a):
    if len(a)==0:
        return a
    else:
        return string(a[1:])+ a[0]
#a="josipa"
#print(string(a))
