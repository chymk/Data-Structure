from collections import defaultdict

d = defaultdict(list)
d["a"]= ["b","c"]
d["b"] = ["a","c"]
print(d["c"])

