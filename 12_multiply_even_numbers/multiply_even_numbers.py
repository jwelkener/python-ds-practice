def multiply_even_numbers(nums):
    
    res = 1

    for num in nums:
        if num%2==0:
            res *= num

    return res

"""Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """