# 🛡️ Password-Entropy-Analyzer

## Project Summary
This script is an upgraded cybersecurity tool that assesses password strength using the industry-standard **Shannon Entropy** metric (measured in bits). It applies a core principle of Information Theory to quantify a password's randomness and resistance against brute-force attacks.

---

## 💻 Technical Details

| Category | Details |
| :--- | :--- |
| **Language** | Python 3.x |
| **Dependencies** | Standard Python Library (`string`, `sys`, `math`) |
| **Skills Demonstrated** | **Computational Mathematics (Logarithms), Information Theory (Entropy), Functional Programming** (`any`), **Security Metrics, and Python Tool Development.** |

---

## 🔢 Entropy Methodology and Strength Ratings

The strength is determined by calculating the theoretical maximum randomness of the password.

### A. Entropy Formula

The script uses the Shannon Entropy formula to calculate the number of bits of randomness ($H$):

$$H = L \times \log_2(R)$$

Where:
* **$L$ (Length):** The total number of characters in the password.
* **$R$ (Keyspace):** The size of the character set (Assumed to be $\mathbf{94}$: 26 lowercase + 26 uppercase + 10 digits + 32 common special characters).
* **$2^H$:** The total number of possible combinations an attacker must test.

### B. Strength Ratings

The calculated entropy ($H$) is used to provide an objective security rating. These thresholds are based on common industry benchmarks for brute-force resistance.

| Entropy Score ($H$) | Rating | Rationale |
| :--- | :--- | :--- |
| **$\mathbf{\ge 80.0}$ bits** | **Excellent / Cryptographically Secure** | High resistance to brute force; requires full complexity to qualify. |
| **$\mathbf{\ge 64.0}$ bits** | **Strong** | Meets the standard industry minimum for secure symmetric keys. |
| **$\mathbf{\ge 40.0}$ bits** | **Medium** | Necessary to defend against modern dictionary and offline attacks. |
| **$\mathbf{< 40.0}$ bits** | **Weak / Dangerous** | Highly vulnerable to rapid cracking. |

**Source Note:** The use of Shannon Entropy as a metric is based on mathematical principles. The strength thresholds (64 bits, 80 bits, etc.) align with common industry benchmarks and the security principles emphasizing length and randomness outlined in the [**NIST Special Publication 800-63B**](https://pages.nist.gov/800-63-3/sp800-63b.html) guidelines.

---

## Development Tools and Transparency

The core mathematical model, the entropy formula implementation, and the complexity thresholds were **designed and written manually** to demonstrate foundational principles in Math, Physics, and Security.

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

4.  **Input:** The program will prompt you to enter the password you wish to analyze.

---

## ⚙️ Core Functions

| Function | Purpose | Return Value |
| :--- | :--- | :--- |
| `check_password(password)` | Calculates the Shannon Entropy ($H$), checks for full complexity (all character types), and returns the float score and rating. | `tuple[float, str]` (Entropy Score, Rating) |
| `main()` | Handles the command-line input, calls the checker, and prints the formatted results to the user with **2 decimal places of precision**. | None |