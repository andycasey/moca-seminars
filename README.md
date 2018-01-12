Monash Centre for Astrophysics Seminar Series
---------------------------------------------

Now with fewer humans.™

Launch on Nectar Cloud
----------------------

1. Create an instance of flavor `m2.tiny` or above and select the image name as `NeCTAR Ubuntu 16.04 LTS (Xenial) amd64 (287.3 MB)`. Make sure you can access the instance with a Key Pair and enable `ssh` and `http` security groups.

2. Set the Post-Creation script source as Direct Input and enter this into the Script Data box: `wget https://raw.githubusercontent.com/andycasey/moca-seminars/master/etc/setup.sh | sudo source setup.sh`
