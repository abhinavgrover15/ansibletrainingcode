Ansible mm-Jumbo Role
========================

Description: This role is used for placing and updating configuration and property files, creating neccessary directory structures and installig custom packages on the remote servers.



Requirements
------------
Steps to import a new Project:

  -- Create <project>-vars.yml file under vars directory with all the required variables defined with values.
  -- Create <project> directory under templates/files directory.
  -- As per the project's requirement scan all the tasks defined in this role and create respective folders under templates/<project> directory, and place respective files in them with .j2 extension.
  -- As per the project's requirement scan all the tasks defined in this role and create respective folders under files/<project> directory, and place respective files in them.


Explaination
------------

The tasks defined in this role executes as per 
  -- variables defined under vars/<project>-vars.yml file.
  -- directories defined under files/<project> or templates/<project> directories, as it scans the filesystem as places the files under them to the respective folder on the remote servers.

Installation
------------

Add this role under the project's playbook roles section.


Role Variables
--------------

  a.) custom_dirs : provide list of directories to be created on the remote servers.
		e.g: custom_dirs: ["/opt/prop","/opt/apache/htdocs"]

  b.) custom_files_loc : Name of folder under which all the property files will reside.
		e.g: custom_files_loc: "/opt/prop"

  c.) custom_dirs_owner: username which will be the owner of directories created using "custom_dirs".
  		e.g: custom_dirs_owner: "apache"

  d.) php_pear_extensions: list of pear/pecl packages to be installed on the remote server.
		e.g: php_pear_extensions:
		  		- pecl/solr

  e.) php_packages: list of php additional modules to be installed
  		e.g: php_packages:
  				- php56w
  				- php56w-bcmath
  
  f.) packages_x86_64: List of packages to be installed on the server with arch type x86_64.
  		e.g: packages_x86_64:
  				- pkg_name: postfix
    			  pkg_version: 2.10.1-6.el7
  				- pkg_name: zlib
                  pkg_version: 1.2.7-17.el7
  
  g.) packages_noarch: List of packages to be installed on the server with arch type noarch.
  		e.g: packages_noarch:
  				- pkg_name: mod_security_crs
    			  pkg_version: 2.2.9-1.el7
  
  h.) systemdunits_loc: custom location to place systemctl files.
  		e.g: systemdunits_loc: "/etc/systemd/system"
  
  i.) npm_packages: list of npm packages to be installed.
  		e.g: npm_packages:
   				- "@angular/cli"
  
  j.) custom_hiddenfiles_loc: Name of the folder in which all the hidden files will be placed.
  		e.g: custom_hiddenfiles_loc: "/opt/Apache/prime"


