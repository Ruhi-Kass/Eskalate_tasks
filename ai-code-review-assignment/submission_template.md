# AI Code Review Assignment (Python)

## Candidate
- Name: Ruhama Kassahun Aklilu
- Approximate time spent: 75 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Divides by total number of orders (`len(orders)`) instead of number of non-cancelled orders → completely wrong average
- doesn't handle division by 0

### Edge cases & risks
- Empty list → ZeroDivisionError
- All orders cancelled → ZeroDivisionError
- Missing `"status"` or `"amount"` keys → KeyError
- Non-dict items in list → TypeError
- Non-numeric `"amount"` values → TypeError

### Code quality / design issues
- Uses integer `total = 0` → potential precision loss with fractional amounts
- No input validation whatsoever
- Assumes perfect input structure

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only non-cancelled orders with valid numeric amount
- Return 0.0 when no valid orders exist (common analytics convention)
- Add defensive checks + try/except for robustness
- Use float summation from the beginning

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

 - I would focus on it not accepting invalid input because it reduces the amount of time it takes to computes and prevents the code form crashing abruptly
 - I would make sure the cancelled orders are recorded so as to reduce the amount of time it takes to sift through unecssary data as well as to preserve time and space in both computer aspect and logistically in reality
- I would also focus on make sure large data is processed accuratley and flitered to fit the requirements of my program


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Claims correct exclusion of cancelled orders while still dividing by total count → misleading
- Doesn't mention division by zero danger
- Ignores all robustness and crash problems

### Rewritten explanation
- Calculates the average amount of non-cancelled orders. Only valid non-cancelled orders with numeric amounts are included in the calculation. Returns 0.0 when there are no valid orders to average (empty input, all cancelled, or all invalid). Vaild data is invalubale to assesement and evaluation of data in AI.

## 4) Final Judgment
- Decision:**Reject**
- Justification:Fundamental business logic error (wrong denominator) + multiple crash scenarios + zero robustness
- Confidence & unknowns:High confidence — the bug is obvious and severe

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- None (no crashes), but extremely incorrect behavior and execution of a program that can't be taken into consideration when implmenting it in real world scenario

### Edge cases & risks
- `"user@domain@evil.com"` → counted (invalid)
- `"a@"`, `"@domain.com"`, `"@"` → counted
- Non-string items (None, int, list) → TypeError on `in`
- Whitespace-only strings → counted if contains `@`

### Code quality / design issues
- `"@" in email` is dangerously weak validation — completely misleading for claimed purpose
- No type checking
- No trimming of whitespace

## 2) Proposed Fixes / Improvements
### Summary of changes
- Check input is string + strip whitespace
- Require non-empty local part and domain
- Require at least one dot in domain
- Very basic structural validation

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
 -I would reduce the acceptance rate of the input by making sure it discards emails that are invalid. This is especially good to avoid access of critical accounts so it is sensitive information.

 - I would make sure the program also matches and verifies with the password which is important for security.

 - I would test it with very long email addresses to check how much it can compute

 - I would make sure it handles non numerical inputs as well as whitespace
 - I would test it with real world addresses to verify it's functionality


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Grossly overstates validity — almost nothing is actually "invalid" according to this logic
- "Safely ignores invalid entries" is false — most invalid formats are accepted
- Empty input technically returns 0, but that's the only correct claim

### Rewritten explanation
- > Counts strings that contain at least a non-empty local part, `@`, and a domain with at least one dot. Very permissive basic structural check — not suitable for production email validation.

## 4) Final Judgment
- Decision:**Reject**
- Justification:Claimed purpose ("valid email addresses") is completely misleading given the extremely weak check
- Confidence & unknowns: High Confidence

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Divides by total length (`len(values)`) instead of number of valid (non-None) values → wrong average

### Edge cases & risks
- Empty list → ZeroDivisionError(tries to divide an empty value)
- All values `None` → ZeroDivisionError
- Non-numeric values → TypeError/ValueError on `float()`
- Mixed types that can't be converted → crashes(tries to evaluate none number values like strings)

### Code quality / design issues
- Integer `total = 0` → potential precision loss(makes you lose accuracy while using very small numbers)
- No error handling at all(if anything goes wrong, the entire program crashes)
- Assumes all non-None values are convertible to float

## 2) Proposed Fixes / Improvements
### Summary of changes
- Integer `total = 0` → potential precision loss(make it hard to work with numbers close to 0 like 0.000001)
- No error handling at all
 Example 

The list contains text like "hello" → float("hello") → crash
The list contains True, False, lists, dictionaries → crash
The list is empty → divide by zero → crash
All values are None → divide by zero → crash

- Assumes all non-None values are convertible to float(it assumes every none value is number so it will try to convert it to 0 which causes it to crash)

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
 
 - Make sure if the list has only None values, it doesn't crash but returns 0.0
 - Make sure if the list has empty values it doesn't crash but return 0.0
 - When there are mixed values that it makes sure it ignores the None and non numerical values
 - If there are strings that look like numbers, to make sure it is included in the average and make sure it doesn't crash over strings that don't look like numbers and ignore them while calcuating


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Wrong denominator claim → average is not accurate
- "Safely handles mixed input types" → completely false, crashes on most non-numeric
- No mention of division by zero risk

### Rewritten explanation
- Calculates average of successfully converted numeric values, ignoring None and any values that cannot be converted to float. Returns 0.0 when there are no valid numeric values.

## 4) Final Judgment
- Decision:**Reject**
- Justification:Serious correctness error (wrong denominator) + crashes on almost any real-world messy data
- Confidence & unknowns:Very high confidence
