# Learn CI with an equation solver

A small Python project for learning **continuous integration (CI)**. It solves
linear and quadratic equations, has seven tests, and has a GitHub Actions
workflow that runs them automatically. Only the Python standard library is
needed.

## 1. Run the application

From the repository root:

```bash
python equations.py linear 2 -6
python equations.py quadratic 1 -3 2
python equations.py quadratic 1 0 1
```

The outputs are `x = 3`, then `x = 1` and `x = 2`, then `No real solutions`.
The solver handles **real roots only**. A zero leading coefficient is rejected
rather than silently changing the type of equation.

## 2. Run the tests yourself

```bash
python -m unittest discover -s tests -v
```

Read [`tests/test_equations.py`](tests/test_equations.py). Each `test_...`
method supplies an input and checks an expected result. There are cases for
two roots, one repeated root, no real roots, invalid input, and the command
line output. A failed assertion makes the command exit with a nonzero status.

## 3. See the automated run

Open the **Actions** tab and select the newest **CI** run. GitHub reads
[`.github/workflows/ci.yml`](.github/workflows/ci.yml) when code is pushed,
when a pull request is opened or updated, or when you use **Run workflow**.
For each Python version in the matrix (3.11 and 3.13), GitHub starts a fresh
Ubuntu runner, checks out that commit, sets up Python, runs the tests, and
tries the application. A green check means every step passed. A red X means
at least one step failed; open that step to read the error.

These checks do not publish or deploy the application.

## 4. Make a safe practice change

Create a branch (in GitHub, use the branch selector and **New branch**).
In `tests/test_equations.py`, temporarily change the expected result in
`test_linear_equation` from `3` to `4`. Commit the change on your branch and
watch the CI run turn red. Open **Run unit tests** to see the assertion
failure. Change the expected result back to `3`, commit again, and watch the
new run turn green. You can open a pull request to see the same check appear
beside the proposed change, then close the practice pull request and delete
the branch if you wish. Keep `main` green.

## 5. Extend the project

Try adding a test for `solve_linear(0.5, -1)` before changing the program.
Then add a feature of your own, such as an option to print the discriminant,
with a test for its output. Run the tests locally and push to see CI repeat
the checks on GitHub.

The project is available under the [MIT License](LICENSE).
