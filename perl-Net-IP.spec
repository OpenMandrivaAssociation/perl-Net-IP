%define upstream_name	 Net-IP
%define upstream_version 1.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension for manipulating IPv4/IPv6 addresses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides functions to deal with IPv4/IPv6 addresses.
The module can be used as a class, allowing the user to instantiate
IP objects, which can be single IP addresses, prefixes, or ranges of
addresses. There is also a procedural way of accessing most of the
functions. Most subroutines can take either IPv4 or IPv6 addresses
transparently.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/*
%{perl_vendorlib}/Net
%{_mandir}/*/*
