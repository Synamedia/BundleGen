echo making directory DAC-SDK
mkdir DAC-SDK

echo Where am I ?
pwd

echo Whats in this directory ?
ls -al

echo Whats in the CD directory?
ls -al /home/runner/work/BundleGen/BundleGen/DAK-SDK


cd /home/runner/work/BundleGen/BundleGen/DAK-SDK
git clone https://android.googlesource.com/tools/repo
./repo/repo init -u https://github.com/stagingrdkm/lgpub/ -m manifests/dac-dunfell-3.1.6-manifest.xml
