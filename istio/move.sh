#!/bin/bash

sudo cp /home/vagrant/integrations-core/istio/conf.yaml.example /etc/dd-agent/conf.d/istio.yaml
sudo cp /home/vagrant/integrations-core/istio/datadog_checks/istio/istio.py /etc/dd-agent/checks.d/istio.py

sudo /etc/init.d/datadog-agent restart

# less +F /var/log/datadog/collector.log
tail -f /var/log/datadog/collector.log
