# $Id: rc-inetd.spec,v 1.1 1999-09-02 07:44:43 kloczek Exp $
Summary:	Wrapper for managing inet service using any kind inet aplication
Summary(pl):	Skrypty do zarz±dzania inet serwisami
Name:		rc-inetd
Version:	0.1
Release:	0.1
Copyright:	GPL
Group:		Base
Group(pl):	Bazowe
Source:		%{name}-%{version}.tar.gz
BuildPrereq:	inetdaemon
Buildroot:	/tmp/%{name}-%{version}-root

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

%clear
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,754)
%attr(754,root,root) /etc/rc.d/init.d/rc-inetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd.conf
