#coding:utf-8
import threading 
rs = []
lock = threading.RLock()
class Isprime(threading.Thread):
	def __init__(self,num):
		threading.Thread.__init__(self)
		self.num = num
	def run(self):
		global rs,lock
		isprime = False
		m = self.num
		for i in range(2, m//2+1):#在python3中"/"是真正除法，返回类型为float，在range中应用"//"
			if m % i == 0:
				isprime = True
				break
		lock.acquire() #加锁控制
		if not isprime:
			rs.append(m)
		lock.release()

def main():
	global rs 
	threads = []
	#装载线程
	for i in range(2000,3000): 
		a=Isprime(i)
		threads.append(a)
	#启动线程
	for x in threads:
		x.start()
	#阻塞线程直到结束
	for s in threads:
		x.join()
	#打印结果  
	print("2000-3000之间所有素数为")
	print(rs)
	print("素数个数为:",len(rs))
if __name__=='__main__':
	main()
