"""
Solution file to calculate number of ways to attend classes over N days and graduation probability
"""


# function to calculate graduation probability
def get_total_sequences_and_graduation_probability(N):

    # dictionary utilized for recursion memoization
    memo = {}

    # recursive function to count valid sequences of length `n` ending with `absent` consecutive absences
    def count_sequences(n, absent):

        # return the sequence count if already calculated
        if (n, absent) in memo:
            return memo[(n, absent)]

        # base case, only one valid sequence of length 0 (the empty sequence), no absences allowed
        if n == 0:
            return 1 if absent == 0 else 0

        # if the current day is attended (`absent = 0`),
        # then it can follow any valid sequence of length \( n-1 \) with 0, 1, 2, or 3 consecutive absences.
        if absent == 0:
            result = (count_sequences(n - 1, 0) +
                      count_sequences(n - 1, 1) +
                      count_sequences(n - 1, 2) +
                      count_sequences(n - 1, 3))

        # if the current day is missed (`absent = 1, 2, 3`),
        # then it can follow a sequence of length 'n-1' with `absent-1` consecutive absences.
        else:
            # length `n-1` with `absent-1` absences and miss the nth day
            result = count_sequences(n - 1, absent - 1)

        # memoize the result
        memo[(n, absent)] = result

        return result

    # total sequences will be addition of all the possible consideration of valid scenarios which is absence < 4
    total_sequences = (count_sequences(N, 0) +
                       count_sequences(N, 1) +
                       count_sequences(N, 2) +
                       count_sequences(N, 3))

    # total number of sequences of length N ending with an absence
    miss_graduation_sequences = (count_sequences(N, 1) +
                                 count_sequences(N, 2) +
                                 count_sequences(N, 3))

    # return the result as a fraction
    return total_sequences, f"{miss_graduation_sequences}/{total_sequences}"
