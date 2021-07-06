---
Title: Installing numpy through pip with openBLAS on Debian
Slug: installing-numpy-pip-openblas
Author: 'Marc-Olivier Titeux'
Date: 2014-01-27
Category: computers
Tags: python, scistack, numpy
Summary: Compiling, compiling, compiling...
---


Strangely, I was struggling hard to install numpy 1.8.0 (with pip in a virtualenv) on Debian 7.1 with [OpenBLAS][openblas]. I always got the following error message:

    numpy.distutils.system_info.BlasNotFoundError:

        Blas (http://www.netlib.org/blas/) libraries not found.

        Directories to search for the libraries can be specified in the

        numpy/distutils/site.cfg file (section [blas]) or by setting

        the BLAS environment variable.


After googling (a lot), I stumbled on [gromgull's blog][gromgull] which mentioned at one point to install the header versions of the openblas lib for debian, *aka*

    sudo apt-get install libopenblas-dev liblapack-dev

Though I did not follow the rest of the article. I just tried to install numpy through pip at this stage and everything worked! Actually, that's because there was a [Pull Request accepted in numpy to accept OpenBLAS transparently][pr_openblas], since gromgull's blog entry.

However, afterwards, I decided to remove all blas/atlas/etc lib from stock (all system libs), and compile openblas from source, to get a few performance improvement. To do this, I had to symlink libopenblas lib using update-alternatives (pip install numpy is looking for that specific path. If not there, one should add it or follow gromgull's approach):

    sudo update-alternatives --install /usr/lib/libblas.so.3 libblas.so.3 /usr/local/lib/libopenblas.so 90

And everything went great!


[openblas]: http://www.openblas.net/
[gromgull]: http://gromgull.net/blog/2013/07/multithreaded-scipynumpy-with-openblas-on-debian/
[pr_openblas]: https://github.com/numpy/numpy/pull/3642
