import random as r

Max_t = 0.0#最优基因
kk = 2#迭代次数
PS = 10 #群体规模
mm = 0

#1.初始化
tt = []
def d():
	a = []
	p = 4 #一条染色体上的基因数
	while p:
		a.append((r.randint(-500,500)/100))
		p-=1
	return a
for i in range(PS):
	tt.append(d())
while mm < kk:
	#2.适应性评价
	def f(x1, x2, x3, x4):
			return 1/(x1**2+x2**2+x3**2+x4**2)	
	Eval = []#适应值
	t = []
	if mm == 0:
		t = tt[:]
	else:
		t = mt
	for tt in t:
		Eval.append(f(tt[0], tt[1], tt[2], tt[3]))
	print('初始基因：')
	for tt in t:
		print(tt)
	max_t = max(Eval)
	if max_t > Max_t:
		Max_t = max_t
	print('最优染色体')
	print(max_t)

	#3.选择
	def sum_s(t):
		sum = 0
		for s in t:
			sum+=s
		bl = []
		for s in t:
			bl.append(s/sum)
		return bl
	d = sum_s(Eval)#染色体的占比
	print('染色体的占比')
	print(d)
	def select(t):
		bb = []
		for i in range(PS):
			j = 0
			s = t[0]
			g = t[0]
			rs = r.randint(0,999)/1000
			if rs > s:
				while rs > s:
					s+=t[j+1]
					g = t[j+1]
					j+=1
				bb.append(g)
			else:
				bb.append(g)
		return bb
	e = select(d) #选择出的染色体
	print('选择出的染色体')
	print(e)
	#选择基因
	ee = []
	def select_gene(e):
		ee = []
		for es in e:
			for i in range(PS):
				if es == d[i]:
					ee.append(t[i])
					break
		return ee
	ee = select_gene(e)
	print('选择出的基因')
	for e in ee:
		print(e)

	#4.交配
	xy = []
	xy2 = []#交配的选择容器
	p = 0
	k = 0.88
	while p < 5:
		rr = r.randint(0,100)/100
		if rr < k:
			xy.append(ee[p])#交配
		else:
			xy2.append(ee[p])#不交配
		p+=1
	print('参加交配的染色体')
	for x in xy:
		print(x)
	if len(xy)%2 == 0:
		p = 0
		while p < len(xy): 
			rr = r.randint(0,3)
			tt = xy[p][rr]
			xy[p][rr] = xy[p+1][rr]
			xy[p+1][rr] = tt

			p+=2
	else:
		pp = xy.pop()
		p = 0
		while p < len(xy): 
			rr = r.randint(0,3)
			tt = xy[p][rr]
			xy[p][rr] = xy[p+1][rr]
			xy[p+1][rr] = tt
			p+=2
		xy.append(pp)
	p = 0
	for i in xy2:
		xy.append(i) 

	mt = xy[:]
	print('交配完成的基因')
	for m in mt:
		print(m)#最后交配的基因

	#5.变异
	TPO = 0.1
	p = 0	
	for i in range(len(mt)):
		rr = r.randint(0,10)/10
		if rr < TPO:
			print(i)
			mt[i][r.randint(0,3)] = r.randint(-500,500)/100
	#变异后的基因
	print('变异后的基因')
	for m in mt:
		print(m)

	#6.重新更新染色体适应值，更新染色体最优值
	e = []
	for m in mt:
		e.append(f(m[0], m[1], m[2], m[3]))
	max_tt = max(e)
	print('1次迭代后的适应值:')
	print(max_tt)
	if max_tt > Max_t:
		Max_t = max_tt
	mm+=1

print('经过'+str(kk)+'次之后的最优值:')
print(Max_t)




