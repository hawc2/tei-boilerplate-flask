import os
import sys


def pytest_configure():
    # Ensure repo root is on sys.path so app.py is importable in CI.
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
