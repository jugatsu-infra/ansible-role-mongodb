import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# check if MongoDB package is installed
def test_mongodb_is_installed(host):
    package = host.package('mongodb-org')
    assert package.is_installed
    assert package.version.startswith('3.4.7')


# check if MongoDB is enabled and running
def test_mongod_is_running(host):
    mongo = host.service('mongod')
    assert mongo.is_running
    assert mongo.is_enabled


# check if configuration file contains the required line
def test_mongod_config_file(File):
    config_file = File('/etc/mongod.conf')
    assert config_file.contains('port: 27017')
    assert config_file.contains('bindIp: 127.0.0.1')
    assert config_file.is_file


# check if mongod process is listening on localhost
def test_mongod_is_listening(host):
    port = host.socket('tcp://127.0.0.1:27017')
    assert port.is_listening
