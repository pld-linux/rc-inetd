Summary:	Wrapper for managing inet service using any kind of inet daemon
Summary(pl.UTF-8):	Skrypty do zarządzania usługami inet
Name:		rc-inetd
Version:	0.17
Release:	3
License:	GPL
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	7218ebe82d2755a8d5051bd9b3a1a221
Patch0:		egrep.patch
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	inetdaemon
Requires:	rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper for managing inet service using any kind inet daemon.

%description -l pl.UTF-8
Skrypty do zarządzania usługami inet przy użyciu dowolnego rodzaju
demona inet.

%prep
%setup -q
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd}
install rc-inetd $RPM_BUILD_ROOT/etc/rc.d/init.d
cp -a rc-inetd.conf $RPM_BUILD_ROOT/etc/sysconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add rc-inetd
%service rc-inetd restart

%preun
if [ "$1" = "0" ]; then
	%service rc-inetd stop
	/sbin/chkconfig --del rc-inetd
fi

%files
%defattr(644,root,root,755)
%doc template_inetd template_service
%attr(754,root,root) /etc/rc.d/init.d/rc-inetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd.conf
%dir /etc/sysconfig/rc-inetd
