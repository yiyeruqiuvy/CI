#裴乾锋 毛梓蒙 王航 = 4:3:3
def d_s(d):#7个计算函数 1个模糊规则
	if d <= 25:
		return -d/25+1
	else: 
		return 0.0

def d_m(d):
	if (d >= 15) and (d <= 30):
		return (d/15 - 1)
	elif d >= 30 and d <= 45:
		return -d/15+3
	else:
		return 0.0

def d_l(d):
	if (d >= 35) and (d <= 60):
		return (d/25 - 7/5)
	else:
		return 0.0

def t_s(d):
	if(d <= 25):
		return (-d/25)+1
	else:
		return 0.0

def t_m(d):
	if d <= 25:
		return d/25
	elif d < 50:
		return -d/25 +2
	else:
		return 0.0

def t_ll(d):
	if d >= 25 and d <= 50:
		return d/25 - 1
	elif d >= 50 and d <= 75:
		return -d/25 +3
	else:
		return 0.0

def t_l(d):
	if d >= 50 and d <= 75:
		return d/25 - 2
	elif d >= 75 and d <= 100:
		return -d/25 +4
	else:
		return 0.0

def d(d):
	D = [];
	D.append(d_s(d))
	D.append(d_m(d))
	D.append(d_l(d))
	return D

def t(t):
	T = [];
	T.append(t_s(t))
	T.append(t_m(t))
	T.append(t_ll(t))
	T.append(t_l(t))
	return T

def count_yt(t,d):
	yt = []
	s = max(min(t[0],d[1]),min(t[1],d[1]),min(t[2],d[1]),min(t[1],d[2]))
	yt.append(s)
	m = max(min(t[0],d[0]),min(t[1],d[0]),min(t[3],d[1]),min(t[2],d[2]),min(t[3],d[2]))
	yt.append(m)
	l = max(min(t[2],d[0]),min(t[3],d[0]),min(t[0],d[2]))
	yt.append(l)
	return yt

def count_time(yt):
	return (100*yt[0]+500*yt[1]+1000*yt[2])/(yt[0]+yt[1]+yt[2])

T = [56, 28, 18, 80, 70]
D = [33, 20, 40, 50, 10]#初始化啰

p = 0#打印结果呗
while(p < 5):
	print("温度为"+str(T[p])+"湿度为"+str(D[p])+"时灌溉时间为:")
	print(str(round(count_time(count_yt(t(T[p]),d(D[p]))),2))+'s')
	p +=1







