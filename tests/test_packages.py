"""Verify that every package the playbook installs on Debian/Ubuntu actually
provides the command a user (or the rest of this repo's roles) expects.

Run against the host the playbook targeted, e.g.:
    pytest --hosts=local:// tests/test_packages.py
"""

import pytest

EXPECTED_COMMANDS = [
    # role: rust
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
    # role: web / ai
    "node",
    "npm",
    "claude",
    "ccstatusline",
    "codex",
]


@pytest.mark.parametrize("command", EXPECTED_COMMANDS)
def test_command_is_on_path(host, command):
    assert host.exists(command), f"expected `{command}` to be on PATH after the playbook runs"


def test_rust_analyzer_runs(host):
    result = host.run("rust-analyzer --version")
    assert result.rc == 0, result.stderr


def test_bat_runs(host):
    result = host.run("bat --version")
    assert result.rc == 0, result.stderr


def test_delta_runs(host):
    result = host.run("delta --version")
    assert result.rc == 0, result.stderr
