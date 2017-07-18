import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_somedb_is_installed(Package):
    mariadb = Package("mariadb")
    mysqld = Package("mysqld")
    assert (mariadb.is_installed or mysqld.is_installed)


def test_somedb_is_running(Service):
    mariadb = Service("mariadb")
    mysqld = Service("mysqld")
    assert (mariadb.is_running or mysqld.is_running)
    assert (mariadb.is_enabled or mysqld.is_enabled)


def test_mysql_port_is_listening(Socket):
    mysql_port = Socket("tcp://0.0.0.0:3306")
    assert mysql_port.is_listening
