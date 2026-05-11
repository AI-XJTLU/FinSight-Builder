# Clean Software Packaging Checklist

The final Software submission zip should be created only after the final review.

Required internal structure:

```text
2472811-Feiyu_Chen/
  Task1/
  Task2/
```

Before creating the final zip, check:

- `Task1/` contains exactly one notebook: `DTS114_FinSight_Builder.ipynb`.
- `Task2/screenshots/01_commit_records.png`, `02_docker_deployed_website.png`, and `03_github_actions_success.png` are present.
- `Task2/test_results/pytest_output.txt` is present and shows passing tests.
- No `.git/` directory is included.
- No top-level `.github/` directory is included; if workflow evidence is needed, include only the copied file under `Task2/github_workflow_copy/ci.yml`.
- No `__pycache__/`, `.pytest_cache/`, `.ipynb_checkpoints/`, `*.pyc`, existing `*.zip`, or temporary browser profiles are included.
- No `.env`, real API keys, private SSH keys, or other local credential files are included.
- No temporary logs, local-only cache files, ad hoc browser profiles, or failed-run scratch files are included.
- No `.flask_pid` file is included.
- The submitted archive should not contain a nested copy of itself or any other `*.zip` file.

Recommended PowerShell command from the parent `CW` folder after cleanup:

```powershell
Compress-Archive -Path .\2472811-Feiyu_Chen\Task1,.\2472811-Feiyu_Chen\Task2 -DestinationPath .\2472811-Feiyu_Chen_clean.zip -Force
```

Do not create the final zip until GitHub Actions evidence has been captured and the working tree has been reviewed.

Important: this checklist is only packaging guidance. It does not create, delete, or modify the final submission archive by itself.
