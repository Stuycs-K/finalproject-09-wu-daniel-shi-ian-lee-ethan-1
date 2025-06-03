# Dev Log:

This document must be updated daily every time you finish a work session.

## Ethan Lee
### 2025-05-20 - Brief description
Researched sha256 and preprocessing; 
### 2025-05-22 - Brief description
Researched sha256 and preprocessing again, wrote psuedocode for padding and chunking
### 2025-05-27 - Brief description
Recloned repo; worked on rightrotate and rightshift functions for sha256 step 6 compression
Delegated tasks for groupwork so we can collaborate outside of school
Discussed presentations with other sha groups.

### 2025-05-28 - Brief description
finished right rotate right shift and started testing; initialized variables a-h
started compression methods and working on implentation within the chunking loop
### 2025-05-29 
Wrote the compression loop and created bitwise add function
### 2025-05-31
HUGE WIN! Went through each new variable in the first iteration of the compression loop, modified the helper functions, and readjusted the loop to run for 64 iterations. Tested and confirmed success with the final a-h values from research.
### 2025-01-31
Testing and starting combining the code. Getting several errors but each part should work individually. 
### 2025-02-31
Wrote several new test cases and spent most of class debugging with Ian. Spent most of my time at home trying to ssh and push classwork. 
### 2025-03-31
Fixed most of the issues found yesterday and made new tests, got sha256 to finally work for an input length of at least 52. Reworked several functions and variables so that they exist in the same file; modified the sha256(input) function to include several missing steps in chunking and compression loops.