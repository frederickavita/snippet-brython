# -*- coding: utf-8 -*-

#test

listing = [   
]


for v in listing:
    name = "\"" + v + ' brython' + "\"" 
    name_low = "\"" + v.lower() + "\"" 
    name_min = "\"" + v + "\"" 
    r = name +  ":" + "{" +  '"prefix"' + ":" +\
           name_low  + "," + '"body"' +\
        ":" + "[" + name_min  + "]," +\
        '"description"' + ":" + name_min + "},"
    print(r)    

