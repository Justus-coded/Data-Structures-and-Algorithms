def longest_consecutive_seq(nums):
    """
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    Your algorithm should run in O(n) complexity.
    :param nums:
    :return:
    """
    # Create a set of the numbers
    num_set = set(nums)

    # Initialize the length of the longest consecutive sequence
    longest_seq = 0

    # Iterate through the numbers
    for num in num_set:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_seq = 1

            # Increment the current number and sequence length until the sequence ends
            while current_num + 1 in num_set:
                current_num += 1
                current_seq += 1

            # Update the longest sequence length
            longest_seq = max(longest_seq, current_seq)

    return longest_seq
