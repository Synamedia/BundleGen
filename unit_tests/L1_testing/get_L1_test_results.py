import os
import sys
import unittest

from loguru import logger
os.chdir("..")
result = open("L1_test_results.txt", "w")
result.write("SNo\tTest Name (Results)\t\tReason\n")
result.write("---\t-------------------\t\t------")
result.close()

passed=0
total=0

class add_test_results:
    def add_tests(self):
        logger.debug("Adding new Test to the list...")
        logger.debug("Test Name: %s" %(self._testMethodName))
        global total
        total = total+1
        global result
        result = open("L1_test_results.txt", "a")
        result.write("\n\n%d\t" %total)
        result.write("%s" %(self._testMethodName))
        result.close()

    def test_passed(self):
        logger.debug("Test is Passed...")
        global result
        result = open("L1_test_results.txt", "a")
        result.write("(PASSED)\t")
        result.close()
        global passed
        passed=passed+1

    def test_failed(self, msg):
        logger.debug("Test is Failed...")
        global result
        result = open("L1_test_results.txt", "a")
        if msg:
            result.write("(FAILED) %s" %(msg.split(":")[0]))
        result.close()

    def end_results(self):
       global passed
       global total
       logger.debug("Total Tests Ran= %s" %total)
       logger.debug("Passed = %s" %passed)
       logger.debug("Failed = %s" %(total-passed))
       global result
       result = open("L1_test_results.txt", "r")
       content = result.read()
       result.close()
       result = open("L1_test_results.txt", "w")
       result.write("TEST RESULTS\n")
       result.write("============")
       result.write("\nTOTAL TESTS: %d\n" %(total))
       result.write("PASSED: %d\n" %(passed))
       result.write("FAILED: %d\n" %(total-passed))
       result.write("\nTEST DETAILS")
       result.write("\n============\n")
       result.write(content)
       result.close()
    if (total-passed)>0:
        sys.exit(1)
