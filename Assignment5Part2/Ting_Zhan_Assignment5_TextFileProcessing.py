GullTrvls=open('17157-8.txt','r',encoding='ISO-8859-1')
prtext=open('gulliver_pure_text.txt','w')

i=0

for count,line in enumerate(GullTrvls.readlines()):
    if 'THE FIRST PUBLISHER TO THE READER.' in line:
        a=count
    if 'NOTE.' in line:
        b=count-1

print(a,b)
GullTrvls.close()
GullTrvls=open('17157-8.txt','r',encoding='ISO-8859-1')

for line in GullTrvls.readlines():
    i=i+1
    
    #if len(line.strip())<1:
        #pass

    if i < a:
        pass
    
    elif i > b:
        pass

    elif "[Illustration" in line:
        pass

    elif ".]" in line:
        pass

    else:
        prtext.writelines(line)

inputlines='The number of lines in the input file: {0}.'.format(i)
print(inputlines)

prtext.close()

a=0
b=0
c=0
d=0

prtext=open('gulliver_pure_text.txt','r')
for lines in prtext.readlines():
    a=a+1
    if 'Lilliput' in lines:
        b=b+1
    if 'LILLIPUT' in lines:
        c=c+1
    if 'lilliput' in lines:
        d=d+1
    
outputlines='The number of lines in the ouput file: {0}.'.format(a)
lilliput='The number of times that “Lilliput” appeared: {0}.'.format(b)
print(outputlines)
print(lilliput)
