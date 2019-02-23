from numpy.random import binomial,normal
from numpy import ones,array,zeros,mean,std,arange
from random import randrange,randint,random,sample,shuffle
from numpy import delete,where,argsort


def bin(n):
	p=0.5
	rep=n-1	
	att=rep*p
	adj=n-att
	rval=binomial(rep,p)
	return rval+adj




def PP(M):	#M is the matrix, in form of a numpy array
	R,C=M.shape
	ct_,rt_=sorted(M.sum(0),reverse=True),sorted(M.sum(1),reverse=True)
	ct=[bin(i) for i in ct_]
	rt=[bin(i) for i in rt_]
	while sum(ct)<sum(ct_):
		try:
			ct[binomial(C-1,0.5)]+=1
		except:
			pass
	while sum(ct)>sum(ct_):
		try:
			ct[binomial(C-1,0.5)]-=1
		except:
			pass
	while sum(rt)<sum(rt_):
		try:
			rt[binomial(R-1,0.5)]+=1
		except:
			pass
	while sum(rt)>sum(rt_):
		try:
			rt[binomial(R-1,0.5)]-=1
		except:
			pass
	occs=float(M.sum())
	rm=zeros([R,C],dtype=int)
	RR=[]
	for i in range(len(rt)):
		for j in range(int(rt[i])):
			RR.append(i)
	RC=[]
	for i in range(len(ct)):
		for j in range(int(ct[i])):
			RC.append(i)
	while rm.sum()<occs:
		rr,rc=sample(RR,1)[0],sample(RC,1)[0]
		rm[rr][rc]+=1
	sc=0
	more=where(rm>=1)
	while len(more[0])>0 and sc<100000:
		a,b=sample(range(len(more[0])),2)
		rr1,rc1=more[0][a],more[1][a]
		rr2,rc2=more[0][b],more[1][b]
		sc+=1
		if rm[rr1][rc2]<(rm[rr1][rc1]) and rm[rr1][rc2]<(rm[rr2][rc2]) and (rm[rr2][rc1])<(rm[rr1][rc1]) and rm[rr2][rc1]<(rm[rr2][rc2]):
			rm[rr1][rc1]-=1
			rm[rr1][rc2]+=1
			rm[rr2][rc1]+=1
			rm[rr2][rc2]-=1
			more=where(rm>=1)
	if sc==100000:
		more=where(rm>1)
		while len(more[0])>0:
			z=where(rm==rm.min())
			rr1,rc1=more[0][0],more[1][0]
			a=randrange(len(z[0]))
			rr2,rc2=z[0][a],z[1][a]
			if random()<=(float(ct[rc2])*float(rt[rr2]))/float(occs**2):
				rm[rr1][rc1]-=1
				rm[rr2][rc2]+=1
				more=where(rm>1)
	sc=0
	while sc<(10*C*R):
		rr1,rr2,rc1,rc2=sample(RR,2)+sample(RC,2)
		if m[rr1][rc1]!=m[rr1][rc2] and m[rr1][rc1]!=m[rr2][rc1] and m[rr2][rc1]!=m[rr2][rc2]:
			m[rr1][rc1]=abs(m[rr1][rc1]-1)
			m[rr1][rc2]=abs(m[rr1][rc2]-1)
			m[rr2][rc1]=abs(m[rr2][rc1]-1)
			m[rr2][rc2]=abs(m[rr2][rc2]-1)
			sc+=1
	return rm


