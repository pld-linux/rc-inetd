# $Id: rc-inetd.spec,v 1.9 1999-10-23 08:02:44 waszi Exp $
Summary:	Wrapper for managing inet service using any kind inet aplication
Summary(pl):	Skrypty do zarządzania inet serwisami
Name:		rc-inetd
Version:	0.7
Release:	1
Copyright:	GPL
Group:		Base
Group(pl):	Bazowe
Source:		%{name}-%{version}.tar.bz2
Requires:	inetdaemon
BuildArch:	noarch
Buildroot:	/tmp/%{name}-%{version}-root

%description
Wrapper for managing inet service using any kind inet aplication.

%description -l pl
Skrypty do zarządzania inet serwisami.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd}

install rc-inetd $RPM_BUILD_ROOT/etc/rc.d/init.d
install rc-inetd.conf $RPM_BUILD_ROOT/etc/sysconfig

gzip -9f template_inetd  template_service

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {template_inetd,template_service}.gz
%attr(754,root,root) /etc/rc.d/init.d/rc-inetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd.conf
%dir /etc/sysconfig/rc-inetd
