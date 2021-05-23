n=int(input())
a=[i for i in range(1,n*(n+1)+1)]
c=n
for i in range(n):
	print("  "*i,end="")
	l=a[:c]
	l1=a[-c:]
	m=""
	for i in l:
		m=m+str(i)+"*"
		a.remove(i)
	for i in l1:
		m=m+str(i)+"*"
		a.remove(i)
	for i in range(len(m)-1):
		print(m[i],end="")
	print()
	c=c-1
