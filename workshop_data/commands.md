# Ansible installation

- You have ansiblecm installed on ansiblecm.
- Check ./workshop_data/prov-ansible.sh.
- Piece of cake.

On windows, check:https://doauto.blog/2016/12/22/ansible-windows-rodando-ansible-a-partir-do-windows-com-docker/

ansible -i inventory all -m ping
ansible -i inventory all -m ping -u vagrant --ask-pass

# The inventory

- And group_vars
- And the lousy/insecure/dumb way of storing passwords


# Ansible ad-hoc
ansible -i inventory all -m shell -a "cat /etc/hosts"
ansible -i inventory m1 -m setup

# Simple ansible playbook
ansible-playbook -i inventory plays/ex1/package-file-service.yml

# Templates, Variables and Facts
ansible-playbook -i inventory plays/ex1/package-file-service-template.yml
