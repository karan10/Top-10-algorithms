# link - http://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

def count_triplet_with_smaller_sum(arr, given_sum):
    arr.sort()
    n = len(arr)
    ans = 0
    for i in range(0, n):
        j = i + 1
        k = n - 1
        while k > j:
            if ( arr[i] + arr[j] + arr[k] ) >= given_sum:
                k = k - 1
            else:
                ans = ans + ( k - j )
                j = j + 1
    return ans



if __name__ == "__main__":
    arr = [5, 1, 3, 4, 7]
    given_sum = 12
    print count_triplet_with_smaller_sum(arr, given_sum)

