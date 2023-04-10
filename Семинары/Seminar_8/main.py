file = open('Семинары\Seminar_8\Sample.txt', 'r', encoding='UTF-8')
data = file.readlines()
print(data)
file.close()

print (data[0])
print (data[1].split())

# file = open('Семинары\Seminar_8\Sample.txt', 'a', encoding='UTF-8')
# file.write('\nДобавим еще одну строку')
# file.close()