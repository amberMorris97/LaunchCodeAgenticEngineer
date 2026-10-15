Agent A's workflow reviews the code in module_x.py, creates tests for all public functions without modifying the code in module_x.py itsself, and makes commits in logical chunks. 

Agent B's workflow reviews the code in module_y.py, adds docstrings to all the public functions, reviews the project structure, updates README.md to reflect current project structure, without modifying any test files and committing in logical chunks.

### Agent A Trigger: 

A developer invokes claude "Write unit tests for module_x.py.

- Create tests/test_module_x.py

- Cover all public functions

- Do not modify module_x.py itself

- Commit in logical chunks" from the repo root 

### Agent B Trigger: 

A developer invokes claude "Improve documentation for module_y.py and update the README.

- Add docstrings to all public functions in module_y.py

- Update README.md to reflect current project structure

- Do not modify any test files

- Commit in logical chunks" from the repo root

For Agent A, if a public function exists, the agent creates a test for it. 
For Agent B, if a public function exists, the agent creates a docstring for it.

### Agent A's Actions: 

1. Reviews code in module_x.py
2. Creates tests for each public function
3. Makes commits in logical chunks 

### Agent B's Actions: 

1. Reviews code in module_y.py
2. Creates docstring for each public function 
3. Reviews project structure 
4. Creates README.md going over project structure 
5. Makes commits in logical chunks

### Agent A Acceptance Criteria: 
- The agent correctly reviews all public functions and creates passing tests
- The agent does not modify module_x.py 
- The agent makes commits in logical chunks 

### Agent B Acceptance Criteria: 
- The agent correctly reviews all public functions and creates logical docstrings
- The agent does not modify module_y.py
- The agent correctly reviews project structure and accurately outlines it in README.md 
- The agent makes commits in logical chunks