lst = [1,3,5,6]
target = 5

# Binary Search Solution:
# solution: log(n)?
def findTargetIndex(lst, target):
  lowPoint = lst[0]
  highPoint = len(arr) - 1

  if not lst:
    return None
  if target > lst[-1]:
    return len(lst)
  if target < lowPoint:
    return 0

  while lowPoint <= highPoint:
    midPoint = (lowPoint + highPoint) // 2
    if target == lst[midPoint]:
      return midPoint
    elif val < lst[midPoint]:
      highPoint = midPoint - 1
    else:
      lowPoint = midPoint + 1


  return midPoint

# Recursive solution:
def findTarget:
  if target < lst[0] # error checking logic
  fti(lowPoint, highPoint)
  def fti(lowPoint, highPoint):
    if target == lst[midPoint]:
      return midPoint
    if target < lst[midPoint]:
      fti(lst,target,lowPoint, midPoint)
    else:
      fti(lst,target,midPoint+1,highPoint)

