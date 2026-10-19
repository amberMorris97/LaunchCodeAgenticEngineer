# 1. Quality Rubric

## 1.1 Dimensions
Agent A: Accurate file review, test coverage, logical commits
Agent B: Accurate file review, docstring coverage, readme consistency, logical commits

### 1.1.1 Accurate file review

Agent A: Measures whether the agent reviewed the correct files. A high score requires a test file for module_x.py.
Agent B: Measures whether the agent reviewed the correct files. A high scorre requires docstrings added to module_y.py.

### 1.1.2 Test/Docstring coverage
Agent A: Measures whether the agent wrote tests for the named file. A high score requires passing tests in the correct file for all public functions in module_x.py.
Agent B: Measures whether the agent wrote docstrings for the named file. A high score requires accurate docstrings added to all public functions in module_y.py.

### 1.1.3 Logical Commits 
Agent A & B: Measures whether the agent made commits in logical chunks. A high score requires the agent to have made regular, descriptive commits. 

### 1.1.4 Readme consistency
Agent B: Measures whether the agent accurately reviewed project structure. A high score requires the agent to have created README.md with an accurate outline of exisitng project structure. 

Alternatives considered: a binary pass/fail checklist with one item per acceptance criterion. Ruled it out because each agent needs to take multiple steps, and can not be described in one or two criterion. 