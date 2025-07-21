# Contributing to Code Morningstar

Thank you for your interest in contributing to Code Morningstar! This document provides guidelines and information for contributors.

## 🎯 How to Contribute

### Reporting Issues
- Use the GitHub issue tracker
- Include detailed description of the problem
- Provide steps to reproduce
- Include system information (OS, Python version, etc.)
- Add relevant logs or error messages

### Submitting Changes
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with clear commit messages
4. Add tests for new functionality
5. Ensure all tests pass: `python -m pytest backend/tests/ -v`
6. Submit a pull request

## 🏗️ Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment tool

### Setup Steps
```bash
# Clone repository
git clone https://github.com/your-username/Code-Morningstar.git
cd Code-Morningstar

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Unix

# Install dependencies
pip install -r backend/requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy safety bandit

# Run tests
python -m pytest backend/tests/ -v
```

## 📝 Code Standards

### Python Code Style
- Follow PEP 8 style guide
- Use Black for code formatting: `black backend/`
- Use type hints throughout the codebase
- Write comprehensive docstrings

### Code Quality
- Run linting: `flake8 backend/`
- Type checking: `mypy backend/`
- Security scanning: `bandit -r backend/`
- Dependency checking: `safety check -r backend/requirements.txt`

### Testing
- Write tests for all new functionality
- Maintain 100% coverage of core functionality
- Use descriptive test names
- Include both positive and negative test cases

### Documentation
- Update README.md for significant changes
- Add docstrings to all functions and classes
- Update API documentation for endpoint changes
- Include examples in documentation

## 🧪 Testing Guidelines

### Running Tests
```bash
# Run all tests
python -m pytest backend/tests/ -v

# Run specific test file
python -m pytest backend/tests/test_llm_service.py -v

# Run with coverage
python -m pytest backend/tests/ -v --cov=backend --cov-report=html
```

### Writing Tests
```python
import pytest
from backend.services.llm_service import LLMService

def test_llm_service_functionality():
    """Test that LLM service works correctly."""
    service = LLMService(mock_mode=True)
    result = service.generate("test prompt")
    assert "[MOCK]" in result
    assert "test prompt" in result
```

## 🔀 Git Workflow

### Branch Naming
- Feature branches: `feature/description`
- Bug fixes: `fix/description`
- Documentation: `docs/description`
- Refactoring: `refactor/description`

### Commit Messages
Follow conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Examples:
- `feat(api): add model information endpoint`
- `fix(llm): handle missing model file gracefully`
- `docs(readme): update installation instructions`
- `test(llm): add tests for parameter validation`

### Pull Request Process
1. Ensure all tests pass
2. Update documentation if needed
3. Add entry to CHANGELOG.md
4. Request review from maintainers
5. Address feedback promptly

## 📋 Code Review Guidelines

### For Contributors
- Keep changes focused and atomic
- Provide clear description of changes
- Include screenshots for UI changes
- Be responsive to feedback

### For Reviewers
- Focus on code quality and maintainability
- Check for security vulnerabilities
- Verify tests are comprehensive
- Ensure documentation is updated

## 🏷️ Release Process

### Version Numbering
Follow Semantic Versioning (SemVer):
- MAJOR.MINOR.PATCH
- Major: Breaking changes
- Minor: New features (backward compatible)
- Patch: Bug fixes (backward compatible)

### Release Checklist
- [ ] All tests passing
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in relevant files
- [ ] Tagged release in Git
- [ ] GitHub release created

## 💡 Project Structure

### Backend (`backend/`)
- `app/` - FastAPI application modules
- `services/` - Business logic services
- `tests/` - Test suite
- `feature_flags/` - Feature toggle configuration
- `settings.py` - Configuration management
- `start.py` - Application entry point

### Frontend (`frontend/`)
- `standalone.html` - Main frontend interface
- `src/` - Svelte source (optional)
- `package.json` - Frontend dependencies

### Documentation (`docs/`)
- Development guides
- API documentation
- Architecture overview

## 🎯 Areas for Contribution

### High Priority
- Performance optimizations
- Security enhancements
- Test coverage improvements
- Documentation updates

### Medium Priority
- New API endpoints
- UI/UX improvements
- Error handling enhancements
- Logging improvements

### Future Features
- Database integration
- User authentication
- WebSocket support
- Docker containerization
- Kubernetes deployment

## 🤔 Getting Help

### Documentation
- [Development Guide](docs/DEVELOPMENT.md)
- [API Reference](docs/API.md)
- [Project README](README.md)

### Community
- GitHub Discussions for questions
- GitHub Issues for bug reports
- Pull Requests for code contributions

### Contact
- Create GitHub issue for project-related questions
- Tag maintainers in pull requests for review

## 📄 License

By contributing to Code Morningstar, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to Code Morningstar! 🌟
