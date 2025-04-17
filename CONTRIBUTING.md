# Contributing to CompanyWise DSA Q&A

Thank you for your interest in contributing to **CompanyWise DSA Q&A**! We welcome contributions such as adding new questions, fixing bugs, or improving the app.

## How to Contribute

### 1. Fork the Repository
Click the "Fork" button on the project page to create a copy of the repository in your GitHub account.

### 2. Create a New Branch
Create a new branch for your changes:

```bash
git checkout -b add-new-question 
```

### 3. Add New Data
- **Questions**: Add company-specific question CSV files in the `data/` directory. Each file should contain columns like:
  - `ID`, `Question`, `Acceptance`, `Difficulty`, `Frequency`, `Link`
  
- **Answers**: Add answer CSV files in the `answers/` directory. Each answer file should contain columns:
  - `Answer`, `Question` (matching Question ID)

### 4. Test the Changes
Test the app locally to ensure everything works by building and running the Docker container:

```bash
docker build -t leetcode-dsa-app .
docker run -p 8501:8501 leetcode-dsa-app:latest
```

### 5. Submit a Pull Request
Once you're happy with your changes, submit a pull request. Please ensure to:

- Provide a clear and concise description of the changes you made.
- Reference any relevant issues (if applicable) by mentioning them using `#issue_number`.
- Follow the repository’s code style and formatting guidelines.
- Make sure your changes do not break existing functionality (run tests locally to confirm).

Once submitted, your pull request will be reviewed. If everything looks good, it will be merged into the main codebase.

