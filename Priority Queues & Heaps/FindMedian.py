from heapq import *

class Median:

	def __init__(self):
		self.maxHeap = []
		self.minHeap = []

	def insertNum(self,num):
		if not self.maxHeap or -1*self.maxHeap[0] >= num:
			heappush(self.maxHeap,-1*num)
		else:
			heappush(self.minHeap,num)
		print("After Insert",num,self.maxHeap,self.minHeap)

		if len(self.maxHeap) > len(self.minHeap):
			heappush(self.minHeap, -1*heappop(self.maxHeap))
		elif len(self.maxHeap) < len(self.minHeap):
			heappush(self.maxHeap, -1*heappop(self.minHeap))
		print("After balancing of array ",num,self.maxHeap,self.minHeap)

	def findMedian(self):
		print("Find Median:",self.maxHeap,self.minHeap)
		if len(self.maxHeap) == len(self.minHeap):
			print("true : ",-1*self.maxHeap[0],self.minHeap[0])
			return (-1*self.maxHeap[0] + self.minHeap[0])/2
		return -1*self.maxHeap[0]/1.0

m = Median()
m.insertNum(3)
m.insertNum(1)
print(m.findMedian())
m.insertNum(5)
print(m.findMedian())
m.insertNum(4)
print(m.findMedian())

