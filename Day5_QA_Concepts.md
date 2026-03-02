# QA Fundamentals

## 1. What is Quality Assurance (QA)?

Quality Assurance (QA) ensures that software works as expected and meets requirements before release.  
It focuses on preventing defects rather than just detecting them.

QA Goals:
- Improve product quality
- Reduce bugs before production
- Ensure reliability and performance
- Validate user requirements

---

## 2. Manual Testing Basics

Manual testing is the process of testing software manually without automation tools.

The tester:
- Executes test cases step by step
- Compares expected vs actual results
- Reports defects if found

Types of Manual Testing:
- Functional Testing
- Regression Testing
- Smoke Testing
- Exploratory Testing

---

## 3. Bug Life Cycle

The Bug Life Cycle defines the stages a defect goes through.

1. New – Tester reports the bug
2. Assigned – Bug assigned to developer
3. Open – Developer starts fixing
4. Fixed – Bug is resolved
5. Retest – Tester verifies fix
6. Closed – Bug successfully resolved
7. Reopened – If issue still exists

---

## 4. Test Cases

A Test Case is a document that defines:
- Test Case ID
- Description
- Preconditions
- Test Steps
- Expected Result
- Actual Result
- Status (Pass/Fail)

Example:

Test Case ID: TC_01  
Description: Verify login with valid credentials  
Steps:
1. Enter valid email  
2. Enter valid password  
3. Click Login  

Expected Result:
User should be redirected to dashboard.

---

## 5. Regression Testing

Regression Testing ensures that new code changes do not break existing functionality.

Why it is important:
- Prevents side effects of new updates
- Ensures stability after bug fixes
- Maintains product reliability

Example:
If a login bug was fixed, regression testing ensures:
- Signup still works
- Password reset still works
- Dashboard loads correctly

---

## 6. QA in AI/ML Context

In AI/ML systems, QA also focuses on:
- Data quality validation
- Model accuracy verification
- Bias detection
- Output consistency
- Performance monitoring

Unlike traditional software, AI systems must be tested continuously because models learn and evolve over time.

---

# Summary

QA ensures software quality through structured testing processes.  
Understanding bug lifecycle, test cases, and regression testing builds the foundation for advanced AI/ML QA practices.
