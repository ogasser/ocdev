ocdev (0.0.10)

* Fix ci

ocdev (0.0.9)

* Fix setup problems on mysql & postgresql

ocdev (0.0.8)

* Add **DEFINE('DEBUG', true);** to autoconfigs

ocdev (0.0.7)

* Disable enabling of files_sharing, files_encryption, files_external, user_ldap and files_versions apps since they might not be needed and can be activated by php -f console.php app:enable files_versions for instance

ocdev (0.0.6)

* Add generator for ci setups that generates configs for core and setups an install for tests

ocdev (0.0.5)

* Add templates for ownCloud 7

ocdev (0.0.4)

* Move to setuptools for distributing
* Fail more gracefully if app directory exists already
* Transition to reST documentation files

ocdev (0.0.3)

* Fix bug that breaks calling ocdev setup base


ocdev (0.0.2)

* Add support for setting up the development environment


ocdev (0.0.1)

* First release