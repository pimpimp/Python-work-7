#3
admin_username = "admin"
admin_password = "1412"

username = input()
password = input()

if username == admin_username:
  if password == admin_password:
      print("Welcome, admin")
  else:
      print("You are not admin")
else:
    print("You are not admin")
