# This is a Python script that finds prime numbers in a given range using the Sieve of Eratosthenes algorithm.

def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [num for num, prime in enumerate(is_prime) if prime]


def main():
    # Get user input for the range of numbers
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))

    # Validate input
    if start_range < 0 or end_range < 0 or start_range >= end_range:
        print("Invalid input. Please enter a valid range.")
        return

    # Find and print prime numbers in the specified range
    primes = sieve_of_eratosthenes(end_range)
    primes_in_range = [p for p in primes if p >= start_range]

    print(f"Prime numbers between {start_range} and {end_range}: {primes_in_range}")


if __name__ == "__main__":
    main()