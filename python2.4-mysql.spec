Summary:	Python interface to MySQL
Name:		python2.4-mysql
Version:	1.2.2
Release:	%mkrel 7
License:	GPL
Group:		Development/Python
URL:		http://sourceforge.net/projects/mysql-python/
Source0:	http://prdownloads.sourceforge.net/mysql-python/MySQL-python-%{version}.tar.gz
BuildRequires:	python2.4-setuptools
BuildRequires:	python2.4-devel
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
Requires:	    python2.4
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Python interface to MySQL-3.2 and beyond

MySQLdb is an interface to the popular MySQL database server for Python.
The design goals are:

-     Compliance with Python database API version 2.0 
-     Thread-safety 
-     Thread-friendliness (threads will not block each other) 
-     Compatibility with MySQL-3.23 and later

This module should be mostly compatible with an older interface written by Joe
Skinner and others. However, the older version is a) not thread-friendly, b)
written for MySQL 3.21, c) apparently t actively maintained. No code from that
version is used in MySQLdb. MySQLdb is free software.

%prep
%setup -q -n MySQL-python-%{version}

%build
export CFLAGS="%{optflags}"
python2.4 setup.py build

%install
rm -rf %{buildroot}
python2.4 setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README doc/*

