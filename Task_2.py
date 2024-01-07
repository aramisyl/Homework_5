line = input("Введите строку с пробелами")
inverted_line = " ".join(line.split(" ")[::-1])

print("{}".format(" ".join(line.split(" ")[::-1])))
print(f"{inverted_line}")
print("%s" % inverted_line)