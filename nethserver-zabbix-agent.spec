Summary: nethserver-zabbix-agent integrates the monitoring agent
%define name nethserver-zabbix-agent
Name: %{name}
%define version 0.0.1
%define release 3
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
#Requires: zabbix-web-pgsql-scl
Requires: zabbix-agent < 6.0
Requires: zabbix-agent2 < 6.0
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
NethServer Zabbix agent configuration

%changelog


%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist

%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist
exit 0

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
