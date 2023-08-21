# 0x0A. Configuration management

## Requirements
   - Install `puppet`
     - $ apt-get install -y ruby=1:2.7+1 --allow-dowgrades
     - $ apt-get install -y ruby-augeas
     - $ apt-get install -y ruby-shadow
     - $ apt-get install -y puppet

[Puppet 5 Docs]
(https://intranet.alxswe.com/rltoken/fsIr2xFkJHTkaXwqZFFcbA)

   - Install `puppet-lint`
     - $ gem install puppet-lint


---

### [0. Create a file](./1-

install_a_package.pp)
* Using Puppet, create a file in `/tmp`.

* Requirements:

  - File path is `/tmp/school`
  - File permission is `0744`
  - File owner is `www-data`
  - File group is `www-data`
  - File contains `I love Puppet`


### [1. Install a package](./1-

install_a_package.pp)
* Using Puppet, install `flask` from `pip3`.

* Requirements:

  - Install `flask`
  - Version must be `2.1.0`


### [2. Execute a command](./2-

execute_a_command.pp)
* Using Puppet, create a manifest that kills a process named `killmenow`.

* Requirements:

  - Must use the `exec` Puppet resource
  - Must use `pkill`

---

## Author
* **Richard Akpabio** - [Rikpabi]
(http://github.com/Rikpabi)

