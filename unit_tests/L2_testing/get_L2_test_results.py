import os
import sys
import unittest

from loguru import logger

#os.chdir("..")
f = open("L2_test_results.txt", "w+")
f.write("SNo\tTest Name (Results)\t\tReason\n")
f.write("---\t-------------------\t\t------")
f.close()

passed=0
total=0

class add_test_results:
    def add_tests(self):
        logger.debug("Adding new Test to the list...")
        logger.debug("Test Name: %s" %(self._testMethodName))
        f = open("L2_test_results.txt", "a")
        global total
        f.write("\n\n%d\t" % (total+1))
        f.write("%s" %(self._testMethodName))
        total = total+1
        f.close()

    def test_passed(self):
        logger.debug("Test is Passed...")
        f = open("L2_test_results.txt", "a")
        f.write("(PASSED)\t")
        global passed
        passed=passed+1
        f.close()

    def test_failed(self):
        logger.debug("Test is Failed...")
        f = open("L2_test_results.txt", "a")
        f.write("(FAILED) %s" %(self.failure))
        f.close()

    def end_results(self):
       global passed
       global total
       logger.debug("total = %s" %total)
       logger.debug("passed = %s" %passed)
       f = open("L2_test_results.txt", 'r+')
       content = f.read()
       f.close()
       f = open("L2_test_results.txt", "w")
       f.write("TEST RESULTS\n")
       f.write("============")
       f.write("\nTOTAL TESTS: %d\n" %(total))
       f.write("PASSED: %d\n" %(passed))
       f.write("FAILED: %d\n" %(total-passed))
       f.write("\nTEST DETAILS")
       f.write("\n============\n")
       f.write(content)
       f.close()
