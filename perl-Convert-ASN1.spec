%define		_noautoreq "perl(Convert::ASN1::Debug)" "perl(Convert::ASN1::IO)" "perl(Convert::ASN1::_decode)" "perl(Convert::ASN1::_encode)"
%include	/usr/lib/rpm/macros.perl
Summary:	Convert-ASN1 perl module
Summary(pl):	Modu³ perla Convert-ASN1
Name:		perl-Convert-ASN1
Version:	0.10
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-ASN1-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I consider Convert::ASN1 a replacement for my earlier Convert::BER
module. While ASN1.pm is not as flexable as BER.pm, because PDUs must
be described up fronta, it is also more powerful.  For example an LDAP
filter is a recursive structure, BER.pm cannot encode or decode this in
a single pass, ASN1.pm can.

Convert::ASN1 will parse ASN.1 descriptions and will encode from and
decode to perl data structures using a hierarchy of references.

%prep
%setup -q -n Convert-ASN1-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz htdocs/Convert/*.html
%dir %{perl_sitelib}/Convert/ASN1
%{perl_sitelib}/Convert/ASN1/*.pm
%{perl_sitelib}/Convert/ASN1.pm
%{_mandir}/man3/*
