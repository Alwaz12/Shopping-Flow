Below is a revised, professional version of your installation instructions:

---

# Shopping Flow

## Installation

### Prerequisites
- **Python:** Ensure you have Python installed (version **>=3.10 and <3.13**).
- **UV:** This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

### Setup Instructions

1. **Navigate to the Project Directory**
   ```bash
   cd shopping_flow
   ```

2. **Install UV (if not already installed)**
   ```bash
   pip install uv
   ```

3. **Create and Activate a Virtual Environment**
   - Create the virtual environment:
     ```bash
     uv venv
     ```
   - For **Windows** users, activate the virtual environment:
     ```bash
     source ./.venv/Scripts/activate
     ```

4. **Initialize Dependencies**
   Add and install all necessary dependencies from the `requirements.txt` file:
   ```bash
   uv add -r requirements.txt
   ```

5. **Run the Shopping Flow Agent**
   Start the agent using:
   ```bash
   chainlit run src/shopping_flow/main.py
   ```

---

**Note:**  
Ensure you execute these commands from the root of the project directory. If you encounter any issues, verify that your Python environment is correctly configured and that all required dependencies are properly installed.

Happy coding!
