n = int(input())
sang = [ int(input()) for _ in range(n)]
geun = []
for i in range(1,2*n+1):
  if i not in sang:
      geun.append(i)

sang.sort(reverse = True)
geun.sort(reverse = True)

temp = sang.pop() #처음은 상근이가 시작
for i in range(2*n):
  if not geun or not sang:
    break
  if i%2==0: #근상이 차례
    for j in range(len(geun)):
      if geun[-j-1] > temp:
        temp = geun.pop(-j-1) 
        break
    else : #큰게 없다면
      temp =0

  else : #상근이 차례
    for j in range(len(sang)):
      if sang[-j-1] > temp:
        temp = sang.pop(-j-1) 
        break
    else : #temp보다 큰게 없다면   
      temp = 0
      
if not sang:
  print(len(geun),0,sep="\n")
else:
  print(0,len(sang), sep="\n")
