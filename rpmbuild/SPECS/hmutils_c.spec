%define debug_package %{nil}

Name:    hmutils-c
Version: %version
Release: 1%{?dist}
Summary: This package includes the implementation of utils
Group:   Applications/Internet
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source0: hmutils-c-%{version}.tar.gz

%description
There is a shared lib in the rpm which have a basic feature of utils

%prep
%setup

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/libs/
mkdir -p $RPM_BUILD_ROOT/usr/include/
install -D %_topdir/BUILD/hmutils-c-%{version}/version.h $RPM_BUILD_ROOT/usr/include/hmutils/version.h
install -D %_topdir/BUILD/output/libhmutils-c.so $RPM_BUILD_ROOT/usr/lib/libhmutils-c.so
install -D %_topdir/BUILD/output/libhmutils-c.so.%{version} $RPM_BUILD_ROOT/usr/lib/libhmutils-c.so.%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
rm -rf /usr/lib/libhmutils-c.so
ln -s /usr/lib/libhmutils-c.so.%{version} /usr/lib/libhmutils-c.so

%files
/usr/include/hmutils/*.h
/usr/lib/libhmutils-c.so.%{version}
/usr/lib/libhmutils-c.so

