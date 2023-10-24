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