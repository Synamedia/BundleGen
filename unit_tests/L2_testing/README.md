#For L2 Testing
Main objective of L2 testing is verifying the bundle image for an individual app which was taken from oci image.

## Pre-requests
Create three empty folders named as oci_images, bundlegen_images and metadatas inside the unit_tests/L2_testing folder.
Build the oci image/Pre-build oci image and store the oci image tar file in unit_tests/L2_testing/oci_images folder.
Build the bundlegen image/Pre-build bundlegen image and store the bundlegen image tar file in unit_tests/L2_testing/bundlegen_images folder.
unit_tests/L2_testing/metadatas folder is for storing the appmetadata.json (which is extracting when test script runs).

## Environment Setup
Python version should be greater than or equal to 3.7 to run L2_testing.
Once installed the python version, setup the pip install
```console
    $ cd BundleGen
    $ pip install -r requirements.txt
    $ pip install --editable .
```

## How to run L2 test
Required Parameters to run L2 test(run_L2_test.py)
Appname and Platformname.
Test run_L2_test.py script will do below things,
    Extracting oci image and storing in unit_tests/L2_testing/oci_images folder.
    Extracting bundle image in unit_tests/L2_testing/bundlegen_images folder.
    Extracting appmetadata.json from oci image, storing into unit_tests/L2_testing/metadatas folder.
    After running L2 test script file it removes all extracted ones and remains only tar files in respective folders.    
Run the L2 test using the run_L2_test.py file.
```console
    $ cd unit_tests/L2_testing
    $ python run_L2_test.py -a appname -p platformname
```
