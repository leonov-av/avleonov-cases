#!/bin/bash

# Making a target virtual machine for vulnerability scans

distribution="ubuntu"
release="bionic64"
version="20190508.0.0"
network="mynetwork"
ip="192.168.50.4"
folder_name="scan_target_"$distribution"_"$release

mkdir vagrants
rm -rf vagrants/$folder_name
mkdir vagrants/$folder_name/
cd vagrants/$folder_name/
#vagrant init $distribution/$release --box-version "$version"
#cat Vagrantfile  | egrep -v " *#.*" | grep -v "^$"
echo "Vagrant.configure(\"2\") do |config|
  config.vm.box = \"$distribution/$release\"
  config.vm.box_version = \"$version\"
  config.vm.network \"forwarded_port\", guest: 22, host: 3333
  config.vm.network \"private_network\", ip: \"$ip\",
    virtualbox__intnet: \"$network\"
end" > Vagrantfile

vagrant up

vagrant ssh -c "sudo useradd test_user;"
vagrant ssh -c "echo -e \"test_password\ntest_password\" | sudo passwd test_user"
vagrant ssh -c "sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config"
vagrant ssh -c "sudo service sshd restart"


#vagrant destroy -f
#cd ../../

# ssh test_user@localhost -p 3333