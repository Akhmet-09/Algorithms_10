# class Solution:
#     def searchRange(self,nums:list[int],target:int) ->list[int] : 
#         def isFirst(findBound : bool ) -> int : 
#             left = 0 
#             right = len(nums) - 1 
#             bound = - 1 
#             while left<=right:
#                 mid = (left+right)//2 
#                 if nums[mid] == target :
#                     bound = mid 
#                     if isFirst:
#                         left = mid + 1 
#                     else:
#                         right = mid - 1 
#                 elif nums[mid] < target :
#                     left = mid + 1 
#                 else:
#                     right = mid - 1 
#             return bound 
#         first_pos = isFirst(findBound=True)
#         if first_pos == -1 :
#             return [-1,-1]
#         last_pos = isFirst(findBound=False)
#         return [first_pos,last_pos]   
# solver = Solution()

# class Solution:
#     def isValid(self,s:str) -> bool : 
#         stack = []
#         pairs = {
#             ')' : '(',
#             ']' : '[',
#             '}' : '{'
#         }
#         for char in s :
#             if char in "([{":
#                 stack.append(char)
#             else:
#                 if not stack :
#                     return False 
#                 if stack[-1] != pairs[char]:
#                     return False 
#                 stack.pop()    
#         return len(stack) == 0 
# solve = Solution()

# raqamlar = arr.array('i' , [1,2,3,4,5,6,7])

# print(type(raqamlar))
# for num in raqamlar : 
#     print(num)


# def stack_ex(s:str):
#     stack = []
#     for char in s :
#         stack.append(char)
#     result =  ""
#     while len(stack)>0:
#         result += stack.pop()
#     return result 
# print(stack_ex('salom'))    


# def remove_duplicate(s:str):
#     stack = []
#     for char in s :
#         if stack  and stack[-1] == char :
#             stack.pop()
#         else:
#             stack.append(char)
#     return "".join(stack )        
# print(remove_duplicate('abbaca'))
# navbat =deque()
# numbers = [random.randint(1,100) for _ in range(10)]
# for x in numbers : 
#     navbat.append(x)
# navbat = deque(['Ali','Vali','Ruslan','Nurik','Berik'])
# print(f"Boshlangish mijozlar : {navbat}")
# while len(navbat)>0:
#     hozirgi_mijoz = navbat.popleft()
#     print(f" {hozirgi_mijoz}ga xizmat ko'rsatildi va u ketdi.")
# print(f"Hozirgi navbat holati : {navbat} " )    
import math 
# print(math.comb(127,4))
print(math.comb(127,30))

















