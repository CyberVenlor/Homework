# Classwork feedback 20260911

**Student:** Geralt
**Classwork:** Recursion and abstract data types (stack and queue)
**Date:** 2026-09-11

## Score

**96 / 100**

| Question | Score |
|---|---|
| Q1 Recursion (18) | 15 |
| Q2 Recursion in detail (20) | 20 |
| Q3 Stack (20) | 19 |
| Q4 Queue (26) | 26 |
| Q5 Applications (16) | 16 |

## Feedback on incorrect answers

**Q1 (c) why a stack suits recursion (-3 marks)**
- LIFO is correct and you link it to the order of calls and returns. For full marks, explain the mechanism: every call pushes an activation record (return address and local variables) onto the stack, and when the base case is reached the records are popped in reverse order, so the most recent call returns first.

**Q3 (a) LIFO / operations (-1 mark)**
- LIFO, push and pop are all correct. Add the operational meaning: the most recently added element is the first to be removed.

## Notes (no marks deducted)

**Q1 (b) base case**
- Full marks. Correctly stating that the base case stops the recursion answers the question. To strengthen future answers you could add that it is the simplest/smallest instance, solved directly without a further recursive call.

**Q3 (c) another use of a stack**
- Full marks - the question asked only for a situation, and the browser back button is a valid one. Adding the reason (the most recently visited page is returned to first, LIFO) would complete the answer.

---
_Detailed notes are also added as comments in your Word file._
