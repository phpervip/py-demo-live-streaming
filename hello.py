print("Hello, World!")
print("你好，世界")

import datetime

def writefile(path, filename, data, type):
    with open(path + filename, type)as f:
        f.write(data)

t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

path = "A/video/"
writefile(path, 'update.log', t + '\n', 'w')
