Title: How to repair mysql workbench on CentOS
Slug: how-to-repair-mysql-workbench-centos
Date: 2013-12-08
Author: Marc-Olivier Titeux
Email: marcolivier.titeux@gmail.com
Summary: Check the requirements...

One of the issue on linux with mysql-workbench is linked to Python. 

1. First, check the requirement list is depicted on [mysql-workbench page](http://dev.mysql.com/doc/workbench/en/wb-requirements-software.html) for the supported platforms. 

2. On CentOS, you could have installed it using yum and [remi repos](http://blog.famillecollet.com/post/2012/08/11/mysql-workbench-5.2.41-en). If this is the case, reinstall it:
    yum --enablerepo=remi reinstall mysql-workbench
    
3. If you installed it using the tar.gz package, check that you have the following Python package for the linux version: [python-paramiko](https://github.com/paramiko/paramiko/)
    if you use pip: pip install paramiko
    if you use setuptools: 
        easy_install pycrypto
        easy_install paramiko
   
Let me know if it works for you.
