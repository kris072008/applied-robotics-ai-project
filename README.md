# firefly-brain: Applied Robotics and AI Project

Project repository for the Applied Robotics and AI Project module (PSB Academy / University of Hertfordshire).
Maintained by Krishna Mahajan (@kris072008).

## About the project

firefly-brain simulates part of the fruit fly (*Drosophila*) connectome using leaky integrate-and-fire (LIF) neurons.

1. **Sensory input** - game events (food left, food right, danger) stimulate sensory neurons.
2. **Simulation** - spikes spread through the connectome using the LIF model.
3. **Motor output** - spikes from motor neurons become fly movement (turn left, turn right, move forward).

This is a working prototype using a small sample connectome. The next step is to load a real subset of the FlyWire dataset.

## Repository structure

    applied-robotics-ai-project/
    ├── src/
    │   ├── sensor.py              # Ultrasonic sensor reading module
    │   ├── connectome_loader.py   # Loads connectome data into a graph
    │   ├── lif_simulation.py      # Leaky integrate-and-fire spiking simulation
    │   ├── sensory_mapping.py     # Game events -> sensory neurons
    │   └── motor_mapping.py       # Motor neuron spikes -> fly movement
    ├── data/
    │   └── sample_connectome.csv  # Small sample connectome
    ├── tests/
    │   └── test_simulation.py     # Unit tests for the full pipeline
    ├── docs/                      # Documentation and screenshots
    └── README.md

## Getting started

Requirements: Git and Python 3.10+.

    git clone https://github.com/kris072008/applied-robotics-ai-project.git
    cd applied-robotics-ai-project
    PYTHONPATH=src python3 src/motor_mapping.py               # run the pipeline
    PYTHONPATH=src python3 -m unittest discover -s tests -v   # run the tests

## Project management (Trello)

Tasks are tracked on a Trello board, linked to GitHub with the Trello GitHub Power-Up.

| List | Purpose |
|------|---------|
| Backlog | Future ideas, not planned for this sprint |
| To Do | Planned for this sprint |
| In Progress | Being worked on (**WIP limit: 3**) |
| Done | Finished and merged, with the PR attached |

**Labels:** Feature, Testing, Setup, Hardware, Assignment, Future.

## Workflow and branching strategy

- `main` always holds stable, working code. Nothing is committed to it directly.
- Every change, including documentation, goes on its own branch: `feature/...`, `fix/...` or `docs/...`.
- Commit often, with clear messages that say what changed.
- When the work is finished: push the branch, open a pull request, merge it into `main`.
- After merging: attach the PR to its Trello card and move the card to Done.

## Git basics: add, commit, push

| Command | What it does | Where the change is afterwards |
|---------|--------------|-------------------------------|
| `git status` | Shows changed, untracked and staged files | - |
| `git add <file>` | Moves changes into the staging area | Staged, not saved in history yet |
| `git commit -m "msg"` | Saves staged changes as a snapshot with a message | Saved locally |
| `git push` | Uploads local commits to GitHub | On GitHub, visible to others |
| `git pull` | Downloads and merges the latest changes from GitHub | Up to date locally |

`git log --oneline --graph --all` shows the full history, including how each branch was merged.

## Author

Krishna Mahajan, BSc Robotics and AI
