# PJs Python Library
Python library containing utilities, connectors, resources, handlers, etc.

## Python Semantic Release
### Github - Personal Access Token (PAT)
Ref. https://stackoverflow.com/a/75116350

Create a Fine-grained personal access token (aka «PAT») with the least necessary privileges to commit changes to your repo:

Create a fine grained PAT with these steps -> https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token

Under Repository Access select Only select repositories and select the repo that you want to work with (authenticated pulls, commits, pushes etc.)

Under Permissions choose Repository permissions and set only Contents to Access level -> Read and write.

Then add the PAT with context secrets to your GitHub workflow/action, e.g.:
```
runs-on: ubuntu-latest
steps:
  - uses: actions/checkout@v3
    with:
      token: ${{ secrets.NAME_OF_YOUR_PAT }}
```

Additional documentation -> https://docs.github.com/en/rest/overview/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2022-11-28

### Github Workflow Actions
Create a Github workflow actions releasse.yml.

### Configure project settings
Create a pyproject.toml configuration file.

### Conventional Commits
This repo requires Conventional Commits.
  -> https://www.conventionalcommits.org

### Semantic Versioning
This repo uses Semantic Versioning.
  -> https://semver.org/

### Automated Semantic-Release (CI)
This repo uses [python-]semantic-release.
  -> https://www.youtube.com/watch?v=41WWOaaXW1M
  -> https://www.youtube.com/watch?v=mxPfbwJ0FiU
