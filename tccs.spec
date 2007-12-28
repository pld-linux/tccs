Summary:	Show tc statistics in a nicer way
Name:		tccs
Version:	0.1
Release:	1
License:	GPL
Group:		Networking
Source0:	http://tccs.sourceforge.net/tccs
# Source0-md5:	1a52b887a5ea8a98f353247b837540f3
Source1:	http://tccs.sourceforge.net/tccg
# Source1-md5:	9150cc5227a8e7d3208464d77d60d82c
URL:		http://tccs.sourceforge.net/
BuildArch:	noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Show tc statistics in a nicer way.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
