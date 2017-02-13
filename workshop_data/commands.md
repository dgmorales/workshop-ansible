# Ansible installation

- You have ansiblecm installed on ansiblecm.
- Check ./workshop_data/prov-ansible.sh.
- Piece of cake.

On windows, check:https://doauto.blog/2016/12/22/ansible-windows-rodando-ansible-a-partir-do-windows-com-docker/

```
ansible -i inventory all -m ping
ansible -i inventory all -m ping -u vagrant --ask-pass
```

# Basics
## The inventory

- And group_vars
- And the lousy/insecure/dumb way of storing passwords
- There are host_vars too.

## Ansible ad-hoc
```
ansible -i inventory all -m shell -a "cat /etc/hosts"
ansible -i inventory m1 -m setup
```

- User, password, sudo

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

`ansible-playbook -i inventory plays/ex3/webserver.yml`

# Roles

The right way.

## Creating a Roles

## Using roles and ansible-galaxy

# Orchestration, rolling upgrades, etc.

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
