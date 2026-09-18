# Q5. A customer enters their full name with extra spaces and inconsistent casing, e.g.
# "  raJEsh KUMAr  ". Clean this string to produce a properly formatted name: "Rajesh Kumar".

name = "  raJEsh KUMar  "
print (name)
b = name.lstrip().title().rstrip()
print(b)