# Student Housing Decision Support System

A final project using TOPSIS for multi-criteria housing decisions. Seminars begin on **December 12, 2026**. The team begins work on **November 21**; the immediate target is a validated Week 1 baseline by **November 27**. The remaining timeline will be set after the first team review.

## Local setup

Install Python 3.11 or later and Git. Run these commands in PowerShell:

```powershell
git clone https://github.com/KhanhTaiTran/Decision-support-system.git
cd Decision-support-system
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m streamlit run app.py
```

On macOS/Linux, replace `.\.venv\Scripts\python.exe` with `.venv/bin/python`.
Virtual environment activation is optional. Stop the application with Ctrl+C.

On Windows, use the official Python distribution from python.org. If `python` resolves to MSYS2/Git Bash and creates `.venv/bin` instead of `.venv/Scripts`, use `py -3 -m venv .venv` with the official Python installation to avoid compiling dependencies from source.

## Project structure

```text
app.py                       # Streamlit interface and integration
src/housing_dss/
  criteria.py                # Labels, units, and cost/benefit directions
  data.py                    # CSV loading and validation
  topsis.py                  # Ranking algorithm independent of the UI
  ui/                        # Streamlit presentation modules
    preferences.py           # Budget and priority controls in the sidebar
    results.py               # Ranked-room tables and calculation details
data/
  rooms_sample.csv           # Thirty synthetic rooms for the starter demo
  README.md                  # Data schema and scoring rubric
tests/                       # Algorithm and data tests
docs/                        # Methodology, report, slides, and demo materials
.github/workflows/tests.yml  # Automated checks on pushes and pull requests
```

## Module ownership

- **Hồ Ngọc An**: requirements and report coordination.
- **Châu Thành Phát**: `src/housing_dss/topsis.py`, methodology, and sensitivity analysis.
- **Trần Khánh Tài**: `app.py`, packaging, interface, CSV import/export, and integration.
- **Trần Việt Trung**: `tests/`, demo scenarios, integration testing, and backup video.

Coordinate schema and function signature changes with the integration owner. Each member writes the report section covering their own contribution.
All project documentation, interface text, messages, comments, and presentation materials must be written in English. Preserve team members' names as provided.

[Google Sheets project plan and deadlines](https://docs.google.com/spreadsheets/d/1wgrpr-N_P16rFBHk9lmXNfw0crfg0Z2PDYrWAIVx7LE/edit)

[Detailed internal Week 1 plan (Vietnamese)](docs/ke-hoach-tuan-1.md)

## Branches and pull requests

Create a separate branch for each task:

```powershell
git switch main
git pull --ff-only
git switch -c feat/topsis-sensitivity
# Edit files and run tests before committing.
git add src/housing_dss/topsis.py tests/test_topsis.py
git commit -m "Add sensitivity comparison"
git push -u origin feat/topsis-sensitivity
```

Open a pull request into `main`, request a teammate's review, and wait for CI to pass before merging. Do not force-push to `main`. The repository owner must invite the other three members through GitHub Settings → Collaborators.

## Checks before pushing

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m compileall -q app.py src tests
```

## Starter scope

The starter implements budget filtering, five adjustable criterion weights, TOPSIS ranking, the top three options, and calculation details. Data is synthetic. Scores depend on the candidate set and are not probabilities of suitability. Ties are displayed by ID; indistinguishable alternatives receive 0.5. An empty candidate set prompts the user to increase their budget.

Remaining team tasks: expand the dataset, verify an independently calculated example, add CSV import/export, compare three weight profiles, improve explanations, and prepare the report and slides. Authentication, payments, scraping, and map APIs are outside the current scope.

## References

- [Streamlit: Create an app](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [Towards Explainable TOPSIS](https://arxiv.org/abs/2306.07706)
