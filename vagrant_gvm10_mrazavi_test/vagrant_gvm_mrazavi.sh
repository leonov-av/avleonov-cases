#!/bin/bash

# Making GVM10/OpenVAS10 scanner host

distribution="ubuntu"
release="bionic64"
network="mynetwork"
ip="192.168.50.5"
folder_name="openvas_mrazavi_"$distribution"_"$release

mkdir vagrants
rm -rf vagrants/$folder_name
mkdir vagrants/$folder_name/
cd vagrants/$folder_name/
#vagrant init $distribution/$release
#cat Vagrantfile  | egrep -v " *#.*" | grep -v "^$"
echo "Vagrant.configure(\"2\") do |config|
  config.vm.box = \"$distribution/$release\"
  config.vm.network \"forwarded_port\", guest: 22, host: 3334
  config.vm.network \"forwarded_port\", guest: 4000, host: 4000
  config.vm.network \"private_network\", ip: \"$ip\",
    virtualbox__intnet: \"$network\"
end" > Vagrantfile

vagrant up

### Go to vagrants/$folder_name/, run `vagrant ssh` and run commands from gvm_mrazavi_commands.txt on the host

#vagrant destroy -f
#cd ../../

