file_obj=open('file.txt','r')
content = file_obj.read()
print(content)
content=file_obj.readline()

count+=1
for line in content:
  count+=1
  line=line.strip("\n")
  print(f"line{count}=>{line}")
