# $Id: rc-inetd.spec,v 1.31 2003-08-12 15:21:42 qboosh Exp $
Summary:	Wrapper for managing inet service using any kind inet daemon
Summary(pl):	Skrypty do zarz�dzania us�ugami inet
Name:		rc-inetd
Version:	0.14
Release:	1
License:	GPL
Group:		Base
Source0:	ftp://ftp.pld.org.pl/software/rc-inetd/%{name}-%{version}.tar.bz2
# Source0-md5: ee79925472952f8c8c19db3abb985d80
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	inetdaemon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper for managing inet service using any kind inet daemon.

%description -l pl
Skrypty do zarz�dzania us�ugami inet przy u�yciu dowolnego rodzaju
demona inet.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd}

install rc-inetd $RPM_BUILD_ROOT/etc/rc.d/init.d
install rc-inetd.conf $RPM_BUILD_ROOT/etc/sysconfig

%clean
rm -rf $RPM_BUILD_ROOT

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

%files
%defattr(644,root,root,755)
%doc template_inetd template_service
%attr(754,root,root) /etc/rc.d/init.d/rc-inetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd.conf
%dir /etc/sysconfig/rc-inetd
