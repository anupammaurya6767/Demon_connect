# Contribution Guidelines for Demon_Connect1 WhatsApp API

We welcome contributions to the Demon_Connect1 WhatsApp API project. Whether you want to fix a bug, add a new feature, or improve the documentation, your contributions are valuable. To ensure smooth collaboration, please follow these guidelines:

## Project Structure

Our project is organized as follows:

```
whatsapp_api_project/
├── 📁 api/
│ ├── 📄 whatsapp_api.py
│ └── 📄 __init__.py
│
├── 📁 drivers/
│ ├── ⚙️ chromedriver.exe
│ └── ⚙️ geckodriver.exe
│
├── 📁 utils/
│ ├── 📄 constants.py
│ ├── 📄 helpers.py
│ └── 📄 __init__.py
│
├── 📁 features/
│ ├── 📁 send/
│ ├── 📁 receive/
│ ├── 📁 login/
│ ├── 📁 group/
│ ├── 📁 media/
│ ├── 📁 commands/
│ ├── 📁 moderation/
│ └── 📁 user_management/
│
├── 📄 requirements.txt
├── 📄 main.py
└── 📄 sample_usage.py
```

## Contribution Workflow

1. **Fork the Repository**: Click on the "Fork" button on the top right of the [Demon_Connect1 repository](https://github.com/anupammaurya6767/Demon_connect) to create your own copy of the repository.

2. **Clone Your Fork**: Clone your forked repository to your local machine:

   ```shell
   git clone https://github.com/anupammaurya6767/Demon_connect.git
   ```

3. **Create a New Branch**: Create a new branch for your work. Name it descriptively, indicating the purpose of the branch:

   ```shell
   git checkout -b feature/add-new-feature
   ```

4. **Make Changes**: Make your changes in the appropriate directory based on the feature you're working on. Please follow our coding style and conventions.

5. **Commit Changes**: Commit your changes with a descriptive commit message:

   ```shell
   git commit -m "Add new feature: feature name"
   ```

6. **Push to Your Fork**: Push your changes to your fork on GitHub:

   ```shell
   git push origin feature/add-new-feature
   ```

7. **Open a Pull Request**: Go to your fork on GitHub and click the "New Pull Request" button. Describe your changes and submit the pull request. Make sure to select the appropriate base repository and branch.

## Coding Guidelines

- Follow PEP 8 style guidelines.
- Write clear and concise code.
- Provide meaningful variable and function names.
- Document your code using docstrings and comments as necessary.
- Ensure backward compatibility if you're modifying existing functionality.

## Testing

If you're adding new features or modifying existing ones, please provide tests for your code. We use Python's built-in `unittest` framework for testing.

## Documentation

If you're contributing to documentation, please use reStructuredText (rst) format and add your documentation in the relevant modules or create a new documentation module.

## Review and Merge

Your pull request will be reviewed by the project maintainers. They may suggest changes or improvements. Once the changes are accepted, your code will be merged into the main project.

## Be Courteous

Respect other contributors and maintainers. Constructive criticism is welcome, but be respectful in your interactions. We value a friendly and inclusive community.

We look forward to your contributions! Thank you for helping improve Demon_Connect1 WhatsApp API.
