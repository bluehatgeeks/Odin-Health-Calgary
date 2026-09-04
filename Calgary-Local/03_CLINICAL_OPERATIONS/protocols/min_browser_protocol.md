# Min Browser Automation Protocol

## Overview
Min Browser is used to bypass Google's "Sign-in wall" and "Robot detection" by leveraging its persistent authenticated sessions. Since Min is Electron-based, it is controlled via the Chrome DevTools Protocol (CDP).

## 🛠 Execution Workflow

### 1. Activation (Remote Debugging)
To enable agent control, Min Browser must be launched with the remote debugging port.
- **Command**: `/Applications/Min.app/Contents/MacOS/Min --remote-debugging-port=9222`
- **Verification**: Check if `http://localhost:9222/json/version` is reachable.

### 2. Session Attachment
Instead of launching a new browser instance, the agent must **attach** to the existing session:
- **Tool**: Playwright or Puppeteer.
- **Connection**: Use `browserType.connectOverCDP('http://localhost:9222')`.
- **Targeting**: Iterate through available pages/targets to find the one matching the target URL (e.g., Google Sheets).

### 3. Operational Rules
- **Persistence**: Never clear cookies or cache within the Min session unless explicitly requested.
- **Authentication**: If a login wall appears, do NOT attempt to automate the login. Stop and ask the user to manually complete the login in the visible Min window, then re-attach.
- **Digital Glue**: Use this method for any task requiring UI-level interaction with Google Sheets/Drive that API calls cannot handle.

## ⚠️ Safety & Constraints
- Ensure only one instance of Min is running with the debugging port to avoid port conflicts.
- Use `headless=False` (or the existing window) to maintain session stability.
