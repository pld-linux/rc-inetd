# $Id: rc-inetd.spec,v 1.22 2001-01-21 12:22:56 zagrodzki Exp $
Summary:	Wrapper for managing inet service using any kind inet aplication
Summary(pl):	Skrypty do zarz±dzania inet serwisami
Name:		rc-inetd
Version:	0.13
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
/sbin/chkconfig --add rc-inetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/rc-inetd start\" to start rc-inetd service."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd stop 1>&2
	fi
	/sbin/chkconfig --del rc-inetd
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {template_inetd,template_service}.gz
%attr(754,root,root) /etc/rc.d/init.d/rc-inetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd.conf
%dir /etc/sysconfig/rc-inetd
