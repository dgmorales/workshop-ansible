# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.vm.box = "bento/centos-7.2"
  # set some names <=> ips inside all machines
  # config.vm.provision :hosts do |h|
  #     h.add_host '192.168.100.7', ['ansible']
  #     h.add_host '192.168.100.11', ['m1.local', 'm1']
  #     h.add_host '192.168.100.12', ['m2.local', 'm2']
  # end

  #config.vm.provider "virtualbox" do |vb|
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "512"
  #end

  # we need to this so vagrant generates the ansible inventory for us
  #config.vm.provision "ansible" do |ansible|
  #  ansible.playbook = "./nothing.yml"
  #end

  config.vm.define :ansiblecm do |cm|
    #cm.vm.provider "virtualbox" do |vb|
    #   vb.memory = "1024"
    #end
    cm.vm.provision "shell", path: "./workshop_data/prov-ansible.sh"
    cm.vm.hostname = "ansiblecm.local"
    cm.vm.network "private_network", ip: "192.168.100.7", virtualbox__intnet: "cmnet"
    #cm3.vm.network "forwarded_port", guest: 80, host: 9080
    #cm3.vm.network "forwarded_port", guest: 4440, host: 4440
  end

  # config.vm.define :tower do |cm5|
  #   cm5.vm.box = "ansible/tower"
  #   cm5.vm.provider "virtualbox" do |vb|
  #      vb.memory = "1024"
  #   end
  #   cm5.vm.hostname = "tower.local"
  #   cm5.vm.network "private_network", ip: "192.168.100.9", virtualbox__intnet: "cmnet"
  #   cm5.vm.network "forwarded_port", guest: 443, host: 8443
  #   cm5.vm.boot_timeout = 600
  # end

  config.vm.define :m1 do |m1|
    m1.vm.hostname = "m1.local"
    m1.vm.network "private_network", ip: "192.168.100.11", virtualbox__intnet: "cmnet"
    m1.vm.network "forwarded_port", guest: 15672, host: 15672  # rabbitmq mgmt
    m1.vm.network "forwarded_port", guest: 80, host: 8081  # nginx
  end
  config.vm.define :m2 do |m2|
    m2.vm.hostname = "m2.local"
    m2.vm.network "private_network", ip: "192.168.100.12", virtualbox__intnet: "cmnet"
    m2.vm.network "forwarded_port", guest: 15672, host: 25672  # rabbitmq mgmt
    m2.vm.network "forwarded_port", guest: 80, host: 8082  # nginx
  end
   config.vm.define :m3 do |m3|
    m3.vm.hostname = "m3.local"
    m3.vm.network "private_network", ip: "192.168.100.13", virtualbox__intnet: "cmnet"
   end

end
