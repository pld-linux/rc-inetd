# $Id: rc-inetd.spec,v 1.24 2001-07-25 16:30:59 saq Exp $
Summary:	Wrapper for managing inet service using any kind inet aplication
Summary(pl):	Skrypty do zarz±dzania inet serwisami
Name:		rc-inetd
Version:	0.14
Release:	1
License:	GPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://ftp.pld.org.pl/software/rc-inetd/%{name}-%{version}.tar.bz2
Requires:	inetdaemon
Prereq:		chkconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper for managing inet service using any kind inet aplication.

%description -l pl
Skrypty do zarz±dzania inet serwisami.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd}

install rc-inetd $RPM_BUILD_ROOT/etc/rc.d/init.d
install rc-inetd.conf $RPM_BUILD_ROOT/etc/sysconfig

gzip -9nf template_inetd template_service

%post
DESC="rc-inetd service"; %chkconfig_add

%preun
%chkconfig_del

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {template_inetd,template_service}.gz
%attr(754,root,root) /etc/rc.d/init.d/rc-inetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd.conf
%dir /etc/sysconfig/rc-inetd
