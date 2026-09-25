# Classwork feedback 20260918

**Student:** Geralt
**Classwork:** Abstract data types - binary tree, linked list, circular queue
**Date:** 2026-09-18

## Score

**95 / 100**

| Question | Score |
|---|---|
| Q1 Binary tree concepts (25) | 23 |
| Q2 Linked list (35) | 32 |
| Q3 Circular queue programming (40) | 40 |

## Feedback on incorrect answers

**Q1 (f) choice of key (-2 marks)**
- You have the two key points - keys should be unique, and surnames are not - plus a closing judgement. Missing: the consequence of duplicated keys, that two records could not be told apart so a search would be ambiguous; and that a key must also be comparable, which is what allows the tree to order the records and search by them.

**Q2 (b) null pointer (-1 mark)**
- "The end of the linked list" earns one mark and the value -1 earns another. The middle point is missing: a null pointer specifically marks a node that has no successor - the last node of the list - and the same value terminates the free list.

**Q2 (e) returning a node to the heap (-2 marks)**
- "Added to the heap" and "will be reused again" earn two marks. Two are missing, and they are the mechanics the question is asking for: the removed node's pointer is set to the current `heapStartPointer` so that it links on to the rest of the free list, and `heapStartPointer` is then updated to point at the removed node, making it the new first free node.

## Notes (no marks deducted)

**Q1 (b) level and height**
- Full marks. Level 3 and height 2 are both correct. To make the answer complete in the exam it also helps to state that the root is counted as level 1, which is what makes 45 level 3, and to define height as the number of edges on the longest path from the root to the deepest leaf.

**Q1 (e) inserting 40**
- Full marks. Your answer - 40 becomes the **left child of 45** - is correct, and the three comparisons you give (40 > 38 right, 40 < 57 left, 40 < 45 left) are exactly right.

**Q2 (a) trace table**
- Full marks. Every itemPointer is correct, and `-1` in the last row is the right value: the node holding 61 is the last node in the list, so its next pointer is the null pointer. It is worth adding in words that the search stops and returns the index once the item is found.

**Q3 (a)-(f) circular queue**
- Full marks across the whole question. The declaration, enqueue, dequeue, main program, screenshot and the final explanation are all correct. The screenshot clearly shows the output in the right order.

---
_Detailed notes are also added as comments in your Word file._
