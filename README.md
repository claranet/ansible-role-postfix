# Ansible role - postfix
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-postfix?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-postfix?style=flat-square)](https://github.com/claranet/ansible-role-postfix/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-postfix/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-postfix/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.9-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/postfix)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure Postfix

## :warning: Requirements

Ansible >= 2.9

## :zap: Installation

```bash
ansible-galaxy install claranet.postfix
```

## :gear: Role variables

Variable                            | Default value                                              | Description
------------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------
postfix_main_conf                   | {}                                                         | Configure `/etc/postfix/main.cf`
postfix_main_conf_default           | See [defaults/main/main.yml](defaults/main/main.yml)       | Default main configuration, will be merged with `postfix_main_conf`
postfix_master_conf                 | {}                                                         | Configure `/etc/postfix/master.cf`
postfix_master_conf_default_buster  | See [defaults/main/buster.yml](defaults/main/buster.yml)   | Default master configuration for Debian Buster, will be merged with `postfix_master_conf`
postfix_master_conf_default_stretch | See [defaults/main/stretch.yml](defaults/main/stretch.yml) | Default master configuration for Debian Stretch, will be merged with `postfix_master_conf`
postfix_postmap                     | {}                                                         | Dictionary: postmap file as key, template file as value `postfix_postmap: {"/etc/postfix/transport": "my_template"}
postfix_postalias                   | {}                                                         | Dictionary: postalias file as key, template file as value `postfix_postalias: {"/etc/aliases": "my_template"}

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - role: claranet.postfix
      postfix_postmap:
        /etc/postfix/transport: my_template
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
