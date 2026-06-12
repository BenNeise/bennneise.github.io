# Ben's Blog

Ben's personal website and technical blog, hosted on [GitHub Pages](https://pages.github.com/) using [Jekyll](https://jekyllrb.com/).

## Quick Start

### Using Dev Container (Recommended)

1. **Prerequisites:** Docker and Visual Studio Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open in Dev Container:**

   - Open the workspace in VS Code
   - VS Code will prompt to reopen in container
   - Or manually: `Cmd/Ctrl + Shift + P` → "Dev Containers: Reopen in Container"

3. **Start the dev server:**
   ```bash
   bundle exec jekyll serve --livereload --drafts --future --incremental
   ```
   - Site will be available at `http://localhost:4000`
   - Live reload enabled; changes refresh automatically

### Local Setup (macOS/Linux/WSL)

**Prerequisites:**

- Ruby 3.3.4 ([rbenv](https://github.com/rbenv/rbenv) or [rvm](https://rvm.io/) recommended)
- Bundler (`gem install bundler`)

**Setup:**

```bash
bundle install
```

**Run dev server:**

```bash
bundle exec jekyll serve --livereload --drafts --future --incremental
```

## Building & Deployment

**Build static site:**

```bash
bundle exec jekyll build
```

Output: `_site/` directory contains the static HTML.

**Deployment:**

- Push to `master` branch
- GitHub Actions runs CI checks (dependency audit, build validation)
- GitHub Pages automatically builds and deploys `master`
- Site available at `https://bennneise.github.io`

## Project Structure

```
.
├── _posts/          # Blog posts (Markdown, named YYYY-MM-DD-*.markdown)
├── _drafts/         # Draft posts (not published)
├── _guides/         # Long-form guide pages
├── _includes/       # Reusable page fragments
├── _layouts/        # Page templates (home, post, etc.)
├── assets/          # CSS, images, and static files
├── .devcontainer/   # Dev container configuration
├── .github/         # GitHub Actions workflows & configs
├── _config.yml      # Jekyll configuration
├── Gemfile          # Ruby dependencies
└── README.md        # This file
```

## Customization

### Colour Scheme

- Light gray: `#BFBFBF`
- Dark gray: `#525559`
- Yellow: `#E5BC5B`
- Orange: `#D47144`
- Red: `#B3443E`

### Custom CSS Classes

Add to your posts/pages:

- `<div class="info"></div>` — Info box
- `<div class="note"></div>` — Note box
- `<div class="tip"></div>` — Tip box
- `<div class="warning"></div>` — Warning box
- `<!--more-->` — Post excerpt marker (content before this displays in listings)

## Development Workflow

1. **Create a feature branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write or edit posts in `_posts/` or `_drafts/`**

   - Posts: `_posts/YYYY-MM-DD-title.markdown`
   - Drafts: `_drafts/title.markdown` (use `--drafts` flag when serving)

3. **Test locally:**

   ```bash
   bundle exec jekyll serve --livereload --drafts
   ```

4. **Push and open a pull request**

   - GitHub Actions runs CI checks
   - Merge once checks pass

5. **Deploy:** Push to `master` automatically triggers deployment

## Dependencies & Security

- **Ruby:** 3.3.4 (pinned for reproducibility)
- **Jekyll:** 3.10.0 (via `github-pages` v232)
- **Automated updates:** Dependabot creates PRs for dependency updates (see `.github/dependabot.yml`)
- **Vulnerability scanning:** `bundler-audit` runs in CI to detect security issues

## Contributing

Contributions welcome! Please:

1. Create a feature branch
2. Test changes locally
3. Ensure CI passes
4. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
