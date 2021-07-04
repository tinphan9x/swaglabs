import sys
import os
import pytest
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Test_Login import Test_Login_Page

import testtools as testtools

if __name__ == "__main__":

    # test_loader = TestLoader()
    # # Test Suite is used since there are multiple test cases
    # test_suite = TestSuite((
    #     test_loader.loadTestsFromTestCase(Test_Login_Page),
    #     ))
    #
    # test_runner = TextTestRunner(verbosity=2)
    # test_runner.run(test_suite)
    #
    # # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    # parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    # parallel_suite.run(testtools.StreamResult())

    os.system("C:/Users/USER/scoop/apps/allure/2.14.0/bin/allure generate --clean --output " + './Reports')
    #Run allure report of this file, export report to PJ/Reports
    pytest.main(['-s', '-q','--alluredir','./Reports','./Tests/Test_Login.py'])
    #Open allue report via browser
    os.system("C:/Users/USER/scoop/apps/allure/2.14.0/bin/allure serve " + './Reports')
