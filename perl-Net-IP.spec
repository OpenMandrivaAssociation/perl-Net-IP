%define upstream_name	 Net-IP
%define upstream_version 1.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    6

Summary:	Perl extension for manipulating IPv4/IPv6 addresses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-4mdv2012.0
+ Revision: 765529
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-3
+ Revision: 764053
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-2
+ Revision: 667273
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2011.0
+ Revision: 407812
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.25-4mdv2009.0
+ Revision: 223856
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.25-3mdv2008.1
+ Revision: 180507
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 10:04:09 (53848)
- commit

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 10:02:36 (53847)
Import perl-Net-IP

* Thu Jun 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2007.0
- New release 1.25

* Mon May 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2007.0
- 1.25
- spec cleanup
- rpmbuildupdate aware

* Fri Oct 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.24-1mdk
- 1.24
- spec cleanup

* Fri Jun 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.23-1mdk
- 1.23
- spec cleanup

* Thu Jun 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.22-1mdk
- 1.22

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.21-1mdk
- 1.21-1
- rebuild for new perl

* Sat Aug 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.20-2mdk
- rebuild for perl

* Mon Mar 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.20-1mdk
- 1st mdk spec

