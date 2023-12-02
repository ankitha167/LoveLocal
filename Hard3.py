def count_digit_one(n):
    count = 0
    for i in range(1, n + 1):
        num = i
        while num > 0:
            if num % 10 == 1:
                count += 1
            num //= 10
    return count

# Example Usage
number = int(input())
total_ones = count_digit_one(number)
print("Output:", total_ones)

""" For each number i in the range from 1 to n, the inner loop extracts individual digits.
The inner loop continues dividing the number by 10 ( num //= 10 in Python) to extract the rightmost digit in each iteration.
Here count_digit_one(n) , accepts an integer n.Using a for loop with range(1, n + 1), it iterates through numbers from 1 to n.
The inner while loop extracts digits by continually dividing each number by 10 and counts the '1's.
It returns the total count of digit '1's."""
