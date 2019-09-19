def copy_file(a,b):
    with open(a, 'r') as file_a, open(b, 'w') as file_b:
        for fileid, line in enumerate(file_a.readlines()):
            file_b.write('{} {}'.format(fileid+1, line))

a = '/home/shiyanlou/shiyanlou.txt'
b = '/home/shiyanlou/shiyanlou_copy.txt'

copy_file(a,b)
