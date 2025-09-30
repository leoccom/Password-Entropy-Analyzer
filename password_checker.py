import string
import sys
import math
import secrets

# Define constants
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARS = string.punctuation
ALL_CHARS = LOWERCASE + UPPERCASE + DIGITS + SPECIAL_CHARS

# R(Keyspace): Total unique characters (26 lowercase + 26 uppercase + 10 digits + 32 special characters)
KEYSPACE_SIZE = 94

# Entropy criteria
EXCELLENT_BITS = 80.0
STRONG_BITS = 64.0
MEDIUM_BITS = 40.0

# Default password length
DEFAULT_PASSWORD_LENGTH = 16


def check_password(password: str):
    """
    Calculates the Shannon Entropy (H) and assigns a security rating
    It returns a tuple[float, str] containing given password's score(float) and rating(str).
    """

    # Scoring criteria
    length = len(password)

    # 1. Calculate entropy
    # Shannon Entorpy Formula : H = L x log2(R) where H: Entropy, L: Length, R: Keyspace
    entropy = length * math.log2(KEYSPACE_SIZE)

    # 2. Check complexity
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


def generate_password(length: int=DEFAULT_PASSWORD_LENGTH):
    """
    Generates a secure password meeting all complexity requirements.
    """

    # Complexity requirements
    required_chars = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SPECIAL_CHARS)
    ]

    # Remaining characters
    remaining_length = length - len(required_chars)

    if remaining_length > 0:
        remaining_chars = [secrets.choice(ALL_CHARS) for _ in range(remaining_length)]
    else:
        remaining_chars = []

    # Combine all characters (required + remaining)
    password_chars = required_chars + remaining_chars

    # Shuffle the list
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
    

def main():
    """
    Handles user interaction and prints the final result.
    """

    # User choice
    print("\nSelect an action to operate:")
    print("1. Password Analyzation")
    print("2. Password Generation")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
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
    
    elif choice == "2":
        try:
            length = 0
            while length < 4:
                length_input = input(f"Enter your desired length (default {DEFAULT_PASSWORD_LENGTH}): ").strip()
                if length_input == "":
                    length = DEFAULT_PASSWORD_LENGTH
                    break
                length = int(length_input)
                if length < 4:
                    print("Please provide length at least 4")
            
            new_password = generate_password(length)

            print("\n--- GENERATED PASSWORD ---")
            print(f"Generated password: {new_password}")
            print(f"Entropy score: {length * math.log2(KEYSPACE_SIZE):.2f} bits")
            print("-" * 30)
        
        except ValueError:
            print("Invalid input for length")
            sys.exit(1)
    
    else:
        print("Invalid choice. Quitting.")
        sys.exit(1)
                


if __name__ == "__main__":
    main()