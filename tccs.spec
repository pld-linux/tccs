Summary:	Show tc statistics in a nicer way
Summary(pl.UTF-8):	Analizator statystyk klas tc
Name:		tccs
Version:	0.1
Release:	1
License:	GPL
Group:		Networking
Source0:	tccs
Source1:	tccg
URL:		http://tccs.sourceforge.net/
BuildArch:	noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Show tc statistics in a nicer way. There is also tc-viewer with
different approach.

%description -l pl.UTF-8
Analizator statystyk klas tc, przedstawiający je w czytelnej formie.
Nieco inne podejście zastosowano w projekcie tc-viewer.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
