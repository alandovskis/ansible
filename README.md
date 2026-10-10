# ansible

[![CI](https://github.com/alandovskis/ansible/actions/workflows/ci.yml/badge.svg)](https://github.com/alandovskis/ansible/actions/workflows/ci.yml)

Personal Ansible playbook for provisioning my development machines. It installs and
configures the tools I use day to day, targeting both macOS (via Homebrew) and
Debian/Ubuntu (via `apt`).

## Layout

A single playbook (`playbook.yaml`) applies to `localhost` and runs the following
roles in order:

| Role                      | Purpose                                                              |
|---------------------------|-----------------------------------------------------------------------|
| `android`                 | Android Studio                                                        |
| `languages/cpp`           | GCC, GDB, Valgrind (Debian/Ubuntu only), CMake, Ninja, ccache, pkg-config, Doxygen, lcov, gcovr, clang-tidy, clang-format, GNU Make, Clang, CLion |
| `desktop`                 | Modern CLI replacements (bat, bottom, dust, fd, ripgrep, procs, ...), Warp, Quicksilver, direnv, git, delta, stow |
| `languages/rust`          | Rust toolchain via rustup, rust-analyzer, RustRover                    |
| `languages/javascript`    | Node.js, WebStorm                                                      |
| `languages/typescript`    | TypeScript compiler                                                    |
| `languages/python`        | Python, uv, PyCharm                                                    |
| `cloud`                   | IntelliJ IDEA                                                          |
| `containerization`        | Apple container                                                        |
| `k8s`                     | k3d                                                                    |
| `network`                 | Networking tools (nmap, mtr, httpie, iperf3, doggo, masscan, ...)      |
| `ai`                      | Node.js, Claude Code, Codex CLI, ccstatusline                          |
| `terminal`                | Ghostty, zoxide, difftastic                                            |

Each role's tasks live under `roles/<name>/tasks/`. The `ai` role is split into one task file per
client (`node.yaml`, `claude-code.yaml`, `codex.yaml`), pulled together by `tasks/main.yaml`; note
that `tasks_from` is not honoured for entries in a play's `roles:` list, so the split files must be
imported from `main.yaml` rather than selected from the playbook. Most tasks are guarded with
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

GitHub Actions (`.github/workflows/ci.yml`) runs on pushes to `main` and on pull requests, on an
Ubuntu 26.04 runner: a syntax check, a full run, the `tests/test_packages.py` checks that every
expected command is on `PATH`, and a second run that must report `changed=0` to prove the
playbook is idempotent.

## Licence

MIT, see [LICENSE](LICENSE).
