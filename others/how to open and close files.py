f = open('text')
try:
    date = f.read()
    print(date)
finally:
    f.close()

# with open('text') as f:
#     data = f.read()
#     print(data)
