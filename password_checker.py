import string
import sys
import math

# Define constants
SPECIAL_CHARS = string.punctuation
# R(Keyspace): Total unique characters (26 lowercase + 26 uppercase + 10 digits + 32 special characters)
KEYSPACE_SIZE = 94

EXCELLENT_BITS = 80.0
STRONG_BITS = 64.0
MEDIUM_BITS = 40.0


def check_password(password: str):
    """
    Calculates the Shannon Entropy (H) and assigns a security rating
    It returns a tuple[float, str] containing given password's score(float) and rating(str).
    """

    # Scoring criteria
    length = len(password)

    # 1. Calculate Entropy
    # Shannon Entorpy Formula : H = L x log2(R) where H: Entropy, L: Length, R: Keyspace
    entropy = length * math.log2(KEYSPACE_SIZE)

    # 2. Check Complexity
    is_complex = (
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any((char in SPECIAL_CHARS) for char in password)
    ) # True only if all criteria are passed.


    # Ratings
    ratings = ["Excellent", "Strong", "Medium", "Weak"]
    if entropy >= EXCELLENT_BITS and is_complex:
        rating = ratings[0]
    elif entropy >= STRONG_BITS:
        rating = ratings[1]
    elif entropy >= MEDIUM_BITS:
        rating = ratings[2]
    else:
        rating = ratings[3]

    return (entropy, rating)

def main():
    """
    Handles user interaction and prints the final result.
    """

    # Get password from the user
    try:
        password = input("Enter the password you'd like to check: ")

        if not password.strip():
            print("\nERROR: Password cannot be empty.")
            sys.exit(1)

        # Call the core function
        final_entropy, final_rating = check_password(password)

        # Print the results
        print("\n--- ANALYSIS RESULTS ---")
        print(f"Password: {password}")
        print(f"Entropy score: {final_entropy:.2f} bits")
        print(f"Strength Rating: **{final_rating}**")
        print("-" * 25)

    except KeyboardInterrupt:
        # Allows the user to quit with Ctrl+C or Cmd+C
        print("\nProcess interrupted by user. Goodbye!")
        sys.exit(0)
    
    except Exception as e:
        # If an error occurs, display it.
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()