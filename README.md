Monash Centre for Astrophysics Seminar Series
---------------------------------------------

Now with fewer humans.™

Launch on Nectar Cloud
----------------------

1. [Launch an instance](https://dashboard.rc.nectar.org.au/project/instances/) of flavor `m2.tiny` or above and select the image name as `NeCTAR Ubuntu 16.04 LTS (Xenial) amd64 (287.3 MB)`. Make sure you can access the instance with a Key Pair and enable `ssh` and `http` security groups before launching.

2. Connect to the instance using your ssh key: `ssh -i cloud.key ubuntu@<IP_ADDRESS>`

3. Run the command `wget https://raw.githubusercontent.com/andycasey/moca-seminars/master/etc/setup.sh | sudo sh setup.sh`

4. You should be able to access the initial website at `http://<IP_ADDRESS>`
