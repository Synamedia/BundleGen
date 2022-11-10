echo making directory DAC-SDK
mkdir DAC-SDK

echo Where am I ?
pwd

echo Whats in this directory ?
ls -al

cd DAK-SDK
git clone https://android.googlesource.com/tools/repo
./repo/repo init -u https://github.com/stagingrdkm/lgpub/ -m manifests/dac-dunfell-3.1.6-manifest.xml
