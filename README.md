# ansible

Personal Ansible playbook for provisioning my development machines. It installs and
configures the tools I use day to day, targeting both macOS (via Homebrew) and
Debian/Ubuntu (via `apt`).

## Layout

A single playbook (`playbook.yaml`) applies to `localhost` and runs the following
roles in order:

| Role        | Purpose                                                              |
|-------------|-----------------------------------------------------------------------|
| `android`   | Android Studio                                                        |
| `embedded`  | CLion                                                                  |
| `desktop`   | Modern CLI replacements (bat, bottom, dust, fd, ripgrep, procs, ...), Warp, Quicksilver, direnv, git, delta, stow |
| `rust`      | Rust toolchain via rustup, rust-analyzer, RustRover                    |
| `web`       | Node.js, Google Cloud SDK, IntelliJ IDEA, k3d, Apple container         |
| `network`   | Networking tools (nmap, mtr, httpie, iperf3, doggo, masscan, ...)      |
| `ai`        | Node.js, Claude Code, Codex CLI, ccstatusline                          |
| `terminal`  | Ghostty, zoxide, difftastic                                            |

Each role's tasks live under `roles/<name>/tasks/`. Most tasks are guarded with
`ansible_facts['os_family']` checks so the same playbook can run on macOS or
Debian/Ubuntu, installing the appropriate package for each.

## Requirements

- [Ansible](https://docs.ansible.com/) (installed via Homebrew: see `Brewfile`)
- The `community.general` collection:

  ```sh
  ansible-galaxy collection install -r requirements.yml
  ```

## Usage

Run the full playbook against the local machine:

```sh
ansible-playbook playbook.yaml -i localhost, -c local
```

Check syntax without applying anything:

```sh
ansible-playbook playbook.yaml --syntax-check
```

Limit to a single role with tags or `--start-at-task`, or comment out roles in
`playbook.yaml` as needed.

## CI

GitHub Actions (`.github/workflows/ci.yml`) runs the playbook against an
`ubuntu:26.04` container on every push and pull request: a syntax check, a full
run, and a second run to verify idempotency.
