# Ansible installation

- You have ansiblecm installed on ansiblecm.
- Check ./workshop_data/prov-ansible.sh.
- Piece of cake.

On windows, check:https://doauto.blog/2016/12/22/ansible-windows-rodando-ansible-a-partir-do-windows-com-docker/

# Basics

Enter the ansiblecm vm and got to /vagrant:

```
vagrant ssh ansiblecm
cd /vagrant
```

## The inventory

```
ansible -i inventory all -m ping
ansible -i inventory all -m ping --ssh-extra-args="-o StrictHostKeyChecking=no"
ansible -i inventory all -m ping -u vagrant --ask-pass
```

- And group_vars
- And the lousy/insecure/dumb way of storing passwords
- There are host_vars too.

## Ansible ad-hoc, and Facts
```
ansible -i inventory all -m shell -a "cat /etc/hosts"
ansible -i inventory m1 -m setup
ansible -i inventory m1 -m setup -a filter='ansible_processor_*'
```

You can have local custom facts, written as json or INI files, or a script in any language:
http://docs.ansible.com/ansible/playbooks_variables.html#local-facts-facts-d

## Simple ansible playbook
`ansible-playbook -i inventory plays/ex1/package-file-service.yml`

## Templates, Variables and Facts
`ansible-playbook -i inventory plays/ex1/package-file-service-template.yml`

## Check mode and diff
`ansible-playbook -i inventory plays/ex1/package-file-service-template.yml --check`
`ansible-playbook -i inventory plays/ex1/package-file-service-template.yml --check -D`

## lineinfile example
`ansible-playbook -i inventory plays/ex1/oneline.yml`

- See also ini_file: http://docs.ansible.com/ansible/ini_file_module.html

## Loops and an idempotency note
`ansible-playbook -i inventory plays/ex1/loop.yml`

- Ansible **is** idempotent. It all depends on module quality and purpose.
- **Several** other loop constructs (with_*).

## Conditionals, ignore_errors and a more complex playbook

`ansible-playbook -i inventory plays/ex2/nginx.yml --check`
`ansible-playbook -i inventory plays/ex2/nginx.yml`
`ansible-playbook -i inventory plays/ex2/nginx.yml -e use_epel=no`

Note some details:
- when clause (and "skipping ..." messages)
- block "module"
- Tags (myapp)
- See ignore_errors and ansible_check_mode
- Overriding vars via cli (-e)
- One jinja filter (|bool) and quoting annoyances:

```
  ...
      when: not {{ use_epel|bool }}
  ...
      when: "{{ use_epel|bool }} == true"
  ...
```

Also, we have 3 things here: epel, nginx, and myapp.

# Splitting the nginx example with includes

Includes are not so good, but can be useful.

`ansible-playbook -i inventory plays/ex3/site.yml`

- Variables, plays and tasks includes
- Includes can override variables and be used for multiple instances of a resource

# Roles

The right way. A bit like includes done right.

Advantages:
- More contained. Everything in one place.
- Easy to redistribute.
- Auto search things in appropriate paths.
- Default variables.
- Can have metadata and dependencies.

## Creating a role

We can use ansible-galaxy init:

```
mkdir roles
ansible-galaxy init example.epel -p ./roles
ansible-galaxy init example.nginx -p ./roles
```

An environment playbook: testing.yml.

`ansible-playbook -i inventory testing.yml -l webservers`

Note:
- Two ways to call a role
- *when* used in the role call
- Variable precedence
- Should myapp be a role?
  - We could make it so and use role dependencies for nginx and epel

## Using roles and ansible-galaxy

Let's add haproxy. Let's use a role from Ansible Galaxy.

https://galaxy.ansible.com/list#/roles?page=1&page_size=10&autocomplete=haproxy&order=-download_count,name

`ansible-playbook -i inventory testing.yml`

Note:

- Backend haproxy servers var could be fully built from hostvars
  - "Ansible is not a full language"
  - Need a custom jinja filter?


# Orchestration, rolling upgrades, etc.

`ansible-playbook -i inventory plays/rolling-update.yml`

While on pause, check that only one machine answers using the balancer:
`curl http://192.168.100.13`

Note:
- serial: 1
- delegate_to and {{ inventory_hostname }}
- with_items being used because could be several load balancers
- wait_for and interactive pause
- could use reboot if needed

# Other topics

## Shell/command modules, overriding changed/failed, register results

## Quick Tour on modules

Special mention to:

- script
- bigip modules
- notification modules
- debug
- assert
- trondhenes dsc windows modules
- ...

## Builtin variables

## Ansible Vault

## vars_prompt

## Facts caching

# Reference

- Ansible Docs, specially:
  - Roles
  - Best Practices
  - Variables
  - Testing
  - ...
- Ansible Up and Running
- Telegram @ansiblebr
