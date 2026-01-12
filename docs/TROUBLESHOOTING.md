# Troubleshooting Guide for RALF Note

This guide provides solutions and tips for common issues encountered while using RALF Note.

---

### "ModuleNotFoundError: No module named 'typer'"
This error indicates that required Python packages are not installed.

**Solution:** Install the necessary packages using pip:
```bash
pip install typer rich ollama
```

---

### "Failed to connect to Ollama"
This issue occurs when RALF Note cannot establish a connection with the Ollama server.

**Possible Causes & Solutions:**
- **Ollama server not running:**
  Ensure that the Ollama server is running in the background. Open your terminal and run:
  ```bash
  ollama serve
  ```
- **Incorrect Ollama host configuration:**
  RALF Note might be configured to connect to the wrong address or port. You can check your current configuration and update it:
  ```bash
  ralf-notes init --show
  ralf-notes init --set-ollama-host http://127.0.0.1:11434 # Or your correct Ollama host
  ```
- **Firewall blocking connection:**
  Check if a firewall is preventing RALF Note from connecting to the Ollama port (default is 11434).

---

### "Model '<model_name>' is not available"
This error means that the specified LLM is not downloaded or recognized by your Ollama instance.

**Solution:** Pull the required model using the Ollama CLI:
```bash
ollama pull <model_name>
# Example: ollama pull ministral-3:3b
```
If you wish to use a different model, you can update your RALF Note configuration:
```bash
ralf-notes init --set-model <new-model-name>
```

---

### "Structured Text parsing failed"
RALF Note expects the LLM to return output in a specific structured text format. If the LLM deviates from this format, parsing will fail.

**Solution:**
- **Check LLM's adherence to instructions:** This often indicates an issue with the LLM's ability to follow the exact format instructions. The fallback mechanism creates a warning document with debug info, which you can inspect.
- **Inspect raw LLM output:** Review the raw output in your `stage1_raw` directory to see how the LLM responded.
- **Try a different model or lower temperature:** Some models are better at following instructions. A lower `temperature` setting (`ralf-notes init --set-temperature 0.1`) can also make the LLM's output more deterministic.

---

### Operations timing out or taking too long
LLM calls, especially for larger files or slower models, can sometimes exceed default time limits.

**Solution:**
Use the `--timeout` option with the `ralf-notes generate` command to increase the allowed time per LLM call:
```bash
ralf-notes generate --timeout 120 # Increase timeout to 120 seconds (2 minutes)
```
You can also set this in your configuration:
```bash
ralf-notes init --set-request-timeout-seconds 120
```

---

### Too many requests / API errors
If you are processing many files quickly, you might encounter rate limiting or other API errors from the Ollama server.

**Solution:**
- **Add a delay between requests:** Use the `--delay` option with `ralf-notes generate` to add a pause between processing each file:
  ```bash
  ralf-notes generate --delay 0.1 # Add a 100ms delay between files
  ```
  You can also set this in your configuration:
  ```bash
  ralf-notes init --set-request-delay-seconds 0.1
  ```
- **Increase retry attempts:** RALF Note has built-in retry logic with exponential backoff. You can increase the number of attempts:
  ```bash
  ralf-notes generate --retries 5 # Allow up to 5 retries
  ```
  You can also set this in your configuration:
  ```bash
  ralf-notes init --set-retry-attempts 5
  ```

---

### Path not found or not writable
If you encounter errors related to paths not existing or not having write permissions.

**Solution:**
- **Verify path existence:** Double-check that the source or output directories you specify actually exist on your system.
- **Check permissions:** Ensure RALF Note has the necessary read/write permissions for the directories it needs to access.
- **Use absolute paths:** Sometimes using absolute paths can resolve issues related to relative path interpretation.
- **Run `ralf-notes init` interactively:** The interactive setup will guide you and validate paths.

---

### Debugging with Logs
RALF Note provides comprehensive logging to help diagnose issues.

**Solution:**
- **Change log level:** You can set the log level to `DEBUG` to get more verbose output:
  ```bash
  ralf-notes init --set-log-level DEBUG
  ```
- **Check log file:** By default, logs are written to `~/.ralf-notes/ralf-notes.log`. You can specify a custom log file:
  ```bash
  ralf-notes init --set-log-file /path/to/my/ralf-notes.log
  ```
  Review the log file for detailed error messages and execution flow.

---
