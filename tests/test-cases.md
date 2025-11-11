CleanCity - Test Cases

This document lists all test cases executed during the QA phase of the **CleanCity - Waste Pickup Scheduler** project.  
It serves as a reference for what was tested, expected outcomes, and verification status.

---

## Test Cases Table



| Test Case ID | Date       | Feature                     | Test Description | Steps to Execute | Test Data | Expected Result | Actual Result | Status | Tested By |
|--------------|------------|-----------------------------|------------------|------------------|-----------|-----------------|---------------|--------|-----------|
| **AUTH-TC-001** | 2025-11-05 | User Login/Registration | (Security) Verify passwords are stored in plain text. | 1. Log in with `user@cleancity.com`.<br>2. Open DevTools → Application → Local Storage.<br>3. Inspect `cleancity_users`. | Login: user@cleancity.com<br>Pass: password123 | Password should appear in plain text (Expected Failure). | Password **was** visible in plain text inside `cleancity_users`. | **Fail** | S. Chepkwony |
| **AUTH-TC-002** | 2025-11-05 | Session Management | (Security) Verify privilege escalation via localStorage tampering. | 1. Log in as normal user.<br>2. Edit `currentUser` in Local Storage.<br>3. Change role to `"admin"`.<br>4. Refresh. | Login: user@cleancity.com<br>Value: role:"admin" | Admin link appears; admin page accessible (Expected Failure). | Admin link appeared; full admin access granted. | **Fail** | S. Chepkwony |
| **AUTH-TC-003** | 2025-11-05 | Password Validation | Weak 2-character password accepted. | 1. Go to Register page.<br>2. Fill in all fields.<br>3. Use password `"a1"`. | Name:"Test"<br>Email:test@test.com<br>Password:"a1" | System accepts weak password (Expected Failure). | Account registered successfully with weak password `"a1"`. | **Fail** | I. Macharia |
| **AUTH-TC-004** | 2025-11-06 | User Management | Normal user deletes admin user (IDOR). | 1. Log in as normal user.<br>2. Run `dataService.deleteUser('2')` in console. | Login: user@cleancity.com<br>Command: deleteUser('2') | Admin user ID 2 should be deleted (Expected Failure). | Admin user **was** deleted successfully. | **Fail** | S. Chepkwony |
| **AUTH-TC-005** | 2025-11-06 | User Registration | User enumeration via error messages. | 1. Register with known email.<br>2. Note error.<br>3. Register with non-existent email.<br>4. Compare errors. | Known: admin@cleancity.com<br>Unknown: random@never.com | Known email returns different error (Expected Failure). | Error shown for admin email; none shown for random email. | **Fail** | I. Macharia |
| **AUTH-TC-006** | 2025-11-06 | User Login | Login success message appears before redirect. | 1. Go to Login page.<br>2. Enter valid credentials.<br>3. Observe UI. | Login: user@cleancity.com<br>Pass: password123 | Message "Login successful! Redirecting..." appears briefly. | Message displayed for ~1 second before redirect. | **Pass** | I. Macharia |
| **WASTE-TC-001** | 2025-11-07 | Pickup Scheduling | Verify pickup form does not save data. | 1. Fill form.<br>2. Submit.<br>3. Check `localStorage.pickupRequests`. | Name:"Test User"<br>Location:"Nairobi"<br>Waste:"General" | Request does *not* appear in storage (Expected Failure). | Success message shown, but request not saved. | **Fail** | I. Macharia |
| **WASTE-TC-002** | 2025-11-07 | Request Management | Non-admin can access and use Admin page. | 1. Log in as normal user.<br>2. Navigate to admin via console.<br>3. Update status. | Login:user@cleancity.com<br>Target:REQ001<br>Status:"Completed" | Normal user can update admin data (Expected Failure). | Admin page loaded; REQ001 updated successfully. | **Fail** | S. Chepkwony |
| **WASTE-TC-003** | 2025-11-08 | Status Tracking | No audit trail saved on status change. | 1. Log in as admin.<br>2. Update request status.<br>3. Inspect object. | Login:admin@cleancity.com<br>Request: REQ001 | No audit fields added. | Status changed with *no* audit fields. | **Pass** | I. Macharia |
| **WASTE-TC-004** | 2025-11-08 | Pickup Scheduling | Form accepts date in the past. | 1. Fill form.<br>2. Choose past date.<br>3. Submit. | Name:"Past User"<br>Date:2025-11-01 | Form accepts past date (Expected Failure). | Form accepted past date and showed success message. | **Fail** | I. Macharia |
| **DASH-TC-001** | 2025-11-09 | Admin/Dashboard Data Flow | Non-admin sees global stats. | 1. Set `pickupRequests`.<br>2. Log in as normal user.<br>3. View dashboard. | `[{"id":1,"status":"Missed"}]`<br>Login:user@cleancity.com | Shows global stats (Expected Failure). | Dashboard displayed global stats (1 request, 1 missed). | **Fail** | S. Chepkwony |
| **DASH-TC-002** | 2025-11-09 | Bar Chart Visualization | Handles malformed date fields. | 1. Set test data.<br>2. Log in as Admin.<br>3. View chart. | `{"date":"2025-11-01"}`, `{"date":null}` | Renders bars: "11/25" and empty label. | Chart rendered 2 bars correctly. | **Pass** | I. Macharia |
| **DASH-TC-003** | 2025-11-10 | Missed Pickups Metric | Ignores Pending requests. | 1. Set data.<br>2. Log in as Admin.<br>3. Check metric. | `["Missed","missed","Pending"]` | Missed Pickups = 2. | Displayed 2; Pending ignored. | **Pass** | I. Macharia |
| **DASH-TC-004** | 2025-11-10 | Bar Chart Visualization | (Deferred) Scaling with high data volume. | 1. (Deferred) Generate 15 months of data.<br>2. Log in.<br>3. Check chart. | (Deferred) 15 request entries | Chart should display 15 readable bars. | Deferred | **Deferred** | — |




---

### Notes
- 

---
