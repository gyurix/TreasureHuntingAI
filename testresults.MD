# Test results table

test_crossover_all 31
test_crossover_and_8_random_bytes 31
test_crossover_copy_13_random_bytes 31
test_crossover_xor_10_random_bytes 31
test_mutation_all 31
test_mutation_change_5_random_bytes 31
test_mutation_crossover_all 31
test_mutation_invert_20_random_bits 31
test_mutation_invert_6_random_bytes 30
test_mutation_swap_4_random_bytes 22

## 2nd run
test_crossover_all 39
test_crossover_and_8_random_bytes 40
test_crossover_copy_13_random_bytes 40
test_crossover_xor_10_random_bytes 39
test_mutation_all 40
test_mutation_change_5_random_bytes 40
test_mutation_crossover_all 40
test_mutation_invert_20_random_bits 40
test_mutation_invert_6_random_bytes 40
test_mutation_swap_4_random_bytes 31

## 3rd run
test_crossover_all 40
test_crossover_and_8_random_bytes 39
test_crossover_copy_13_random_bytes 40
test_crossover_xor_10_random_bytes 40
test_mutation_all 39
test_mutation_change_5_random_bytes 40
test_mutation_crossover_all 40
test_mutation_invert_20_random_bits 40
test_mutation_invert_6_random_bytes 40
test_mutation_swap_4_random_bytes 32

## 4th run
test_crossover_all 39
test_crossover_and_8_random_bytes 39
test_crossover_copy_13_random_bytes 38
test_crossover_xor_10_random_bytes 39
test_mutation_all 39
test_mutation_change_5_random_bytes 39
test_mutation_crossover_all 39
test_mutation_invert_20_random_bits 39
test_mutation_invert_6_random_bytes 39
test_mutation_swap_4_random_bytes 37


## 5th run
test_crossover_all 33
test_crossover_and_8_random_bytes 33
test_crossover_copy_13_random_bytes 33
test_crossover_xor_10_random_bytes 33
test_mutation_all 33
test_mutation_change_5_random_bytes 33
test_mutation_crossover_all 33
test_mutation_invert_20_random_bits 33
test_mutation_invert_6_random_bytes 33
test_mutation_swap_4_random_bytes 28


## Runtime in seconds

|           Test Name               |    #1    |    #2    |    #3    |    #4    |    #5    |  Total  | Average |
|-----------------------------------|----------|----------|----------|----------|----------|---------|---------|
|**crossover_all**                  |   3.76   |   3.99   | **2.18** |   6.77   |   2.02   |  18.72  |  3.744  |
|**crossover_and_8_random_bytes**   |   2.58   |   3.53   |   6.32   | **2.37** |   2.43   |  17.23  |  3.446  |
|**crossover_copy_13_random_bytes** |   2.84   |   2.97   |   2.93   |   4.80   |   2.14   |  15.68  |  3.136  |
|**crossover_xor_10_random_bytes**  |   2.33   |   2.80   |   3.00   |   6.63   |   2.01   |  16.77  |  3.354  |
|**mutation_all**                   |   2.24   |   2.92   |   3.06   |   3.09   |   2.14   |  13.45  |  2.69   |
|**mutation_crossover_all**         |   2.42   |   2.88   |   3.76   |   3.25   |   2.03   |  14.34  |  2.868  |
|**mutation_change_5_random_bytes** |   2.61   |   2.65   |   2.51   |   2.34   |   2.18   |  12.29  |  2.458  |
|**mutation_invert_20_random_bits** |   3.00   |   3.93   |   4.24   |   3.06   |   2.17   |  16.4   |  3.28   |
|**mutation_invert_6_random_bytes** | **2.16** | **1.95** |   3.25   |   2.64   |   2.01   |**12.01**|**2.402**|
|**mutation_swap_4_random_bytes**   |   2.73   |   3.22   |   4.74   |   2.71   | **1.96** | 15.36   | 3.072   |

## Found points with max 15 iterations (of 60)

