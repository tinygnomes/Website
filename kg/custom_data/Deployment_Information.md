# Custom Data: Deployment Information

### Website Deployment

*   [2025-06-24 09:14:14]

```json
{
  "current_deployment": {
    "provider": "GitHub Pages",
    "ci_cd_pipeline": "GitHub Actions (deploy.yml)",
    "build_commands": [
      "npm install",
      "npm run build"
    ],
    "trigger": "Push to main branch",
    "deployed_path": "./website"
  },
  "future_deployment": {
    "method": "Manual deployment",
    "servers": "Existing internal servers"
  }
}
```
