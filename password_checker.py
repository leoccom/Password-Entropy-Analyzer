import string
import sys

SPECIAL_CHARS = string.punctuation


def check_password(password: str):
    """
    Evaluates the strength of a given password based on my criteria. (length, case, numbers, special characters)
    It returns a tuple containing given password's score and rating.
    """

    # Scoring criteria
    length = len(password)
    score = 0

    ## Length (Max 3 points)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 1

    ## Uppercase (Max 1 point)
    if any(char.isupper() for char in password):
        score += 1

    ## Lowercase (Max 1 point)
    if any(char.islower() for char in password):
        score += 1

    ## Numbers (Max 1 point)
    if any(char.isdigit() for char in password):
        score += 1

    ## Special characters (Max 1 point)
    if any((char in SPECIAL_CHARS) for char in password):
        score += 1


    # Ratings
    ratings = ["Excellent", "Strong", "Medium", "Weak"]
    rating = ""
    if score >= 7:
        rating = ratings[0]
    elif score >= 5:
        rating = ratings[1]
    elif score >= 3:
        rating = ratings[2]
    else:
        rating = ratings[3]

    return (score, rating)

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
        final_score, final_rating = check_password(password)

        # Print the results
        print("\n--- ANALYSIS RESULTS ---")
        print(f"Password: {password}")
        print(f"Total score: {final_score}/7")
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