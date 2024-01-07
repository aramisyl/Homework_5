phone_number = input("Введите 11-значный номер телефона")
code = phone_number[2:4]
phone_pt1 = phone_number[4:7]
phone_pt2 = phone_number[7:9]
phone_pt3 = phone_number[9:]

print('375 (%s) %s-%s-%s' % (code, phone_pt1, phone_pt2, phone_pt3))
print(f"375 ({code}) {phone_pt1}-{phone_pt2}-{phone_pt3}")
print("375 ({}) {}-{}-{}".format(code, phone_pt1, phone_pt2, phone_pt3))