|           Test Name               | #1 | #2 | #3 | #4 | #5 | Total | Average |
|-----------------------------------|----|----|----|----|----|-------|---------|
|**crossover_all**                  | 31 | 39 | 40 | 39 | 33 |  182  |  36.4   |
|**crossover_and_8_random_bytes**   | 31 | 40 | 39 | 39 | 33 |  182  |  36.4   |
|**crossover_copy_13_random_bytes** | 31 | 40 | 40 | 38 | 33 |  182  |  36.4   |
|**crossover_xor_10_random_bytes**  | 31 | 39 | 40 | 39 | 33 |  182  |  36.4   |
|**mutation_all**                   | 31 | 40 | 39 | 39 | 33 |  182  |  36.4   |
|**mutation_crossover_all**         | 31 | 40 | 40 | 39 | 33 |  **183**  |  **36.6**   |
|**mutation_change_5_random_bytes** | 31 | 40 | 40 | 39 | 33 |  **183**  |  **36.6**   |
|**mutation_invert_20_random_bits** | 31 | 40 | 40 | 39 | 33 |  **183**  |  **36.6**   |
|**mutation_invert_6_random_bytes** | 30 | 40 | 40 | 39 | 33 |  182  |  36.4   |
|**mutation_swap_4_random_bytes**   | 22 | 31 | 32 | 37 | 28 |  150  |  30.0   |


# Raw test output

## 1st run
    tests.py::test_program_execution PASSED                                  [  9%]
    tests.py::test_mutation_crossover_all PASSED                             [ 18%]
    test_mutation_crossover_all 31
    
    tests.py::test_mutation_all PASSED                                       [ 27%]
    test_mutation_all 31
    
    tests.py::test_crossover_all PASSED                                      [ 36%]
    test_crossover_all 31
    
    tests.py::test_crossover_xor_10_random_bytes PASSED                      [ 45%]
    test_crossover_xor_10_random_bytes 31
    
    tests.py::test_crossover_copy_13_random_bytes PASSED                     [ 54%]
    test_crossover_copy_13_random_bytes 31
    
    tests.py::test_crossover_and_8_random_bytes PASSED                       [ 63%]
    test_crossover_and_8_random_bytes 31
    
    tests.py::test_mutation_invert_20_random_bits PASSED                     [ 72%]
    test_mutation_invert_20_random_bits 31
    
    tests.py::test_mutation_change_5_random_bytes PASSED                     [ 81%]
    test_mutation_change_5_random_bytes 31
    
    tests.py::test_mutation_swap_4_random_bytes PASSED                       [ 90%]
    test_mutation_swap_4_random_bytes 22
    
    tests.py::test_mutation_invert_6_random_bytes PASSED                     [100%]
    test_mutation_invert_6_random_bytes 30
    
    
    =========================== slowest test durations ============================
    3.76s call     tests.py::test_crossover_all
    3.00s call     tests.py::test_mutation_invert_20_random_bits
    2.84s call     tests.py::test_crossover_copy_13_random_bytes
    2.73s call     tests.py::test_mutation_swap_4_random_bytes
    2.61s call     tests.py::test_mutation_change_5_random_bytes
    2.58s call     tests.py::test_crossover_and_8_random_bytes
    2.42s call     tests.py::test_mutation_crossover_all
    2.33s call     tests.py::test_crossover_xor_10_random_bytes
    2.24s call     tests.py::test_mutation_all
    2.16s call     tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_crossover_xor_10_random_bytes
    0.00s setup    tests.py::test_mutation_crossover_all
    0.00s teardown tests.py::test_mutation_invert_20_random_bits
    0.00s setup    tests.py::test_crossover_and_8_random_bytes
    0.00s teardown tests.py::test_crossover_and_8_random_bytes
    0.00s setup    tests.py::test_mutation_swap_4_random_bytes
    0.00s setup    tests.py::test_mutation_invert_20_random_bits
    0.00s teardown tests.py::test_crossover_copy_13_random_bytes
    0.00s call     tests.py::test_program_execution
    0.00s teardown tests.py::test_mutation_invert_6_random_bytes
    0.00s setup    tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_mutation_swap_4_random_bytes
    0.00s teardown tests.py::test_mutation_change_5_random_bytes
    0.00s setup    tests.py::test_mutation_change_5_random_bytes
    0.00s setup    tests.py::test_crossover_copy_13_random_bytes
    0.00s setup    tests.py::test_crossover_xor_10_random_bytes
    0.00s teardown tests.py::test_crossover_all
    0.00s setup    tests.py::test_crossover_all
    0.00s teardown tests.py::test_mutation_all
    0.00s setup    tests.py::test_mutation_all
    0.00s teardown tests.py::test_mutation_crossover_all
    0.00s teardown tests.py::test_program_execution
    0.00s setup    tests.py::test_program_execution
    ========================= 11 passed in 26.76 seconds ==========================


