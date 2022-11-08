```# If not stated otherwise in this file or this component's license file the
# following copyright and licenses apply:
#
# Copyright 2021 RDK Management
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

# For L1_testing


Main objective for L1_testing was checking the api’s functionality in bundleprocessor.py script.

This file is to check api’s functionality in bundleprocessor.py script was named as test_bundleprocessor_ut which was a python script file.

Filename should be named as follow '''test_classname_ut.py''' 

\rdk_trail\BundleGen\unit_tests\L1_testing\ test_bundleprocessor_ut this is path for the test script. ( test_bundleprocessor_ut.py)

In this test we create an object for bundleprocessor class which was present in the bundleprocessor.py script.

Instead of passing parameters at the time of object creation, we are passing the required parameters manually.

And then we are comparing the oci_config and the original output from the particular api’s.

# Environment


Python version should be greater than or equal to 3.7 to run L1_testing.

# Adding additional testcases


In L1_testing folder, we can add another testing file(inside L1_testing folder), Changes we need to made inside run_L1_test.py file.

	elif filename:

    os.system(‘python test_'+classname+'_ut.py')

# Running L1 test


To run whole L1 test we use a command:

    python run_L1_test.py

For individual test we use a command

    python run_L1_test.py -s classname

    Ex: python run_L1_test.py -s Bundleprocessor