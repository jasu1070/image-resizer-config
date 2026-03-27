# Image Resizer Pro: Cloud Config Repository

This repository hosts the official update configurations for the **Image Resizer Pro** application by **TECHNOLOGY DEVELOPMENTS**.

> [!NOTE]
> This is a configuration-only repository. The application source code is private and protected for security reasons.

## 📂 Repository Structure

- `version.json`: The source of truth for the update system.
- `README.md`: Instructions and documentation.

## 🚀 How to Update the App

To push a new update to your users, follow these steps:

1. **Edit `version.json`**:
   - Update `versionCode` and `versionName` to match your new build.
   - Set `minVersionCode` to enforce a mandatory update.
   - Update `apkUrl` with your new download link.
2. **Commit Changes**: Push the updated JSON to the `main` branch.

## 📝 Configuration Schema

```json
{
  "versionCode": 2005,
  "versionName": "1.0.4",
  "minVersionCode": 2000,
  "apkUrl": "https://www.uptodown.com/android/imageresizer",
  "releaseNotes": "• Critical security hardening\n• New high-fidelity UI gradients\n• Performance optimizations",
  "isStoreRedirect": true
}
```