## 2nd run

    tests.py::test_program_execution PASSED                                  [  9%]
    tests.py::test_mutation_crossover_all PASSED                             [ 18%]
    test_mutation_crossover_all 40
    
    tests.py::test_mutation_all PASSED                                       [ 27%]
    test_mutation_all 40
    
    tests.py::test_crossover_all PASSED                                      [ 36%]
    test_crossover_all 39
    
    tests.py::test_crossover_xor_10_random_bytes PASSED                      [ 45%]
    test_crossover_xor_10_random_bytes 39
    
    tests.py::test_crossover_copy_13_random_bytes PASSED                     [ 54%]
    test_crossover_copy_13_random_bytes 40
    
    tests.py::test_crossover_and_8_random_bytes PASSED                       [ 63%]
    test_crossover_and_8_random_bytes 40
    
    tests.py::test_mutation_invert_20_random_bits PASSED                     [ 72%]
    test_mutation_invert_20_random_bits 40
    
    tests.py::test_mutation_change_5_random_bytes PASSED                     [ 81%]
    test_mutation_change_5_random_bytes 40
    
    tests.py::test_mutation_swap_4_random_bytes PASSED                       [ 90%]
    test_mutation_swap_4_random_bytes 31
    
    tests.py::test_mutation_invert_6_random_bytes PASSED                     [100%]
    test_mutation_invert_6_random_bytes 40
    
    
    =========================== slowest test durations ============================
    3.99s call     tests.py::test_crossover_all
    3.93s call     tests.py::test_mutation_invert_20_random_bits
    3.53s call     tests.py::test_crossover_and_8_random_bytes
    3.22s call     tests.py::test_mutation_swap_4_random_bytes
    2.97s call     tests.py::test_crossover_copy_13_random_bytes
    2.92s call     tests.py::test_mutation_all
    2.88s call     tests.py::test_mutation_change_5_random_bytes
    2.80s call     tests.py::test_crossover_xor_10_random_bytes
    2.65s call     tests.py::test_mutation_crossover_all
    1.95s call     tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_crossover_all
    0.00s setup    tests.py::test_crossover_xor_10_random_bytes
    0.00s teardown tests.py::test_mutation_swap_4_random_bytes
    0.00s setup    tests.py::test_crossover_and_8_random_bytes
    0.00s setup    tests.py::test_mutation_change_5_random_bytes
    0.00s setup    tests.py::test_crossover_all
    0.00s setup    tests.py::test_mutation_swap_4_random_bytes
    0.00s teardown tests.py::test_mutation_all
    0.00s teardown tests.py::test_mutation_change_5_random_bytes
    0.00s teardown tests.py::test_mutation_invert_20_random_bits
    0.00s setup    tests.py::test_program_execution
    0.00s setup    tests.py::test_mutation_all
    0.00s setup    tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_crossover_copy_13_random_bytes
    0.00s call     tests.py::test_program_execution
    0.00s teardown tests.py::test_mutation_invert_6_random_bytes
    0.00s setup    tests.py::test_mutation_invert_20_random_bits
    0.00s teardown tests.py::test_crossover_and_8_random_bytes
    0.00s setup    tests.py::test_crossover_copy_13_random_bytes
    0.00s teardown tests.py::test_crossover_xor_10_random_bytes
    0.00s teardown tests.py::test_mutation_crossover_all
    0.00s setup    tests.py::test_mutation_crossover_all
    0.00s teardown tests.py::test_program_execution
    ========================= 11 passed in 30.91 seconds ==========================
    Process finished with exit code 0


