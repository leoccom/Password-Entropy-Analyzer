# 🛡️ Password-Entropy-Analyzer

## Project Summary
This script is a comprehensive cybersecurity utility that performs two key functions: **Analyzing** password strength using the quantifiable **Shannon Entropy** metric (measured in bits), and **Generating** cryptographically secure, complex passwords using Python's `secrets` module. It demonstrates the application of Information Theory to security engineering.

---

## 💻 Technical Details

| Category | Details |
| :--- | :--- |
| **Language** | Python 3.x |
| **Dependencies** | Standard Python Library (`string`, `sys`, `math`, `secrets`) |
| **Skills Demonstrated** | **Computational Mathematics (Logarithms), Information Theory (Entropy), Cryptography** (`secrets` module), **Functional Programming** (`any`), and **Python Tool Development.** |

---

## 🔢 Entropy Methodology and Strength Ratings

The strength is determined by calculating the theoretical maximum randomness of the password.

### A. Entropy Formula

The script uses the Shannon Entropy formula to calculate the number of bits of randomness ($H$):

$$H = L \times \log_2(R)$$

Where:
* **$L$ (Length):** The total number of characters in the password.
* **$R$ (Keyspace):** The size of the character set (Assumed to be $\mathbf{94}$: 26 lowercase + 26 uppercase + 10 digits + $\approx 32$ common special characters).
* **$2^H$:** The total number of possible combinations an attacker must test.

### B. Strength Ratings

The calculated entropy ($H$) is used to provide an objective security rating. These thresholds are based on common industry benchmarks for brute-force resistance.

| Entropy Score ($H$) | Rating | Rationale |
| :--- | :--- | :--- |
| **$\mathbf{\ge 80.0}$ bits** | **Excellent** | High resistance to brute force; requires full complexity to qualify. |
| **$\mathbf{\ge 64.0}$ bits** | **Strong** | Meets the standard industry minimum for secure symmetric keys. |
| **$\mathbf{\ge 40.0}$ bits** | **Medium** | Necessary to defend against modern dictionary and offline attacks. |
| **$\mathbf{< 40.0}$ bits** | **Weak** | Highly vulnerable to rapid cracking. |

**Source Note:** The use of Shannon Entropy as a metric is based on mathematical principles. The strength thresholds (64 bits, 80 bits, etc.) align with common industry benchmarks and the security principles emphasizing length and randomness outlined in the [**NIST Special Publication 800-63B**](https://pages.nist.gov/800-63-3/sp800-63b.html) guidelines.

---

## Development Tools and Transparency

The core mathematical model, the entropy formula implementation, and the complexity thresholds were **designed and written manually** to demonstrate foundational principles in Math, Physics, and Security. The secure password generation component relies on the **cryptographically secure `secrets` module**.

This project utilized AI agents for **boilerplate generation** (e.g., standard structural components) and **documentation formatting**, demonstrating proficiency in leveraging advanced tooling while maintaining ownership over the critical, skill-based components of the project.

---

## ▶️ How to Run the Script

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/leoccom/Password-Entropy-Analyzer.git
    ```
2.  **Navigate into the Project Folder:**
    ```bash
    cd Password-Entropy-Analyzer
    ```

3.  **Execute the Script:**
    ```bash
    python3 password_checker.py
    ```

4.  **Options:** The program will prompt you to choose between **Analysis** or **Generation** of a password.

---

## ⚙️ Core Functions

| Function | Purpose | Security Note |
| :--- | :--- | :--- |
| `check_password(password)` | Calculates the Shannon Entropy ($H$), checks for full complexity, and returns the float score and rating. | **Analysis** |
| `generate_password(length)` | Creates a new password of a specified length, guaranteed to contain all four character types. | **Uses `secrets` module for cryptographic strength.** |
| `main()` | Handles user choice, input, and prints the formatted results (entropy to 2 decimal places). | **Utility** |