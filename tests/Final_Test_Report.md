
CleanCity – Software Test Report 

Version: 2.0
Date: November 19, 2025
Testing Cycle: November 5 – November 18, 2025
Prepared By: Shanice Chepkwony

Test Manager: Shanice Chepkwony

Risk Analyst: Mark Mwangi Gaituri

Test Executor: Ian Macharia


1. Executive Summary

This Software Test Report documents the results of the QA testing effort performed on the CleanCity Waste Pickup Scheduler Web Application (v1.0).
Testing activities focused on validating functional requirements defined in the Functional Requirements Specification (FRS), assessing security and code quality, and verifying user experience across devices and browsers.

Overall Result: NOT READY for Production

Testing uncovered significant security flaws, data persistence failures, and access control vulnerabilities.

Key Highlights

14 test cases executed

Pass rate: 36%

8 failed, 1 deferred, 5 passed

Critical security issues:

Plain-text password storage

Privilege escalation through localStorage

Missing input sanitization (XSS)

Functional defects:

Pickup requests not saving

Dashboard metrics inconsistent

Community posts fail on refresh

Static Code Analysis (SonarCloud):

22 code smells, 5 security hotspots

Poor maintainability index

Cross-browser testing:

Works on Chrome/Firefox; minor layout issues on Edge and Safari

Recommendation

A full bug fix + regression testing cycle is required before any deployment.
Security vulnerabilities must be addressed as priority.

2. Test Objective

The objectives of this test cycle were:

✔ Validate all functional requirements 
✔ Assess usability, performance, accessibility & responsiveness
✔ Identify security vulnerabilities 
✔ Conduct manual and automated functional tests
✔ Analyze code quality using SonarCloud
✔ Evaluate application stability over multiple user sessions
✔ Ensure role-based access restrictions function correctly

3. Scope of Testing
3.1 Functional Test Coverage

Testing covered all major modules:

Authentication & Authorization

Registration, login/logout

Form validation

Session management

User role enforcement

Waste Pickup Scheduling

Form validation

Date rules & business logic

Data persistence to localStorage

Edit/cancel behavior

Dashboard & Analytics

Charts, trends, and statistics

Badge/achievement system

Content Management

Blog creation

Comment posting

Content moderation

Community Features

Posts

Likes/comments

Profile updates

Admin Functions

User management

Pickup approval/rejection

Request filtering

Notifications

Notification list

Mark as read

Unread counter

3.2 Non-Functional Testing
Security Testing

Authentication bypass

Direct object reference checks

Cross-site scripting (XSS) attempts

Password encryption verification

Session security

Performance

Page load times

JS memory usage

Load with 50+ records

Compatibility

Chrome, Firefox, Edge, Safari

Responsive checks (desktop/tablet/mobile)

Accessibility

WCAG 2.1 checks

Screen reader compatibility

Keyboard navigation

3.3 Out-of-Scope

❌ Email alerts (not implemented)
❌ Payment integration (not part of MVP)
❌ Full penetration testing
❌ Backend API testing (app is fully client-side)
❌ Stress testing with >100 concurrent users

4. Test Environment
Category	Details
Frontend	React.js SPA
Storage	localStorage only
Browsers	Chrome 129, Firefox 127, Edge 127, Safari 17
OS	Windows 10, macOS Sonoma, Android, iOS
Automation Tools	Selenium 4.x + Python
Static Analysis	SonarCloud
Defect Tracking	GitHub Issues
Management	Jira (Scrum board)

5. Test Approach
5.1 Techniques Used

Equivalence Partitioning (EP)

Boundary Value Analysis (BVA)

Decision Tables

Negative Testing

Risk-Based Testing (RBT)

Exploratory Testing

Ad-hoc testing for security vulnerabilities

5.2 Execution Summary

80 total test cases prepared

14 executed during this sprint (high-priority only)

11 automated

3 manual

