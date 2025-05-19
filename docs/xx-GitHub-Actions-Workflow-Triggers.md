# GitHub Actions Workflow Triggers

This document explains the `on:` section in GitHub Actions workflows, which defines when your workflows will run.

## Understanding the `on:` Section

In GitHub Actions, the `on:` section defines the events that trigger the workflow. It's a crucial part of the workflow configuration that determines when your automated processes will run.

## Current Configuration

In our project's `.github/workflows/python-app.yml` file:

```yaml
on:
  pull_request:
    branches: ["master"]
```

This means:
- The workflow will run whenever a pull request is created or updated that targets the "master" branch
- It won't run for pull requests targeting other branches
- It won't run for other events like pushes, scheduled times, or manual triggers

## Common Trigger Options

### Push Events
Trigger a workflow when code is pushed to specific branches:

```yaml
on:
  push:
    branches: ["main", "develop"]
```

### Multiple Events
Trigger a workflow on multiple different events:

```yaml
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
```

### Scheduled Events
Trigger a workflow on a schedule using cron syntax:

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Run at midnight every day
```

### Manual Triggers
Allow manual workflow execution from the GitHub UI:

```yaml
on:
  workflow_dispatch:
```

### Repository Events
Trigger on various repository activities:

```yaml
on:
  issues:
    types: [opened, edited]
```

## Advanced Configuration

### Path Filtering
Trigger workflows only when specific files change:

```yaml
on:
  push:
    paths:
      - 'backend/**'
      - '!backend/README.md'
```

### Tag Events
Trigger workflows when tags are pushed:

```yaml
on:
  push:
    tags:
      - 'v*'  # Match any tag that starts with 'v'
```

### External Events
Trigger workflows from external events using the repository dispatch event:

```yaml
on:
  repository_dispatch:
    types: [deploy]
```

## Best Practices

1. **Be specific**: Target only the branches and events you need to avoid unnecessary workflow runs
2. **Use path filters**: Limit workflow runs to relevant file changes
3. **Consider workflow_dispatch**: Add manual triggers for testing and emergency runs
4. **Combine triggers wisely**: Use multiple triggers when appropriate, but keep workflows focused