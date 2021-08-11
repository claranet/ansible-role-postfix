#!/usr/bin/python3
import re
import yaml

# http://www.postfix.org/master.5.html
#   Each logical line defines a single Postfix service. Each service is identified by its name and  type.
# so we use "name type" as key

master_cf = open("master.cf")

services = {}
last_service = None

for line in master_cf:
    # comment
    if line.startswith("#"):
        continue

    # whitespace-only line
    if re.match(r"\s*$", line):
        continue

    # a line that starts with whitespace continues a logical lin
    if re.match(r"\s", line):
        services[last_service]["command"] += " " + line.strip()
        continue

    # A logical line starts with non-whitespace text
    line_splited = line.split(maxsplit=7)

    service_key = ' '.join(line_splited[0:2])

    services[service_key] = {
        "private": line_splited[2],
        "unpriv": line_splited[3],
        "chroot": line_splited[4],
        "wakeup": line_splited[5],
        "maxproc": line_splited[6],
        "command": line_splited[7].strip()
    }

    last_service = service_key

del services["smtp inet"]

print(yaml.dump({"postfix_master_conf_default_...": services}, width=10000))