6. Test Results
6.1 Summary
Severity	Total	Passed	Failed	Deferred
Critical	5	0	5	0
High	6	2	3	1
Medium	2	2	0	0
Low	1	1	0	0
TOTAL	14	5	8	1

Pass Rate: 36%
Fail Rate: 57%
Deferred: 7%

7. Key Test Cases & Results (Examples)
TC-AUTH-001 – Password Security

Expected: Passwords hashed or encrypted
Actual: Stored in plain text

❌ FAIL – Critical

TC-AUTH-002 – Privilege Escalation

Steps: Modify localStorage → role = "admin"
Expected: Blocked
Actual: Admin dashboard is accessible

❌ FAIL – Critical

TC-WASTE-001 – Pickup Scheduling Persistence

Expected: Request saved under pickupRequests
Actual: No data saved

❌ FAIL – Critical functional issue

TC-DASH-004 – Dashboard Statistics

Expected: Accurate user-specific totals
Actual: Shows global totals mixing all users

❌ FAIL – High severity

TC-COMM-002 – Post Persistence on Refresh

Expected: Community posts remain after refresh
Actual: Posts disappear

❌ FAIL

8. Defects Summary
8.1 Critical Defects
Defect ID	Description	Severity	Status
DEF-001	Password stored in plain text	Critical	Open
DEF-002	Privilege escalation possible	Critical	Open
DEF-003	Pickup request not saved	Critical	Open
DEF-004	Missing input sanitization (XSS-risk)	Critical	Open
DEF-005	Dashboard metrics inaccurate	Critical	Open

8.2 High Severity Defects
Defect ID	Description	Severity	Status
DEF-006	Community posts vanish on reload	High	Open
DEF-007	Admin unable to filter requests correctly	High	In progress
DEF-008	Notification counter not updating	High	Deferred

8.3 Medium / Low Defects

Missing alt text

Mobile layout breaks on iPhone Safari

Some inconsistent button colors

9. Requirement Traceability Matrix (RTM)
FRS Requirement	Test Case	Status
FR-001 (Register)	AUTH-003	PASS
FR-004 (Login)	AUTH-004	FAIL
FR-012 (Pickup scheduling)	WASTE-001	FAIL
FR-020 (Tracking)	WASTE-004	PASS
FR-023 (Dashboard)	DASH-001	FAIL
FR-041 (Community posts)	COMM-001	PASS
FR-042 (Likes/comments)	COMM-002	FAIL
FR-053 (Admin request mgmt)	ADMIN-003	FAIL

10. Test Metrics

Defect Density: 0.57 defects per test case

Automation Coverage: 78%

Requirements Coverage: 62%

Execution Coverage: 17% of all 80 planned test cases

11. Risks & Impact Analysis
Major Risks Identified
Risk	Impact	Likelihood	Rating
Weak security	Credential leaks, hacked admin panel	High	Severe
Data not persisted	Core functionality fails	High	Severe
Incorrect metrics	Misleading analytics	Medium	High
No backend	All security depends on browser	High	Severe

12. Recommendations

Before release, the following must be done:

🔐 1. Implement secure password hashing

bcrypt, Argon2, or PBKDF2

Remove password from localStorage

🛡️ 2. Enforce server-side authentication (backend needed)

LocalStorage is not secure for auth or roles.

🚫 3. Fix privilege escalation

Never trust client-side roles

Revalidate role on every access

🗃️ 4. Fix pickup scheduling database logic

Ensure localStorage array initialisation & push logic works.

📊 5. Rebuild dashboard metrics

Separate user-specific totals from global totals.

🧪 6. Conduct full regression suite after fixes
🌐 7. Add backend API and database in v2.0

The application depends too heavily on localStorage.

13. Conclusion

CleanCity v1.0 demonstrates solid UI design and feature intentions, but critical issues prevent release.

❌ Release Status: NOT APPROVED
 Requires rework, fixes, and retesting

The QA team recommends a Fix → Retest → Regression → Final Acceptance cycle before deployment.








