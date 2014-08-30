Example code from a quick demonstration of how and why to use a functional programming style.

Only pass simple (immutable) data structures around.
The data flow describes the problem.
Each function has a single purpose, which /should/ be obvious even in the absence of comments.
I/O is pulled out into separate explicit functions, not buried in other logic.
Every (non I/O) function can be fully tested with ease.
Because I/O functions are simple, we do not need much testing for them, beyond an end-to-end integration test or two.
This eliminates mocking or dependency injection in testing, which are rarely suitable or adequate.

This code was used for stripping the date/timestamps from log files so logs from different days could be compared without false positives.