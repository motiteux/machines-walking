Title: Developing Django inside a Vagrant box
Slug: django-vagrant-box
Author: 'Marc-Olivier Titeux'
Date: 2014-05-13
Category: computers
Tags: python, django, vagrant
Summary: Developing Django in Virtualbox made using Vagrant


It seems to me it is always a good idea to have a virtual machine for development. And it seems I am not the [first][fideloper] and [only][pixelmedia] to think about it, which tends to validate the approach...

There are many approaches to this, and my preferred is using [Vagrant][vagrantsite]. There are a lot of tutorials ([here][vagrant1], [here][vagrant2] or [here][vagrant3]), and I am not going to make yet another one. One of my current hackish occupation is to develop a Django website, using a Postgres/nginx/supervisor/Django1.7/Python3 stack (yeah, a classic now). Actually, I am stretching myself since I left Django at version 1.4 with Python 2.
It takes me time, and I do not want to mess with my laptop. So a VM seems the perfect way. 

However, for some reason, I cannot get my prefered browser, with all its tools (Chrome) working properly under this VM ([VirtualBox][virtualbox]). Or IE11 as well for what it's worth. Thus I was looking for a virtualizing my environment and came up with this [vagrant box][my_vagrant] of a Debian Wheezy 7.6 image with the aforementioned stack. It suits me quite well for developing apps for Django. You can check out the README for customizing it to your needs.



[fideloper]: http://fideloper.com/develop-in-vm
[pixelmedia]: http://www.pixelmedia.com/garage/software-development-why-i-using-virtual-machines
[vagrantsite]: https://www.vagrantup.com/
[vagrant1]: 
[vagrant2]:
[vagrant3]:
[virtualbox]: http://www.virtualbox.org/
[my_vagrant]
