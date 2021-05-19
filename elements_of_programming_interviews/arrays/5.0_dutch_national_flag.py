"""
create a better pivot tables for quicksort

assumption: single pivot element
test_case

algorithmic performance
time complexity:
space complexity:

"""

def dutch_pivot_case(pivot_index, A):
    
    pivot = A[pivot_index]
    # iterate to swap out small ones
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
   
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
	elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A



def test():
    A = [10, 2, 9, 5, 7 , 3, 6, 4, 1, 8]
    pivot = 3
    output = [2, 3, 4, 1, 5, 7, 10, 6, 9, 8]
    return_val = dutch_pivot_case(pivot, A)
    print(return_val)
    assert return_val == output


if __name__ == "__main__":
    test()
