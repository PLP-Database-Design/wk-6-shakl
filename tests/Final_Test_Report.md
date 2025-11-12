
## CleanCity – Waste Pickup Scheduler
**Final Test Report**

**Version: 1.0**
**Date: November 5, 2025**
**Prepared by:** Software Testing Team
**Team Members:**

**Test Manager:** Shanice Chepkwony

**Risk Analyst:** Ian Macharia

**Test Executor:** Mark Mwangi

---

## 1. Objective

The objective of this testing cycle was to validate the functionality, usability, accessibility, and responsiveness of the CleanCity Waste Pickup Scheduler web application. The goal was to identify defects, verify intentional flaws, and ensure that the system aligns with defined requirements and user expectations.

---

## 2. Scope

**Testing covered both functional and non-functional aspects of the following modules:**

| Module        | Key Features Tested                                           |
|---------------|---------------------------------------------------------------|
| Home Page     | Form submission, validation, and success messages            |
| Dashboard     | Filtering, sorting, and data display                          |
| Feedback Page | Feedback form and request ID validation                       |
| Awareness Page| Accessibility and responsive design                           |
| Admin Panel   | Request management, status updates, and data persistence     |






---

## 3. Tools Used
- GitHub: Repository management and version control
- Jira: Issue tracking and defect management
- Chrome DevTools: Manual testing and debugging
-

---


## 4. Testing Techniques Used

## 1. Equivalence Partitioning (EP)

**Objective:** Identify valid and invalid input classes for key forms and verify representative values.

| Input       | Partitions (Valid / Invalid) | Representative Value | Expected Behavior                   | Actual Behavior                       | Tester           | Pass/Fail | 
|------------|-------------------------------|--------------------|-----------------------------------|-------------------------------------|-----------------|-----------|------------------------------|
| User Email | Valid: proper email format<br>Invalid: missing @, special chars | user@cleancity.com | Should accept valid email          | Accepted correctly                     |    |     |
| Password   | Valid: >=3 characters<br>Invalid: 1-2 characters | password123 | Should accept valid password      | Accepted correctly                     |     | Pass      |                              
| Pickup Date| Valid: today or future date<br>Invalid: past dates | 2025-11-01 | Form should allow valid date only | Accepted past date                     |     | Fail      | 
**Observations / Notes:**  
- EP testing revealed the pickup date allowed past dates — a functional flaw.  

---

## 2. Boundary Value Analysis (BVA)

**Objective:** Test values around the edges of valid ranges.  

| Parameter      | Boundaries Identified | Test Values (-1 / = / +1) | Expected Behavior                | Actual Behavior                 | Tester       | Pass/Fail |
|----------------|---------------------|---------------------------|---------------------------------|--------------------------------|--------------|-----------|-----------------------------|

**Observations / Notes:**  

---

## 3. Decision Table Testing (DTT)

**Objective:** Combine multiple input parameters and verify expected outcomes.  

| User Type | Pickup Date | Waste Type | Expected Outcome                   | Actual Outcome                   | Tester       | Pass/Fail |
|-----------|------------|------------|-----------------------------------|---------------------------------|--------------|-----------|
| Normal    | Valid      | General    | Request saved                      | Request saved                     |  | Pass      |
| Normal    | Past       | General    | Request rejected                   | Request accepted                  |  | Fail      |
| Admin     | Valid      | Hazardous  | Request saved & visible in admin   | Request saved & visible           |    | Pass      |

**Observations / Notes:**  
- Invalid combinations such as past dates were incorrectly accepted.  

---

## 4.



---

## Defect Summary

| **Severity** | **Defects Count** | **Examples** |
|---------------|------------------|---------------|
|  |  | Plain-text passwords, admin access bypass |
| High |  | Weak password rule, missing validation |
| Medium | | Past date acceptance, dashboard stats exposure |
| Low |  | UX message timing issue |

**Total Defects:** 10  
**Resolved by Development Team:** Pending in next sprint.

---

## Coverage Metrics

| **Metric** | **Value** |
|-------------|-------------|-----------|
| Risk Coverage |   |
| Pass Rate | 
|  |  |

---

## Key Findings & Observations
- All major **security vulnerabilities** were confirmed and documented.  
- Functional areas like **pickup scheduling** and **role-based access** require immediate remediation.  
- Dashboard and visualization modules are **functionally stable** with good data integrity.  

---

##  Attachments


---

##  Conclusion


---





