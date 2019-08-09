s = input('please input:')
b = s.encode('utf-8')
print(b)

print('字符串s的长度是:',len(s))
print('字符串b的长度是:',len(s))

s2 = b.decode('utf-8')
print('s == s2:',s == s2)