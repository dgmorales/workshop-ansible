# Ansible Workshop

Requirements:

  - [Vagrant](https://www.vagrantup.com/)
  - [Virtualbox](https://www.virtualbox.org/)


# Instructions

```
vagrant up
vagrant ssh ansiblecm
```

That should get you 4 machines up (ansiblecm, m1, m2, m3), and drop you in the ansiblecm shell. From there you should be able to ping the other ones. Also, ansible is installed on that machine:

```
ping m1
ping m2
ping m3
ansible --help
```

If that all works, you should be good to start.

# Cheat Sheet

Several commands shown in the workshop:
./workshop_data/commands.txt
