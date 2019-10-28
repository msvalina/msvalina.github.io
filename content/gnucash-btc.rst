###########################################################################
How to patch with Bitcoin, build and deploy GnuCash in Docker on Ubuntu PPA
###########################################################################

:date: 2019-09-08 10:45
:author: marijan
:category: programming
:tags: bitcoin, gnucash, ubuntu, linux, docker
:slug: patch-with-btc-build-and-deploy-gnucash-in-docker-on-ubuntu-ppa
:lang: en
:cover: assets/images/header_doggy_three.jpg

Main goal of this article is to document high level steps. Steps
to patch, build, and deploy `GnuCash`_ on Ubuntu PPA (Personal Package
Archive). Targeted audience is mid-level technical people. Also others who
want to learn more about package building, Docker practices, and Linux.

Docker builds the image. GPG (Gnu Privacy Guard) signs package. dput
publishes packages on Ubuntu PPA. From GnuCash perspective added value is
finding all the puzzles pieces. At the end I will compare
this build process with Archlinux pkgbuild.

.. _GnuCash:  https://www.gnucash.org/

Motivation and background
=========================

There is `no official Bitcoin support`_ in GnuCash. It seems like there
won't be one in future from GnuCash developers. On Archlinux I'm using
`gnucash-xbt from AUR`_. On my other Ubuntu machine I wanted to use the same.
There was no PPA with Bitcoin support in GnuCash. So I created `Ubuntu PPA`_
for myself and others. This wasn't my first build of debian like package.
In past I hacked a Makefile to generate opkg package for OpenWRT. It was
useful knowledge to have for this task.


.. _gnucash-xbt from AUR:  https://aur.archlinux.org/packages/gnucash-xbt/
.. _no official Bitcoin support:  http://gnucash.1415818.n4.nabble.com/Cryptocurrencies-td4690814.html
.. _Ubuntu PPA:  https://launchpad.net/~msvalina/+archive/ubuntu/gnucash

Where is the code?
==================

You can find `code on github repo`_ and skip over this article. You can
find `Ubuntu PPA packages`_ and install them right away.

.. _code on github repo:  https://github.com/msvalina/ppa-gnucash-xbt
.. _Ubuntu PPA packages:  https://launchpad.net/~msvalina/+archive/ubuntu/gnucash

What puzzle pieces did you use?
===============================

Thanks goes to all this work before mine. It was much easier to solve all the
problems because of these people 💗

- Benedykt Przybyło (b3niup) for original Archlinux AUR pkgbuild
  `gnucash-xbt`_ and xbt.patch
- Dmitry Smirnov for maintaining `Debian GnuCash dpkgbuild`_
- Dale Phurrough for nice GnuCash Dockerfile starting point
  `diablodale/gnucash-dev-docker`_
- Sicklylife for maintaining `vanilla GnuCash Ubuntu PPA`_.
- Andrey Arapov of nixaid.com for writing: `Using GPG inside a docker
  container`_

.. _gnucash-xbt:  https://aur.archlinux.org/packages/gnucash-xbt/
.. _Debian GnuCash dpkgbuild:  https://salsa.debian.org/debian/gnucash/
.. _diablodale/gnucash-dev-docker:  https://github.com/diablodale/gnucash-dev-docker/
.. _vanilla GnuCash Ubuntu PPA:  https://launchpad.net/~sicklylife/+archive/ubuntu/gnucash3.6
.. _Using GPG inside a docker container:  https://nixaid.com/using-gpg-inside-a-docker-container/

What prerequisites understanding is necessary?
==============================================

`Ubuntu Packaging Guide`_ is good starting point, has many useful
information. Guide also depends on debian packaging policies and tools. It is
**important** to know that there are many ways/tools to build debian package.
But two main categories are:

Upstream Developer way
----------------------

- `building using bzr-build`_ Ubuntu Packaging Guide focuses on this one
- `building using git-buildpackage`_

Debian packager way
----------------------

`Quoting from askubuntu`_::

  > In the normal workflow, packager starts by
  > downloading *.orig.tar.gz archive then
  > extracting.
  >
  >    Debian packages can be split into two kinds:
  >    -  native '3.0 (native)' and
  >    -  non-native '3.0 (quilt)'.
  >    They have a slight different way in building.

