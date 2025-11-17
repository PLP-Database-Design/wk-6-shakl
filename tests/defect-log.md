CleanCity - Defects Log

This document tracks defects identified during the testing phase of the CleanCity - Waste Pickup Scheduler project.  
Each entry includes details about the defect and its status.

---

## Summary
| Metric | Count |
|---------|-------|
| Total Defects |  |
|  |  |


---


## Defects Table

| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
|------------|----------------|------------------|--------------|--------------------|-----------------|----------------|-----------|----------|
| D-001 | 12-11-2025 | AUTH-TC-001: User Login/Registration - Password Storage | (Security) Verify passwords are stored in plain text. | 1. Log in with user@cleancity.com. <br> 2. Open DevTools → Application → Local Storage. <br> 3. Inspect cleancity_users.	Login: user@cleancity.com |password123	Password should not appear in plain text.  | ![Defect 001: AUTH-TC-001: User Login/Registration - Password Storage](/tests/screenshots/D-001.png) | High | Fail |
| D-002 | 12-11-2025 | AUTH-TC-003	2025-11-05	Password Validation	 | Weak 2-character password accepted. | 1. Go to Register page. <br> 2. Fill in all fields. <br> 3. Use password "a1". | Password:"a1"	System should not accept weak password  | System accepts weak password  | High | Fail | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
| Defect ID | Date Reported | Module / Feature | Description | Steps to Reproduce | Expected Result | Actual Result | Severity | Status | 
|


---

## Notes
- 

---

### Next Steps
- Re-test open defects in the next test cycle.  
- Update this log after each regression test.  
- Link any related GitHub Issues below:

**GitHub Issues:**  
-
-
-

