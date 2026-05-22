# mdformat-frontmatter

[![Build Status][ci-badge]][ci-link]
[![codecov.io][cov-badge]][cov-link]
[![PyPI version][pypi-badge]][pypi-link]
[![OpenSSF Scorecard][scorecard-badge]][scorecard-link]

An [mdformat](https://github.com/executablebooks/mdformat) plugin for ensuring that yaml `front-matter` is respected.
Many tools (such as [jekyll](https://github.com/jekyll/jekyll)) use yaml front matter for automation purposes.
`mdformat-frontmatter` only supports yaml. For example:

```markdown

---
test: yaml
---
# This looks okay
For some markdown code.
```

Frontmatter can only be at the first line or two of the code.
```markdown
# This is not
---
test: yaml
---
```
Note: that at this stage this plugin is not that sophisticated. The principle objective is to allow properly formed yaml header blocks to pass through.
Incorrectly formed blocks may result in strange behaviour.

## Requirements

Python 3.10 or higher.

## Development

This package was built from the [template](https://github.com/executablebooks/mdformat-plugin) provided by [executable books](https://github.com/executablebooks) and customized (specifically to separate content PR's from the release cycle).
This package uses [hatch](https://hatch.pypa.io) as the build engine, and [tox](https://tox.readthedocs.io) for test automation.

To install development dependencies:

```bash
pip install -e ".[dev,test]"
```

To run the tests:

```bash
tox
```

and with test coverage:

```bash
tox -e py312-cov
```

The easiest way to write tests, is to edit tests/fixtures.md

To run the code formatting and style checks:

```bash
tox -e py312-pre-commit
```

or directly

```bash
pip install pre-commit
pre-commit run --all
```

To run the pre-commit hook test:

```bash
tox -e py312-hook
```

## Release Process

Releases are fully automated using [python-semantic-release](https://python-semantic-release.readthedocs.io/) and [conventional commits](https://www.conventionalcommits.org/):

1. Merge PRs with conventional commit titles (e.g., `fix:`, `feat:`, `chore:`)
2. The CI workflow automatically analyzes commits, determines version bump, updates CHANGELOG, creates a tag, and publishes to PyPI
3. Artifacts are signed with [Sigstore](https://www.sigstore.dev/) for supply chain security

The release workflow uses [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (OIDC) and generates [attestations](https://docs.pypi.org/attestations/) for all published packages.

[ci-badge]: https://github.com/butler54/mdformat-frontmatter/workflows/CI/badge.svg?branch=main
[ci-link]: https://github.com/butler54/mdformat-frontmatter/actions?query=workflow%3ACI+branch%3Amain+event%3Apush
[cov-badge]: https://codecov.io/gh/butler54/mdformat-frontmatter/branch/main/graph/badge.svg
[cov-link]: https://codecov.io/gh/butler54/mdformat-frontmatter
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-frontmatter.svg
[pypi-link]: https://pypi.org/project/mdformat-frontmatter
[scorecard-badge]: https://api.scorecard.dev/projects/github.com/butler54/mdformat-frontmatter/badge
[scorecard-link]: https://scorecard.dev/viewer/?uri=github.com/butler54/mdformat-frontmatter
