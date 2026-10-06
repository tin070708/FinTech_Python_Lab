email = input("nhập địa chỉ email: ")
username, domain = email.split("@")
first_three = username[0:3]
email = first_three + "***@"+ domain
print(email)
