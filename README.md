# Student Housing Decision Support System

A Model-driven Decision Support System (DSS) using vector-normalized TOPSIS for multi-criteria student accommodation selection. Developed for the Information Systems Management (ISM) course at International University (VNU-HCM).

### Key Milestones:
- **November 22, 2026:** Baseline MVP operational (budget filter, priority sliders, TOPSIS ranking, calculation details).
- **November 29, 2026:** Feature freeze (30 synthetic rooms, weight presets, manual verification).
- **December 07, 2026:** Final report (PDF) and 20-minute presentation slides sign-off.
- **December 08–10, 2026:** Timed group rehearsals (20 min) and Q&A defense preparation.
- **December 12, 2026:** Final seminar presentation and live demonstration.

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

### Documentation & Planning Links
- [Detailed Internal Week 1 Plan (Vietnamese)](docs/ke-hoach-tuan-1.md)
- [Report Structure & Seminar Presentation Guidelines](docs/README.md)
- [Dataset Schema & Scoring Rubric](data/README.md)

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

## Project Scope & Implementation Status

The application provides:
- Hard budget filtering before TOPSIS ranking.
- Five adjustable criterion weights with automatic vector normalization.
- TOPSIS ranking showing top 3 options, all eligible results, and calculation details ($D^+$, $D^-$, and relative closeness score $C_i$).
- A verified baseline dataset of 30 synthetic rooms with explicit scoring rubrics.

**Key tasks before final seminar:**
- Verify an independently hand-calculated 3-room example (`docs/topsis-worked-example.md`).
- Implement 3 preset weight profiles (Budget-focused, Campus-focused, Space/Amenities-focused) for instant sensitivity demonstration.
- Add CSV export of ranked results and custom CSV upload support.
- Finalize the complete 25–35 page academic report (PDF) and 20-minute presentation slides (18–20 slides).
- Record an offline demonstration video backup.

**Explicitly outside scope:** User authentication, payment processing, web scraping, and live map/geocoding APIs.

## References

- [Streamlit: Create an app](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [Towards Explainable TOPSIS](https://arxiv.org/abs/2306.07706)
