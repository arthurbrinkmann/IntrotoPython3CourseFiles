in_file = open('C:/Python/mydata2.txt', 'r+')
print (in_file.readline())
in_file.seek(0)
print (in_file.readline())
in_file.close()
