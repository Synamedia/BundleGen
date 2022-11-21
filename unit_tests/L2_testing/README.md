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
#For L2 Testing
Main objective of L2_testing is verifying the bundle image for an individual app which was taken from oci image.

## Environment Setup
Python version should be greater than or equal to 3.7 to run L2_testing.
Once installed the python version, setup the pip install
```console
    $ cd BundleGen
    $ pip install -r requirements.txt
    $ pip install --editable .
```
##  Required Parameters to run L2 test
Appname and Platformname

## How to run L2 test
Run the L2 test using the run_L2_test.py file.
$cd unit_tests/L2_testing
$python run_L2_test.py -a appname -p platformname