Check DebianMentorsFaq_ for difference between native and non-native.
This project uses Debian packager way with non-native(quilt) type.

.. _Ubuntu Packaging Guide:  http://packaging.ubuntu.com/html/index.html
.. _building using bzr-build:  https://jameswestby.net/bzr/builddeb/user_manual/
.. _building using git-buildpackage:  https://wiki.debian.org/PackagingWithGit
.. _Quoting from askubuntu:  https://askubuntu.com/questions/1087569/deploying-own-debian-package-to-launchpad
.. _DebianMentorsFaq:  https://wiki.debian.org/DebianMentorsFaq#What_is_the_difference_between_a_native_Debian_package_and_a_non-native_package.3F

Why would you build inside Docker?
==================================

Infrastructure as Code principle is valuable and something Docker forces you
to do. Also I don't want to clutter mine laptop with build dependencies.
There are other ways to do that but, I also wanted to gather
some more experiences with Docker.


Main procedures
===============

Docker image will

- build the environment for building GnuCash
- patch GnuCash with Bitcoin currency type
- build debian source package
- sign it with gpg (works with YubiKey)
- upload it to the Ubuntu PPA (Personal Package Archive)

Interesting parts: Dockerfile
===============================

First job of docker is to install all needed dependencies for build tools and
for GnuCash itself. Other interesting thing is headache less permissions with
docker volume. For that we create user and group in Dockerfile. They will
have the same UID and GID as user which is building the container

.. code-block:: Dockerfile

    RUN groupadd --system \
        --gid ${GID:-1000} \
        ubuntu

    RUN useradd --system \
        --create-home \
        --home-dir /home/ubuntu \
        --shell /bin/bash \
        --uid ${UID:-1000} \
        --gid ${GID:-1000} \
        --groups sudo \
        --password "$(openssl passwd -1 ubuntu)" \
        ubuntu

    USER ubuntu
    WORKDIR /home/ubuntu/ppa-gnucash-xbt

    CMD ./build.sh

Then we create docker container with volumes from user that created docker
image

.. code-block:: shell

    docker run --rm --tty --interactive \
      --volume ${HOME}/.gnupg/:/home/ubuntu/.gnupg/:ro \
      --volume /run/user/$(id -u)/:/run/user/$(id -u)/:ro  \
      --volume ${HOME}/path/to/ppa-gnucash-xbt/:/home/ubuntu/ppa-gnucash-xbt/ \
      --name dpkg-build-gnucash \
      gnucash-xbt-ubuntu-bionic-pkgbuild bash

Now data from repo is available both on host and container. Nobody will mess
up owner, group or permissions.

What happens on new upstream release?
=====================================

On new upstream release build.sh needs change. Latest upstream source url,
sha256 checksum of that source need modification. Other steps are automatic.


Interesting parts: build.sh script
==================================

In current form build.sh only builds debian source package. It doesn't
compile GnuCash itself. To build it for local use and testing run container
with bash and issue after running build.sh

.. code-block:: shell

    cd ppa_builddir
    dpkg-buildpackage --build=binary

How long will I maintain PPA?
===============================

I will maintain it as long as I use GnuCash. I used it for last 5
years. So if we go by `Lindy Effect`_ I will maintain it for 5 more years.
But beware I'm looking at HLedger_ as a replacement.
Feel free to take over maintaining when PPA becomes out of date.

.. _Lindy Effect:  https://en.wikipedia.org/wiki/Lindy_effect
.. _HLedger:  https://hledger.org/


Conclusion
==========

So looking back and seeing how much time it would take me to patch and build
GnuCash for Ubuntu I can say that my intuition was completely off... It took
me 5 times more time then I anticipated. Comparing that to building on
Archlinux's, it is complex. But I get way there is so many tools and
policies in Ubuntu/Debian world. History and compatibility need preservation.
But it takes a while to get gist of things. Also Docker and GPG issues took
time as well. Hand in hand it is valuable experience for me, especially
because Ubuntu Bionic is my main OS now. For a junior level Linux guy, if
such category can be defined at all. It is real pain to build, patch and
deploy dpkg package. If you are still reading. Thank you. Hope you got
something out of it. 💗
