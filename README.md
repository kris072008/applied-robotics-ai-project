# Applied Robotics and AI Project

Project repository for the Applied Robotics and AI Project module (PSB Academy / University of Hertfordshire).
Maintained by **Krishna Mahajan** ([@kris072008](https://github.com/kris072008)).

## About the project

This project develops a robot that combines hardware (sensors, motors, a microcontroller) with AI and Python software to carry out an autonomous task. The repository holds the source code, documentation and progress history for the project.

## Repository structure

```
applied-robotics-ai-project/
├── src/        # Source code (Python / Arduino)
├── docs/       # Documentation, diagrams and screenshots
├── .gitignore  # Python files Git should ignore
└── README.md   # This file
```

## Getting started

```bash
git clone https://github.com/kris072008/applied-robotics-ai-project.git
cd applied-robotics-ai-project
```

Requirements: Git, Python 3.10+, and the Arduino IDE for any microcontroller code.

## Project management

Tasks are tracked on a Trello board with these lists: **Backlog → To Do → In Progress (WIP limit: 3) → Review → Done**.
Each card has a label (Hardware, Software, Documentation), a due date and, where relevant, a link to its commit or pull request through the Trello GitHub Power-Up.

## Workflow and branching strategy

- `main` always holds stable, working code.
- New work goes on a feature branch, for example `feature/sensor-reading` or `fix/motor-speed`.
- Commit often, with clear messages that say what changed (e.g. `Add ultrasonic sensor reading`).
- When a feature is finished, push the branch, open a **pull request** and merge it into `main`.
- After merging, move the Trello card to **Done** and link the PR.

## Git basics: add, commit, push

| Command | What it does | Where the change is afterwards |
|---|---|---|
| `git add <file>` | Moves changes into the **staging area**, choosing what goes into the next commit | Staged, not saved in history yet |
| `git commit -m "msg"` | Saves the staged changes as a **snapshot** in local history, with a message | Saved locally, on your computer only |
| `git push` | Uploads your local commits to the **remote** repository on GitHub | On GitHub, visible to the team and backed up |

Useful extras: `git status` shows what has changed and what is staged, and `git log --oneline` shows the commit history.

## Author

Krishna Mahajan, BSc Robotics and AI

## About the project
firefly-brain simulates part of the fruit fly (Drosophila) connectome with leaky integrate-and-fire neurons. Game events stimulate sensory neurons, and motor neuron spikes become fly movement.