## 3rd run

    tests.py::test_program_execution PASSED                                  [  9%]
    tests.py::test_mutation_crossover_all PASSED                             [ 18%]
    test_mutation_crossover_all 40
    
    tests.py::test_mutation_all PASSED                                       [ 27%]
    test_mutation_all 39
    
    tests.py::test_crossover_all PASSED                                      [ 36%]
    test_crossover_all 40
    
    tests.py::test_crossover_xor_10_random_bytes PASSED                      [ 45%]
    test_crossover_xor_10_random_bytes 40
    
    tests.py::test_crossover_copy_13_random_bytes PASSED                     [ 54%]
    test_crossover_copy_13_random_bytes 40
    
    tests.py::test_crossover_and_8_random_bytes PASSED                       [ 63%]
    test_crossover_and_8_random_bytes 39
    
    tests.py::test_mutation_invert_20_random_bits PASSED                     [ 72%]
    test_mutation_invert_20_random_bits 40
    
    tests.py::test_mutation_change_5_random_bytes PASSED                     [ 81%]
    test_mutation_change_5_random_bytes 40
    
    tests.py::test_mutation_swap_4_random_bytes PASSED                       [ 90%]
    test_mutation_swap_4_random_bytes 32
    
    tests.py::test_mutation_invert_6_random_bytes PASSED                     [100%]
    test_mutation_invert_6_random_bytes 40
    
    
    =========================== slowest test durations ============================
    6.32s call     tests.py::test_crossover_and_8_random_bytes
    4.74s call     tests.py::test_mutation_swap_4_random_bytes
    4.24s call     tests.py::test_mutation_invert_20_random_bits
    3.76s call     tests.py::test_mutation_change_5_random_bytes
    3.25s call     tests.py::test_mutation_invert_6_random_bytes
    3.06s call     tests.py::test_mutation_all
    3.00s call     tests.py::test_crossover_xor_10_random_bytes
    2.93s call     tests.py::test_crossover_copy_13_random_bytes
    2.51s call     tests.py::test_mutation_crossover_all
    2.18s call     tests.py::test_crossover_all
    0.00s setup    tests.py::test_mutation_invert_20_random_bits
    0.00s call     tests.py::test_program_execution
    0.00s setup    tests.py::test_mutation_change_5_random_bytes
    0.00s teardown tests.py::test_crossover_all
    0.00s setup    tests.py::test_crossover_and_8_random_bytes
    0.00s setup    tests.py::test_mutation_crossover_all
    0.00s teardown tests.py::test_program_execution
    0.00s teardown tests.py::test_mutation_change_5_random_bytes
    0.00s teardown tests.py::test_crossover_and_8_random_bytes
    0.00s setup    tests.py::test_mutation_all
    0.00s teardown tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_mutation_crossover_all
    0.00s setup    tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_mutation_swap_4_random_bytes
    0.00s setup    tests.py::test_mutation_swap_4_random_bytes
    0.00s teardown tests.py::test_mutation_invert_20_random_bits
    0.00s teardown tests.py::test_crossover_copy_13_random_bytes
    0.00s setup    tests.py::test_crossover_copy_13_random_bytes
    0.00s teardown tests.py::test_crossover_xor_10_random_bytes
    0.00s setup    tests.py::test_crossover_xor_10_random_bytes
    0.00s setup    tests.py::test_crossover_all
    0.00s teardown tests.py::test_mutation_all
    0.00s setup    tests.py::test_program_execution
    ========================= 11 passed in 36.11 seconds ==========================


## 4th run

    tests.py::test_program_execution PASSED                                  [  9%]
    tests.py::test_mutation_crossover_all PASSED                             [ 18%]
    test_mutation_crossover_all 39
    
    tests.py::test_mutation_all PASSED                                       [ 27%]
    test_mutation_all 39
    
    tests.py::test_crossover_all PASSED                                      [ 36%]
    test_crossover_all 39
    
    tests.py::test_crossover_xor_10_random_bytes PASSED                      [ 45%]
    test_crossover_xor_10_random_bytes 39
    
    tests.py::test_crossover_copy_13_random_bytes PASSED                     [ 54%]
    test_crossover_copy_13_random_bytes 38
    
    tests.py::test_crossover_and_8_random_bytes PASSED                       [ 63%]
    test_crossover_and_8_random_bytes 39
    
    tests.py::test_mutation_invert_20_random_bits PASSED                     [ 72%]
    test_mutation_invert_20_random_bits 39
    
    tests.py::test_mutation_change_5_random_bytes PASSED                     [ 81%]
    test_mutation_change_5_random_bytes 39
    
    tests.py::test_mutation_swap_4_random_bytes PASSED                       [ 90%]
    test_mutation_swap_4_random_bytes 37
    
    tests.py::test_mutation_invert_6_random_bytes PASSED                     [100%]
    test_mutation_invert_6_random_bytes 39
    
    
    =========================== slowest test durations ============================
    6.77s call     tests.py::test_crossover_all
    6.63s call     tests.py::test_crossover_xor_10_random_bytes
    4.80s call     tests.py::test_crossover_copy_13_random_bytes
    3.25s call     tests.py::test_mutation_change_5_random_bytes
    3.09s call     tests.py::test_mutation_all
    3.06s call     tests.py::test_mutation_invert_20_random_bits
    2.71s call     tests.py::test_mutation_swap_4_random_bytes
    2.64s call     tests.py::test_mutation_invert_6_random_bytes
    2.37s call     tests.py::test_crossover_and_8_random_bytes
    2.34s call     tests.py::test_mutation_crossover_all
    0.00s setup    tests.py::test_crossover_xor_10_random_bytes
    0.00s teardown tests.py::test_mutation_all
    0.00s teardown tests.py::test_mutation_change_5_random_bytes
    0.00s teardown tests.py::test_program_execution
    0.00s setup    tests.py::test_crossover_and_8_random_bytes
    0.00s setup    tests.py::test_crossover_copy_13_random_bytes
    0.00s setup    tests.py::test_mutation_swap_4_random_bytes
    0.00s teardown tests.py::test_crossover_all
    0.00s setup    tests.py::test_program_execution
    0.00s setup    tests.py::test_crossover_all
    0.00s teardown tests.py::test_mutation_crossover_all
    0.00s call     tests.py::test_program_execution
    0.00s teardown tests.py::test_mutation_invert_6_random_bytes
    0.00s setup    tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_mutation_swap_4_random_bytes
    0.00s setup    tests.py::test_mutation_change_5_random_bytes
    0.00s teardown tests.py::test_mutation_invert_20_random_bits
    0.00s setup    tests.py::test_mutation_invert_20_random_bits
    0.00s teardown tests.py::test_crossover_and_8_random_bytes
    0.00s teardown tests.py::test_crossover_copy_13_random_bytes
    0.00s teardown tests.py::test_crossover_xor_10_random_bytes
    0.00s setup    tests.py::test_mutation_all
    0.00s setup    tests.py::test_mutation_crossover_all
    ========================= 11 passed in 37.73 seconds ==========================


