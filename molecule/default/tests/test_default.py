#!/usr/bin/env python

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

# have a look at https://testinfra.readthedocs.io/en/latest/modules.html to see the different possible tests


def test_systemd_service(host):
    assert host.service("postfix.service").is_enabled


def test_config(host):
    postfix_check = host.run_expect([0], "postfix check")
    assert postfix_check.stderr == ""
    assert postfix_check.stdout == ""
    assert postfix_check.rc == 0


def test_postmap(host):
    file_name = "/etc/postfix/transport"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o444
    assert file.contains("*            smtp:outbound-relay.my.domain")


def test_postalias(host):
    file_name = "/etc/aliases"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o444
    assert file.contains("postmaster:    root")
    assert file.contains("foo:           bar")
