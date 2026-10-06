# 🔍 Problem 1: Find Most Frequent Element

# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    most_common = numbers[0]

    for number in numbers:
        if counts[number] > counts[most_common]:
            most_common = number

    return most_common


"""
Time and Space Analysis for problem 1:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)

The function goes through the list to count each number and then
goes through the list again to find the number with the highest count.
Both passes are linear, so the total time complexity is O(n).

- Space complexity: O(n)

The dictionary can store up to n different numbers and their counts.

- Why this approach?

I used a dictionary because it allows the function to keep track of
how many times each number appears efficiently.

- Could it be optimized?

The number of passes could be reduced, but the overall time complexity
would still be O(n). The dictionary approach is already efficient.

- What are the trade-offs?

The main trade-off is that the dictionary uses extra memory. However,
using extra space makes the function much faster than repeatedly
counting each value in the list.
"""


# Test cases for Problem 1
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5]) == 5
assert most_frequent([]) is None
assert most_frequent([1, 2, 2, 1]) in [1, 2]

print("Problem 1 tests passed!")


# 🔍 Problem 2: Remove Duplicates While Preserving Order

# Write a function that returns a list with duplicates removed
# but preserves order.

def remove_duplicates(nums):
    result = []
    seen = set()

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)

The function checks every element in the list. Set membership is
O(1) on average, so the overall time is O(n).

- Space complexity: O(n)

The set and result list can both contain up to n elements.

- Why this approach?

I used a set to remember which values have already appeared. This
allows duplicates to be found quickly while keeping the original
order in the result list.

- Could it be optimized?

The time complexity is already O(n), which is efficient. The space
could be reduced if the original list were allowed to be modified,
but this solution creates a new list as required.

- What are the trade-offs?

The benefit is fast duplicate checking and preserved order. The
trade-off is that extra memory is needed for the set and result list.
"""


# Test cases for Problem 2
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([]) == []
assert remove_duplicates([1]) == [1]
assert remove_duplicates([1, 1, 1, 1]) == [1]
assert remove_duplicates([3, 2, 1]) == [3, 2, 1]

print("Problem 2 tests passed!")


# 🔍 Problem 3: Return All Pairs That Sum to Target

# Write a function that returns all unique pairs of numbers
# in the list that sum to a target.
# Order of output does not matter.
# Assume input list has no duplicates.

def find_pairs(nums, target):
    pairs = []
    seen = set()
    used_pairs = set()

    for number in nums:
        needed = target - number

        if needed in seen:
            pair = tuple(sorted((number, needed)))

            if pair not in used_pairs:
                pairs.append(pair)
                used_pairs.add(pair)

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)

The function goes through the list once. Set lookups and insertions
are O(1) on average, so the overall average and worst practical
performance is linear.

- Space complexity: O(n)

The seen set and used_pairs set can hold up to O(n) values. The
result list can also contain multiple pairs.

- Why this approach?

I used a set so that the function can quickly check whether the
number needed to reach the target has already appeared.

- Could it be optimized?

Yes. A two-pointer solution could be used after sorting the list.
That can reduce extra lookup space, but sorting would take O(n log n)
time and would change the ordering of the input.

- What are the trade-offs?

This set-based approach uses more memory, but it keeps the running
time at O(n) and does not require sorting the input.
"""


# Test cases for Problem 3
assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
assert find_pairs([], 5) == []
assert find_pairs([1], 2) == []
assert set(find_pairs([1, 2, 4, 8], 10)) == {(2, 8)}
assert set(find_pairs([-2, -1, 1, 2], 0)) == {(-2, 2), (-1, 1)}

print("Problem 3 tests passed!")


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)

# Create a function that adds n elements to a list that has a fixed
# initial capacity.
# When the list reaches capacity, simulate doubling its size by
# creating a new list and copying all values over.

def add_n_items(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    capacity = 2
    items = []

    for i in range(n):
        if len(items) == capacity:
            new_items = []

            # Copy the existing items into the new list.
            for item in items:
                new_items.append(item)

            items = new_items
            capacity *= 2

            print("Resized to capacity:", capacity)

        items.append(i)

    return items


"""
Time and Space Analysis for problem 4:

- When do resizes happen?

Resizes happen whenever the current number of elements reaches the
list's capacity. The capacity is doubled each time.

- What is the worst-case for a single append?

A single append can take O(n) when a resize happens because all
existing elements must be copied into the new list.

- What is the amortized time per append overall?

The amortized time is O(1) per append. Although some individual
appends require O(n) time, resizing does not happen on every append.
The capacity doubles, so the total copying work across n appends
is O(n).

- Space complexity: O(n)

The list grows as elements are added. During a resize, a second
larger list temporarily exists, but the overall space is still O(n).

- Why does doubling reduce the cost overall?

Doubling means the list does not have to resize after every single
append. This spreads the cost of copying elements across many
future appends.
"""


# Test cases for Problem 4
assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(2) == [0, 1]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

print("Problem 4 tests passed!")


# 🔍 Problem 5: Compute Running Totals

# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.

def running_total(nums):
    totals = []
    current_total = 0

    for number in nums:
        current_total += number
        totals.append(current_total)

    return totals


"""
Time and Space Analysis for problem 5:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)

The function goes through every element in the input list once,
so the running time is linear.

- Space complexity: O(n)

The function creates a new list containing one running total for
each input value.

- Why this approach?

I used one variable to keep track of the current total and added
each result to a new list. This avoids repeatedly summing the
previous values.

- Could it be optimized?

The time complexity is already O(n). The extra result list is
necessary because the problem asks for a new list.

- What are the trade-offs?

The approach is simple and efficient, but it uses O(n) additional
space for the returned list.
"""


# Test cases for Problem 5
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([]) == []
assert running_total([5]) == [5]
assert running_total([-1, 2, -3]) == [-1, 1, -2]
assert running_total([0, 0, 0]) == [0, 0, 0]

print("Problem 5 tests passed!")


# ---------------------------------------------------------
# OPTIMIZATION
# ---------------------------------------------------------
# Problem 3 was optimized using a set-based approach.
#
# A basic nested-loop solution would compare each number with every
# other number. That approach would have O(n^2) time complexity.
#
# The optimized version above uses a set called "seen" so that the
# function can check for the needed number in O(1) average time.
# This reduces the overall time complexity from O(n^2) to O(n).
#
# The trade-off is that the optimized version uses O(n) extra space
# for the sets. This is a good trade-off because the faster runtime
# is more useful when the input becomes large.
#
# Performance comparison:
#
# Original nested-loop approach:
# Time: O(n^2)
# Space: O(1) excluding the output
#
# Optimized set-based approach:
# Time: O(n)
# Space: O(n)
#
# The optimized approach uses more memory but is much faster for
# large input lists.