# Evaluation Guide

## Evaluation Process

For general evaluation, there are three stages: **Compilation**, **Execution**, and **Checking**. (Some stages may be omitted)

### Compilation Stage

In the compilation stage, errors during this stage will be displayed as **Compile Error**.

### Execution Stage

The previously compiled code will be executed according to the method specified by the problem. The runtime, memory usage, and file usage information displayed in the evaluation details are the results of running at this stage.

- If the program exits unexpectedly during this stage, it will display **Runtime Error**
- If the program execution times out during this stage, it will display **Time Limit Exceeded**

### Checking Stage

The results of the execution will be checked according to the method specified by the problem.

**Please Note:** In each stage, to ensure that the evaluation does not affect the normal operation of the server, the evaluation will be completed in a sandbox (the sandbox limits parameters such as file system, number of running CPUs, running time, etc.), so the environment may be different from your local environment.

---

## How to Submit

Use the `submit_acmoj/acmoj_client.py` script to submit code to ACMOJ, query submission status, or abort pending submissions.

**Please check the `acmoj_client.py` script file directly for detailed usage instructions and available commands.**

### Query Submission Status

When you query a submission status, the system will return comprehensive information including:

- **Evaluation details for each test point**:
  - Evaluation result (status)
  - Runtime duration
  - Memory usage
  - File/disk usage
  - Evaluation hints and messages
- **Compilation information**: If there were any compilation messages or errors, they will be displayed in the returned information

### Important Notes

- Remember the `submission_id` returned after each submission (needed for querying status)
- Aborted submissions do not count toward your submission limit
- Check the script file for all available commands and options
- **Note that a test point may still receive partial credit even if its result is not "Accepted"**, depending on the specific problem's scoring rules

---

## Evaluation Status

### Pending
**Waiting for testing.** This may be because the evaluation machine is busy, or all evaluation machines are offline.

### Compiling
**Compiling.** Your program is being compiled into an executable file by the evaluation machine.

### Judging
**Testing.** Your program is being run by the evaluation machine to check correctness.

### Accepted
**Passed.** Your program correctly passed all test points.

### Aborted
**Evaluation interrupted.** This may be because you or an administrator manually interrupted the evaluation, or the evaluation machine went offline during evaluation.

### Voided
**Score invalid.** Your program was marked as invalid by an administrator.

### Wrong Answer
**Wrong answer.** Your program output an incorrect answer at a certain test point.

### Compile Error
**Compilation error.** Your program failed to compile.

### Runtime Error
**Runtime error.** Your program crashed during execution, which may be due to array out of bounds, program return value not being 0, division by 0, etc.

### Time Limit Exceeded
**Time limit exceeded.** Your program did not produce an answer within the specified time, which may be due to an infinite loop or algorithm complexity being too high.

### Memory Limit Exceeded
**Memory limit exceeded.** Your program requested too much memory.

### Memory Leak
**Memory leak.** Your program output the correct answer, but a memory leak occurred. Please check dynamic memory management. (Some problems will detect this)

### Disk Limit Exceeded
**Disk limit exceeded.** Your program used too much disk space. Please check disk space management.

### Bad Problem
**Problem data error.** The problem configuration is incorrect and evaluation cannot be completed. If you encounter this error, please stop submitting.

### System Error
**System error.** The evaluation system encountered an error while testing your program. Please stop submitting.
