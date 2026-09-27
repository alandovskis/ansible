"""Verify that every package the playbook installs on Debian/Ubuntu actually
provides the command a user (or the rest of this repo's roles) expects.

Run against the host the playbook targeted, e.g.:
    pytest --hosts=local:// tests/test_packages.py
"""

import pytest

EXPECTED_COMMANDS = [
    # role: languages/cpp
    "gcc",
    "gdb",
    "valgrind",
    "cmake",
    "ninja",
    "ccache",
    "pkg-config",
    "doxygen",
    "lcov",
    "gcovr",
    "clang-tidy",
    "clang-format",
    "make",
    "clang",
    # role: languages/rust
    "rustup",
    "cargo",
    "rustc",
    "rust-analyzer",
    # role: desktop
    "bat",
    "dust",
    "gping",
    "hyperfine",
    "fd",
    "procs",
    "rg",
    "trippy",
    "tokei",
    "zoxide",
    "direnv",
    "dasel",
    "lnav",
    "git",
    "delta",
    "stow",
    # role: network
    "http",
    "iperf3",
    "ip",
    "masscan",
    "mtr",
    "nethogs",
    "nmap",
    "ssh",
    "tcpflow",
    # role: terminal
    "ghostty",
    "difftastic",
    # role: languages/javascript / ai
    "node",
    "npm",
    "claude",
    "ccstatusline",
    "codex",
    # role: languages/typescript
    "tsc",
    # role: desktop / network (strict-confinement snaps)
    "bandwhich",
    "bottom",
    "grex",
    "doggo",
]

# GUI apps installed via classic-confinement snaps. Not meaningfully
# testable with --version (they need a display), so we only assert the
# snap itself installed rather than that a command is on PATH.
EXPECTED_SNAPS = [
    "android-studio",
    "clion",
    "rustrover",
    "webstorm",
    "intellij-idea",
]


@pytest.mark.parametrize("command", EXPECTED_COMMANDS)
def test_command_is_on_path(host, command: str) -> None:
    assert host.exists(command), f"expected `{command}` to be on PATH after the playbook runs"


@pytest.mark.parametrize("snap_name", EXPECTED_SNAPS)
def test_snap_is_installed(host, snap_name: str) -> None:
    result = host.run(f"snap list {snap_name}")
    assert result.rc == 0, result.stderr


def test_rust_analyzer_runs(host) -> None:
    result = host.run("rust-analyzer --version")
    assert result.rc == 0, result.stderr


def test_bat_runs(host) -> None:
    result = host.run("bat --version")
    assert result.rc == 0, result.stderr


def test_delta_runs(host) -> None:
    result = host.run("delta --version")
    assert result.rc == 0, result.stderr


def test_difftastic_runs(host) -> None:
    result = host.run("difftastic --version")
    assert result.rc == 0, result.stderr
