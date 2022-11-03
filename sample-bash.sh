echo 1. Whats in this directory ?
ls -a

echo "This script is about to run another script."
sh ./unit_tests/run_L1_full_test.sh
echo "This script has just run another script."
