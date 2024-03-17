import os,sys;sys.path.append('./');

from mystring import frame

df = frame({'a':[1,2,3],'b':[4,5,6]})

print(df)

for row in df.roll:
    if row['b'] > 5:
        print("Setting")
        row['b'] = 0
        #row.b = 0
        print("set")

print(df)

from mystring import gh_url
simple = gh_url("https://github.com/franceme/mystring")

print(simple.core)

from mystring import backup_dir
core_dir = "backup"
dyr = backup_dir(core_dir)
def stub(*args, **kwargs):return [core_dir+"00000",core_dir+"00001",core_dir+"00002",core_dir+"00003",core_dir+"00004"]
dyr.__abs__ = lambda:stub()

print(dyr.__abs__())

print(dyr.__abs__()[-1])

print(dyr.__max__())

print(dyr.__max__().replace(dyr.core_dir, "").replace("_",""))

print(dyr.__pos__())

print(dyr.__neg__())

print("00004" in dyr)

print(dyr // 2)

print(dyr / 2)

#print(~dyr)

print(dyr.__enter__(0))

print(dyr.__enter__())
