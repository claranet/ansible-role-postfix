import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

# have a look at https://testinfra.readthedocs.io/en/latest/modules.html to see the different possible tests


def test_systemd_service(host):
    assert host.service("postfix.service").is_enabled
    assert host.service("postfix@-.service").is_running


def test_config(host):
    postfix_check = host.run_expect([0], "/usr/sbin/postfix check")
    assert postfix_check.stderr == ""
    assert postfix_check.stdout == ""
