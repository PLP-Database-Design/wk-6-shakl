# Tests — Software Testing Team

This directory contains the automated test artifacts and test automation suites for the wk-6-shakl project: Selenium/Simple Python scripts and a Cypress E2E project. The README below explains structure, how to run tests, where outputs are stored, and common troubleshooting steps.

## Repository layout (tests/)
- defect-log.md
- selenium_test_results.csv           — single-run summary CSV (metadata + timestamped messages)
- test-cases.md                       — test cases / acceptance criteria
- test-plan.md                         — test plan and scope
- scripts/
  - test.py                            — Selenium Python test script (main Selenium test)
  - cypress-test/
    - package.json
    - cypress.config.js
    - cypress/
      - e2e/                            — Cypress test specs
      - fixtures/
      - screenshots/                    — Cypress screenshots produced during runs
      - support/

## Quick prerequisites (Linux)
- Python 3.10+ and pip
- Google Chrome (or Chromium) and a matching ChromeDriver on PATH (or use webdriver-manager)
- Node.js (16+) and npm for Cypress
- pip packages: selenium (install with pip)
- For Cypress: npm ci (or npm install) inside tests/scripts/cypress-test

Example commands:
- Python + Selenium:
  - python3 -m pip install selenium
  - (optionally) python3 -m pip install webdriver-manager
- Cypress:
  - cd tests/scripts/cypress-test
  - npm ci

## Run the Selenium test (simple, single-file)
From repository root:
- python3 tests/scripts/test.py

What to expect:
- A single CSV summary file will be created/overwritten at:
  - tests/selenium_test_results.csv
- The CSV contains metadata rows followed by a `messages` section where each printed/logged message appears on its own row (timestamped).
- If enabled, screenshots on failure will be saved (check a `screenshots/` folder next to the script or the project root).

Example output file:
- tests/selenium_test_results.csv

Notes:
- The Selenium test is built to be self-contained; it collects timestamped messages into an in-memory list and writes a single CSV at the end.
- If you see a WebDriverException mentioning BiDi / "Unable to find url to connect to from capabilities", use the non-BiDi approach (remove calls to driver.script) or ensure Chrome + ChromeDriver versions support BiDi (ChromeDriver v115+ and matching Chrome).

## Run Cypress tests
From the Cypress project folder:
- cd tests/scripts/cypress-test
- npm ci
- Open interactive runner:
  - npx cypress open
- Run headless:
  - npx cypress run
- Run a single spec:
  - npx cypress run --spec "cypress/e2e/app.cy.js"

Artifacts:
- Cypress screenshots: tests/scripts/cypress-test/cypress/screenshots
- Cypress videos (if enabled): tests/scripts/cypress-test/cypress/videos

## Test plan, cases, defects
- test-plan.md: overall test scope, objectives, and strategy.
- test-cases.md: detailed test cases and expected results.
- defect-log.md: recorded defects and their status.

Keep these documents updated as tests or scope change.

## Troubleshooting & tips
- Chrome/ChromeDriver mismatch often causes failures — ensure versions align.
- If the Selenium test blocks (e.g., waiting for input), remove any manual input() calls to run in CI.
- For CI: run the Selenium script headless by setting Chrome options (add arguments like `--headless=new`, `--no-sandbox`, `--disable-dev-shm-usage`) or use a containerized Chrome.
- To capture richer browser console messages without BiDi: inject a small JS console wrapper into pages or use Chrome DevTools Protocol via execute_cdp_cmd.

## Extending tests
- Selenium: break the monolithic script into functions and convert to pytest for better reporting, fixtures, and CI integration.
- Cypress: add more specs under `cypress/e2e/`, enable video recording in `cypress.config.js`, and add custom commands in `cypress/support`.

## Files of interest
- tests/scripts/test.py — primary Selenium script (logging and CSV writing logic)
- tests/selenium_test_results.csv — last-run CSV summary
- tests/scripts/cypress-test/cypress/e2e — Cypress test specs and examples
- tests/defect-log.md — tracked defects

## Acknowledgements
- ChatGPT (OpenAI) was used to help design the logging and CSV reporting logic used in the Selenium test scripts. This README was generated/expanded with assistance.
