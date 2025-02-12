myfamily = {
  "child1" : {
    "name" : "Nurik",
    "year" : 2015
  },
  "child2" : {
    "Me" : "beka",
    "year" : 2007
  },
  "child3" : {
    "name" : "Bakdaulet",
    "year" : 2006
  },
  "child4" : {
    "name" : "Gulya",
    "year" : 2001
  },
  "child5" : {
    "name" : "Bakos",
    "year" : 2000
  }
}

for child, details in myfamily.items():
    print(f"{child}: {details}")