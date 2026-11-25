# solid-umbrella
My Test Automation Portfolio


# 🧪 Software Test Engineer Portfolio

> An end-to-end demonstration of the Software Testing Life Cycle (STLC) and test automation, from requirements analysis to test reporting and automated checks.

**Author:** Olugbemiga Ojumu · Test Engineer · ISTQB Certified
**Focus:** Manual & Automated Testing · API testing · CI/CD-integrated QA · Experience in Automotive Software

---

## 📌 Overview

This repository shows how I approach quality across the full testing lifecycle. It pairs **professional-style STLC documentation** with **working test automation code**, so you can see both how I plan and think about testing and how I execute it.

**Application under test:** [Grocery Mate Demo Online Grocery Store (https://grocerymate.masterschool.com/)]

---

## 🗂️ Repository Structure

```
solid-umbrella/
├── STLC/
│   ├── requirements.md                 # Requirement analysis & testability review
│   ├── test plan.md                    # Scope, strategy, risks, entry/exit criteria
│   ├── test case design.md             # Test cases, techniques, coverage
│   ├── test env setup.md               # Environment, tools, test data
│   ├── functional test execution.md    # Execution results & defect log
│   └── test reporting.md               # Summary, metrics, conclusions
├── Test automation/
│   └── test-code.py                    # Automated test scripts (Python + Selenium)
└── README.md
```

---

## 🔄 STLC Walkthrough

| Phase                   | Document              | What it demonstrates                                                            |
|-------------------------|-----------------------|---------------------------------------------------------------------------------|
| 1. Requirement analysis | `Requirements.md`     | Reviewing requirements for clarity, ambiguity, and testability                  |
| 2. Test planning        | `Test Plan Design.md` | Scope, approach, risk assessment, entry/exit criteria                           |
| 3. Test case design     | `Test Case Design.md` | Structured cases using [e.g. equivalence partitioning, boundary value analysis] |
| 4. Environment setup    | `Test Env Setup.md`   | Tooling, configuration, and test data preparation                               |
| 5. Test execution       | `Test Execution.md`   | Running cases, logging results and defects                                      |
| 6. Test closure         | `Test Reporting.md`   | Summarising outcomes, metrics, and lessons learned                              |

---

## 🤖 Test Automation

`Test_Automation` contains automated tests written in **Python** with **Selenium** [and **Pytest**].

**Highlights**
- Page interactions: login, search, cart, checkout
- Explicit waits instead of hard sleeps for stability
- Pytest fixtures and parametrization for reusable, data-driven tests
- Assertions that map back to test cases in `Test Case Design.md`
- Building stable XPath expressions for complex elements

### Running the tests

```bash
# 1. Clone the repository
git clone https://github.com/olugbemigaojumu/solid-umbrella.git
cd solid-umbrella

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install selenium pytest

# 4. Run the tests
pytest "Test automation/test-code.py" -v
```

**Prerequisites:** Python 3.x, Google Chrome, and a compatible WebDriver (Selenium 4.6+ manages this automatically).

---

## 🛠️ Tools & Skills Demonstrated

| Area                      | Tools / Techniques                                                                      |
|---------------------------|-----------------------------------------------------------------------------------------|
| Test automation           | Python, Selenium, Pytest                                                                |
| API testing               | Postman                                                                                 |
| Test management & defects | Jira                                                                                    |
| Version control & CI/CD   | Git, GitHub                                                                             |
| Test design               | Equivalence partitioning, boundary value analysis, decision tables, exploratory testing |
| Documentation             | Test plans, test cases, execution & summary reports                                     |

---

## 👤 About Me

I'm a Software Test Engineer, and I have worked with various top tech companies and Innovation Labs in the tech industry, including the Automotive industry. I have about 7 years of experience in software testing. I'm ISTQB certified and currently studying for the **CTAL-TM (Advanced Level Test Manager)** as I grow toward test lead and management responsibilities. My background is in Mechanical Engineering, and I'm building expertise in AI development.

📫 **Connect:** [LinkedIn](https://www.linkedin.com/in/olugbemiga-ojumu/)

---

## 🚀 Roadmap

- [ ] Expand automation coverage to more flows
- [ ] Add API test suite (Postman collection)
- [ ] Integrate tests into a CI pipeline (GitHub Actions)
- [ ] Add HTML test reports

---

*Built to showcase practical QA skills: planning, design, execution, automation, and reporting.*