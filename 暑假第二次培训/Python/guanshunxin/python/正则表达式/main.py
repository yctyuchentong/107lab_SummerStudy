# print(r"\n")
# import re
# pattern=re.compile(r"\d+")
# m1=pattern.match("one123")
# print(m1)
# m11=pattern.match("123one")
# print(m11.group())
# m2=pattern.match("one123",3,6)
# print(m2)
# print(m2.group())
# m3=re.match(r"\d+","one123")
# print(m3)
# m4=re.match(r"[a-z]+","Abcde",re.I)
# print(m4)
# print(m4.group())
# import re
# pattern=re.compile(r"\d+")
# m1=pattern.search("one123one123")
# print(m1)
# print(m1.group())
# m2=pattern.search("one123",0,4)
# print(m2)
# print(m2.group())
# m3=re.search(r"\d+","one123")
# print(m3)
# print(m3.group())
# m4=re.search(r"[a-z]+","123Abcde",re.I)
# print(m4)
# print(m4.group())
# import re
# pattern=re.compile(r"\d{2}")
# m1=pattern.findall("one1234one12345")
# print(m1)
# m2=pattern.findall("one123",0,4)
# print(m2)
# m3=re.findall(r"\d+","one123")
# print(m3)
# m4=re.findall(r"[a-z]","one1234one22")
# print(m4)
# import re
# pattern=re.compile(r"[\s\,\;]+")
# m1=pattern.split("a,b;; c    d")
# print(m1)
# m2=re.split(r'[\s\,\;]+',"a,b;;c  d")
# print(m2)
# import re
# s="hello 123 world 456"
# pattern=re.compile(r"(\w+) (\w+)")
# m1=pattern.sub('hello world',s)
# print(m1)
# m2=pattern.sub('hello world',s,1)
# print(m2)
# m3=re.sub(r"(\w+) (\w+)","hello world",s,1)
# print(m3)
# import re
# p1=re.compile('\d-\d-\d')
# m1=p1.match('1-2-3')
# print(m1.group())
# print(m1.groups())
# p2=re.compile('(\d)-(\d)-(\d)')
# m2=p2.match('1-2-3')
# print(m2.groups())
# print(m2.group())
# m3=re.findall('(\d)-(\d)-(\d)','1-2-3 4-5-6')
# print(m3)
# import re
# m1=re.match(r'.+','Are you ok? No,I am not ok.')
# print(m1.group())
# m2=re.match(r'.+?','Are you ok? No,I am not ok.')
# print(m2.group())
# m3=re.findall(r'<.+>',r'<this><is><an><example>')
# print(m3)
# m4=re.findall(r'<.+?>',r'<this><is><an><example>')
# print(m4)
# import re
# s=r'eating apple seeing paper watching movie'
# m1=re.findall(r'(\b\w+?)ing',s)
# print(m1)
# m2=re.findall(r'(.+?)(?=ing)',s)
# print(m2)
# m3=re.findall(r'(.+?)(?<=ing)',s)
# print(m3)
# s='unite one unethical ethics use untie ultimate'
# m4=re.findall(r'\b(?!un)\w+\b',s)
# print(m4)
# m5=re.findall(r'(?<![a-z])\d{3,}','as123,123,12 4567')
# print(m5)
import re
pattern=re.compile(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
def is_email(email):
    if pattern.match(email):
        print("有效")
    else:
        print("无效")
# email=input()
# is_email(email)
pattern=re.compile(r'^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-])\/?$')
def is_url(url):
    if pattern.match(url):
        print("有效")
    else:
        print("无效")
is_url("www.bbb.com")
pattern=re.compile(r'^\s|\s$')
def has_blank(blank):
    if pattern.search(blank):
        print("前或后有空白字符",blank)
    else:
        print("前或后没有空白字符",blank)
has_blank(" txt ")