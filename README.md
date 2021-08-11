# postfix

Installation et configuration de postfix.

# Usage

## requirements.yml

```yml
- src: git@git.fr.clara.net:claranet/spp/projects/ansible/postfix.git
  scm: git
  version: "…"
```

## Examples

### Minimal

```yaml
- hosts: all
  roles:
    - postfix
```

### Transport

```yaml
- hosts: all
  vars:
    postfix_postmap:
      /etc/postfix/transport: my_template
  roles:
    - postfix
```

# Variables

* `postfix_main_conf`: permet de générer `/etc/postfix/main.cf` (default: voir `postfix_main_conf_default`)
* `postfix_master_conf`: permet de générer `/etc/postfix/master.cf` (default: voir `postfix_master_conf_default_buster`, ou `…_stretch`)
* `postfix_postmap`: dictionnaire contenant en clé le fichier destination et en value le template source.
	Si le fichier destination est modifier la commande `postmap <fichier>` est lancé.
	(default: `{}`)
* `postfix_postalias`: dictionnaire contenant en clé le fichier destination et en value le template source.
	Si le fichier destination est modifier la commande `postalias <fichier>` est lancé.
	(default: `{}`)
