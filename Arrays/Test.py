# def mergeSort(arr,l,r):
#     if l<r:
#         m = l+(r-l)//2
#         mergeSort(arr,l,m)
#         mergeSort(arr,m+1,r)
#         merge(arr,l,m,r)
#
# def merge(arr, l, m, r):
#     n1 = m-l+1
#     n2 = r-m
#     L = [0]*n1
#     R = [0]*n2
#
#     for i in range(n1):
#         L[i] = arr[l+i]
#     for j in range(n2):
#         R[j] = arr[m+1+j]
#     i,j,k = 0,0,1
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i+=1
#         else:
#             arr[k] = R[j]
#             j+=1
#         k+=1
#
#     while i<n1:
#         arr[k] = L[i]
#         i+=1
#         k+=1
#     while j<n2:
#         arr[k] = R[j]
#         j+=1
#         k+=1
#
# arr = [1,7,3,9,5,2,6,4] [1,7,2,3,5,6,4]
# mergeSort(arr,0,len(arr)-1)
# print(arr)
#
# # arr = [1,7,1,3,2,9,1,5,2,6,4]
# # K is greater than m and less than n
# # set = (m number of element ) m is very less than n
# # {1:3,2:2,3:1 O(n+mlogm) o(n)
# #
# #  design base car class
# #
# #
# # class Car:
# #     def __init__(self,make,model,year,color):
# #         self.speed = 0
# #         self.make = make
# #         self.model = model
# #         self.year = year
# #         self.color = color
# #         self.power = False
# #         self.tank = 0.0
# #         self.tank_capacity = 50.0
# #
# #     def getTank(self):
# #         return self.tank
# #     def getTankCapacity(self):
# #         return self.tank_capacity
# #     def setTank(self,fuel):
# #         empty = self.getTankCapacity() - self.tank
# #         if (self.getTank() == 0 and fuel < self.getTankCapacity()):
# #             self.tank = fuel
# #         elif empty < fuel:
# #             self.tank = 50.0
# #         else:
# #             self.tank+=fuel
#
#
# 1-[key1:value,key2:value]
#
# ACID
#
# Atomicity
# Consistency
# Isolation
# Durability