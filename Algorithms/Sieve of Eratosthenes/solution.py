class Solution:
    def sieve_of_eratosthenes(self, n: int) -> int:
        i = 2

        # All numbers are prime therefore all values in array are True
        primes = [True]*(n+1)

        # turning 0,1 index to non-prime i.e. False
        primes[0] = False
        primes[1] = False

        # Outerloop that runs till sqrt i
        while (i*i <= n+1):

            # If primes[i] is not changed, then it is a prime
            if primes[i] == True:

                # Update all multiples of i
                for val in range(i*i, n+1, i):
                    primes[val] = False
            i += 1

        # Print all prime numbers
        for i in range(2, n+1):
            if primes[i]:
                print(i)


if __name__ == '__main__':
    n = int(input())
    obj = Solution()
    obj.sieve_of_eratosthenes(n)
