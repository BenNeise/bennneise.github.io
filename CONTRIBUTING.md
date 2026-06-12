# Contributing

Thank you for your interest in contributing! This document outlines guidelines and workflow for contributing to this project.

## Code of Conduct

Please be respectful and constructive in all interactions.

## Getting Started

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/BenNeise/bennneise.github.io.git
   cd bennneise.github.io
   ```

2. **Set up your environment** (see [README.md](README.md) for detailed setup instructions):
   ```bash
   bundle install
   ```

3. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

1. **Start the dev server:**
   ```bash
   bundle exec jekyll serve --livereload --drafts --incremental
   ```
   Site available at `http://localhost:4000`

2. **Make your changes:**
   - For blog posts: add to `_posts/` (format: `YYYY-MM-DD-title.markdown`)
   - For drafts: add to `_drafts/` (use `--drafts` flag when serving)
   - For pages/guides: add to `_guides/` or root
   - For styling: edit files in `assets/`

3. **Test locally:**
   - Verify the site builds: `bundle exec jekyll build`
   - Check for broken links and HTML issues (see linting section)

4. **Commit with clear messages:**
   ```bash
   git commit -m "type: concise description"
   ```
   Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

5. **Push and open a pull request:**
   ```bash
   git push --set-upstream origin feature/your-feature-name
   ```
   - GitHub Actions will run CI checks
   - Address any failures and push follow-up commits
   - Maintainer will review and merge once checks pass

## Linting & Pre-commit Checks

Before pushing, run pre-commit hooks locally:

```bash
# Install pre-commit framework
pip install pre-commit

# Install hooks (first time only)
pre-commit install

# Run manually at any time
pre-commit run --all-files
```

Checks include:
- Markdown formatting and linting
- YAML validation
- Trailing whitespace removal

## Pull Request Process

1. Ensure your branch is up to date: `git pull origin master`
2. All CI checks must pass
3. Descriptive PR title and description
4. Link related issues if applicable
5. Be open to feedback during review

## CI/CD Pipeline

When you open a PR, the following checks run:

- **Dependency audit:** `bundler-audit` checks for known vulnerabilities
- **Build validation:** Jekyll builds the site successfully
- **Link checking:** Validates internal and external links
- **Linting:** Markdown and HTML validation

All checks must pass before merge.

## Reporting Issues

Found a bug or have a feature request? Please open an issue with:
- Clear description of the problem/request
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Screenshots if applicable

## Questions?

Feel free to open a discussion or issue. We're here to help!

Thanks for contributing! 🎉
