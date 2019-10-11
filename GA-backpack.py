import random as r

#遗传算法求解背包问题

Max_t = 0#最优基因
Max_e = []
kk = 30#迭代次数
PS = 5 #群体规模
mm = 0
wt = [4, 3, 1, 1]#重量
tv = [3, 2, 1.5, 2]#价值
wt_limit = 4 #背包容量

while mm < kk:
	#1.初始化
	tt = []
	def f_wt(x):
			return x[0]*wt[0]+x[1]*wt[1]+x[2]*wt[2]+x[3]*wt[3]
	def d_4():
		a = []
		for i in range(4):#一条染色体上的基因数
			a.append((r.randint(0,5)))
		return a
	def f_produce():
		tt = []
		for i in range(PS):#限制超过背包容量
			t = d_4()
			while f_wt(t) > wt_limit:
				t = d_4()
			tt.append(t)
		return tt

	#2.适应性评价
	def f_tv(x):
			return x[0]*tv[0]+x[1]*tv[1]+x[2]*tv[2]+x[3]*tv[3]
	Eval = []#背包的
	t = f_produce()
	for tt in t:
		Eval.append(f_tv(tt))
	print('初始基因：')
	for tt in t:
		print(tt)
	max_t = max(Eval)
	if max_t > Max_t:
		Max_t = max_t
	for i in range(PS):
		if Eval[i] == Max_t:
			Max_e = t[i]
			break
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

	#4.交配x变异
	xy = []
	xy2 = []#交配的选择容器
	p = 0
	k = 0.88
	while p < PS:
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
			if f_wt(xy[p]) > wt_limit or f_wt(xy[p+1]) > wt_limit:
				td = d_4()
				while f_wt(td) > wt_limit:
					td = d_4()
				print(td)
				for i in range(4):
					xy[p][i] = td[i]
					xy[p+1][i] = td[i]
			p+=2
	else:
		pp = xy.pop()
		p = 0
		while p < len(xy): 
			rr = r.randint(0,3)
			tt = xy[p][rr]
			xy[p][rr] = xy[p+1][rr]
			xy[p+1][rr] = tt
			if f_wt(xy[p]) > wt_limit or f_wt(xy[p+1]) > wt_limit:
				te = d_4()
				while f_wt(te) > wt_limit:
					te = d_4()
				print(te)
				for i in range(4):
					xy[p][i] = te[i]
					xy[p+1][i] = te[i]
			p+=2
		xy.append(pp)
	for i in xy2:
		xy.append(i)
	mt = xy[:]
	print('交配完成的基因')
	for m in mt:
		print(m)#最后交配的基因

	#5.重新更新染色体适应值，更新染色体最优值
	e = []
	for m in mt:
		e.append(f_tv(m))
	max_tt = max(e)
	print('1次迭代后的最优适应值:')
	print(max_tt)
	if max_tt >= Max_t:
		Max_t = max_tt
	for i in range(PS):
		if e[i] == Max_t:
			Max_e = mt[i]
			break
	mm+=1

print('经过'+str(kk)+'次之后的最优值:')
print(Max_t)
print('经过'+str(kk)+'次之后的最优基因:')
print(Max_e)





