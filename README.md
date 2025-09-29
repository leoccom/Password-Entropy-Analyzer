🛡️ Simple Password Strength Checker
Project Summary
This script is a foundational cybersecurity tool developed to assess the complexity and resilience of passwords against brute-force attacks. It utilizes a weighted scoring system based on standard security principles (length, character diversity, and special character usage) to provide both a numeric score and a qualitative strength rating.

💻 Technical Details
Category	Details
Language	Python 3.x
Dependencies	Standard Python Library (string, sys)
Skills Demonstrated	Python Programming, Conditional Flow Control, String Manipulation, Functional Logic (any), and Security Best Practices (Authentication).

Export to Sheets
🔢 Scoring Methodology (Max Score: 7)
The script calculates strength based on the following additive point system.

A. Point Criteria
Criterion	Requirement	Points Awarded
Length	≥12 characters	3 Points
≥8 characters, but <12	1 Point
Character Types	At least one Uppercase, Lowercase, Digit, and Special Character.	1 Point Each (Max 4 Pts)
TOTAL MAX SCORE	3 (Length) + 4 (Types)	7 Points

Export to Sheets
B. Strength Ratings
Total Score	Rating
7	Excellent / Near Perfect
5 - 6	Strong
3 - 4	Medium / Acceptable
0 - 2	Weak / Dangerous

Export to Sheets
🤖 Development Tools and Transparency
The core functional logic, scoring criteria, and flow control (using methods like any() and conditional logic) were designed and written manually to demonstrate foundational Python and security principles.

This project utilized AI agents for boilerplate generation (e.g., standard structural components) and documentation formatting, demonstrating proficiency in leveraging advanced tooling while maintaining ownership over the critical, skill-based components of the project.

▶️ How to Run the Script
Clone the Repository:

Bash

git clone [Your GitHub Repo URL]
cd password-checker
Execute the Script:

Bash

python3 password_checker.py
Input: The program will prompt you to enter the password you wish to analyze.

⚙️ Core Functions
Function	Purpose	Return Value
check_password(password)	Contains the entire scoring logic and rating system based on the defined criteria.	tuple[int, str] (Score, Rating)
main()	Handles the command-line input, calls the checker, and prints the formatted results to the user.	None