## 5th run

    tests.py::test_program_execution PASSED                                  [  9%]
    tests.py::test_mutation_crossover_all PASSED                             [ 18%]
    test_mutation_crossover_all 33
    
    tests.py::test_mutation_all PASSED                                       [ 27%]
    test_mutation_all 33
    
    tests.py::test_crossover_all PASSED                                      [ 36%]
    test_crossover_all 33
    
    tests.py::test_crossover_xor_10_random_bytes PASSED                      [ 45%]
    test_crossover_xor_10_random_bytes 33
    
    tests.py::test_crossover_copy_13_random_bytes PASSED                     [ 54%]
    test_crossover_copy_13_random_bytes 33
    
    tests.py::test_crossover_and_8_random_bytes PASSED                       [ 63%]
    test_crossover_and_8_random_bytes 33
    
    tests.py::test_mutation_invert_20_random_bits PASSED                     [ 72%]
    test_mutation_invert_20_random_bits 33
    
    tests.py::test_mutation_change_5_random_bytes PASSED                     [ 81%]
    test_mutation_change_5_random_bytes 33
    
    tests.py::test_mutation_swap_4_random_bytes PASSED                       [ 90%]
    test_mutation_swap_4_random_bytes 28
    
    tests.py::test_mutation_invert_6_random_bytes PASSED                     [100%]
    test_mutation_invert_6_random_bytes 33
    
    
    =========================== slowest test durations ============================
    2.43s call     tests.py::test_crossover_and_8_random_bytes
    2.18s call     tests.py::test_mutation_crossover_all
    2.17s call     tests.py::test_mutation_invert_20_random_bits
    2.14s call     tests.py::test_crossover_copy_13_random_bytes
    2.14s call     tests.py::test_mutation_all
    2.03s call     tests.py::test_mutation_change_5_random_bytes
    2.02s call     tests.py::test_crossover_all
    2.01s call     tests.py::test_mutation_invert_6_random_bytes
    2.01s call     tests.py::test_crossover_xor_10_random_bytes
    1.96s call     tests.py::test_mutation_swap_4_random_bytes
    0.00s setup    tests.py::test_crossover_all
    0.00s teardown tests.py::test_mutation_invert_6_random_bytes
    0.00s call     tests.py::test_program_execution
    0.00s setup    tests.py::test_mutation_crossover_all
    0.00s teardown tests.py::test_crossover_all
    0.00s setup    tests.py::test_mutation_invert_6_random_bytes
    0.00s teardown tests.py::test_mutation_swap_4_random_bytes
    0.00s setup    tests.py::test_mutation_swap_4_random_bytes
    0.00s teardown tests.py::test_mutation_change_5_random_bytes
    0.00s setup    tests.py::test_mutation_change_5_random_bytes
    0.00s teardown tests.py::test_mutation_invert_20_random_bits
    0.00s setup    tests.py::test_mutation_invert_20_random_bits
    0.00s teardown tests.py::test_crossover_and_8_random_bytes
    0.00s setup    tests.py::test_crossover_and_8_random_bytes
    0.00s teardown tests.py::test_crossover_copy_13_random_bytes
    0.00s setup    tests.py::test_crossover_copy_13_random_bytes
    0.00s teardown tests.py::test_crossover_xor_10_random_bytes
    0.00s setup    tests.py::test_crossover_xor_10_random_bytes
    0.00s teardown tests.py::test_mutation_all
    0.00s setup    tests.py::test_mutation_all
    0.00s teardown tests.py::test_mutation_crossover_all
    0.00s teardown tests.py::test_program_execution
    0.00s setup    tests.py::test_program_execution
    ========================= 11 passed in 21.15 seconds ==========================
