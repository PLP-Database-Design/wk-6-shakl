# CleanCity QA Test Plan

**Project:** CleanCity - Waste Pickup Scheduler  
**Version:**  1.0
**Date:** November 5, 2025  
**Prepared by:** Software Testing Team  
**Reviewed by:**   Ian Macharia

---

## 1. Objective
The objective of this test plan is to ensure the CleanCity application functions as intended, providing a smooth and accessible waste pickup scheduling experience for users and administrators. Testing will validate functional and non-functional requirements, including UI, accessibility, performance, and security.

---

## 2. Scope
### In Scope
- User registration and login
- Scheduling waste pickups
- Viewing and updating pickup requests
- Admin dashboard functionality
- Blog and community post features
- Accessibility and responsiveness testing

### Out of Scope
- Payment gateway integration
- 
---

## 3. Test Strategy
### Types of Testing:
- **Functional Testing:** Verify core app functions (registration, login, scheduling).
- **UI/UX Testing:** Check layout, responsiveness, and user navigation.
- **Cross-Browser Testing:** Chrome, Firefox, Edge, Safari.
- **Performance Testing:** Load handling with multiple users.

### Tools:
- Jest automated testing
- Chrome DevTools for manual testing
- Jira for issue tracking and project

---

## 4. Test Environment
- **Browsers:** Chrome, Firefox, Safari, Edge 
- **Devices:** Desktop, 
- **OS:** Windows 10+, 
- **Data Source:** `tests/test-data.md`

---

## 5. Roles and Responsibilities
| Role | Name | Responsibilities |
|------|------|------------------|
| **Test Manager**  | Shanice Chepkwony     | Oversees the entire testing process, plans schedules, assigns tasks, and ensures deliverables meet deadlines. |
| **Risk Analyst**  | Ian Macharia | Identifies potential risks, assesses impact and likelihood, and develops mitigation strategies |
| **Test Executor** | Mark Mwangi Gaituri | Executes test cases, documents results, and reports defects in issue tracking tools.                          |



---

## 6. Test Deliverables
- `test-plan.md` — Overall strategy  
- `test-cases.md` — Detailed test cases  
- `test-data.md` — Input and validation data  
- `defect-log.md` — Bug tracking log  
- Test summary report and video demo  

---

## 7. Entry and Exit Criteria
**Entry:**
- Application deployed on test environment  
- Test data ready and accessible  

**Exit:**
- 

---

## 8. Schedule
| Phase | Activity | Due Date |
|--------|-----------|-----------|
| Phase 1 | Setup & Planning | Nov 5, 2025 |
| Phase 2 | Test Case Creation | Nov 7, 2025 |
| Phase 3 | Execution & Defect Reporting | Nov 8–15, 2025 |
| Phase 4 | Final Report & Video Demo | Nov 18, 2025 |

---

## 9. Risks & Mitigation

| ID   | Feature (Testing Area)            | Risk Description | Likelihood | Impact   | Priority | Mitigation Strategy (Test Focus) |
|------|----------------------------------|------------------|------------|----------|----------|----------------------------------|
| A-01 | User Login/Registration | Security: Passwords are stored, retrieved, and compared in plain text in localStorage. Critical vulnerability. | High | Critical | High | (Security Test) Log in with sample user and inspect `cleancity_users` in DevTools to confirm passwords are visible in plain text. |
| A-02 | Session Management | Security/Authorization: User role and session management are fully client-side and easily tampered with to escalate privileges. | High | Critical | High | (Security Test) Log in as normal user, modify `localStorage.currentUser.role` to `admin`, refresh, and verify admin access. |
| A-03 | Password Validation | Functional/Security: Weak password rule — minimum length of 3 characters. | High | High | High | (Functional Test) Attempt to register users with 1–2 character passwords and confirm validation incorrectly passes. |
| A-04 | User Management | Security: No authorization checks in user functions (IDOR vulnerability). Any user can modify/delete others. | High | High | High | (Security Test) As normal user, run `dataService.deleteUser('2')` and confirm the admin user is deleted. |
| A-05 | User Registration | Security: User enumeration possible based on differing responses for existing vs non-existent emails. | Medium | High | Medium | (Security Test) Register using known and unknown emails; analyze response messages or delays revealing user existence. |
| A-06 | User Login | Functional: Login success message appears briefly before redirect, causing UX confusion. | Medium | Low | Low | (Usability Test) Log in and verify the “Login successful! Redirecting...” message appears before dashboard navigation. |
| W-01 | Pickup Scheduling | Functional: “Schedule Pickup” form does not save any data; new requests are discarded. | High | Critical | High | (Functional Test) Submit a pickup request, check `localStorage.pickupRequests` or Admin view, and verify it's missing. |
| W-02 | Request Management | Security: Admin page (/admin) has no access control; any user or unauthenticated user can modify all requests. | High | Critical | High | (Security Test) As normal user or logged out, navigate to `/admin` and attempt to modify request status. |
| W-03 | Status Tracking | Functional: Status changes do not record who completed the action; no audit trail. | Medium | High | Medium | (Audit Test) Update status to Completed and inspect localStorage — verify no `completedBy` or `completionDate`. |
| W-04 | Pickup Scheduling (Negative Testing) | Functional: Past dates are allowed as “Preferred Pickup Date”, enabling impossible scheduling. | High | Medium | Medium | (Negative Test) Schedule a date in the past and verify the system accepts it without warnings. |
| D-01 | Admin/Dashboard Data Flow | Security/Authorization: Dashboard displays global stats to all users, not just admins. | High | High | High | (Security Test) Log in as non-admin, open Dashboard, and confirm global statistics are shown. |
| D-02 | Data Visualization (Bar Chart) | Functional: Malformed or null dates cause corrupted keys, potentially breaking charts. | Medium | Medium | Medium | (Data Integrity Test) Insert request with null/empty date and verify Dashboard renders without crashing. |
| D-03 | Missed Pickups Metric | Functional: Metric ignores “Pending” requests, leading to misleading operational insights. | Medium | Medium | Medium | (Metric Test) Add many Pending requests and confirm metric only counts explicit Missed statuses. |
| D-04 | Data Visualization (Bar Chart) | Functional: Chart cannot scale for large data volumes; labels overlap or truncate. | Low | Low | Low | (Stress Test – Deferred) Add high-volume data across 15+ months and verify chart behavior. |

---

# Coverage Summary

## Risk Coverage Overview
- Total Unique Risks Identified: 14  
- Risks Covered by a Test Case (Tested or Deferred): 14  

All identified risks are associated with at least one test case.

---

## Coverage Metrics

| Metric | Calculation | Percentage |
|--------|-------------|------------|
| Tested Risks Percent | (14 / 14) × 100 | 100% |
| Untested Risks Percent | (0 / 14) × 100 | 0% |

---

## Conclusion

All 14 risks identified in the risk analysis have been fully mapped to corresponding test cases. Although one stress test (DASH-TC-004) was deferred, overall risk coverage remains at 100%.



## 10. References
- 
