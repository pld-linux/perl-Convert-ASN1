%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	ASN1
%define		_noautoreq "perl(Convert::ASN1::Debug)" "perl(Convert::ASN1::IO)" "perl(Convert::ASN1::_decode)" "perl(Convert::ASN1::_encode)"
Summary:	Convert::ASN1 perl module
Summary(pl):	Modu³ perla Convert::ASN1
Name:		perl-Convert-ASN1
Version:	0.17
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5e76be5dfb90d8c8fdb8c28b2f9a427
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I consider Convert::ASN1 a replacement for my earlier Convert::BER
module. While ASN1.pm is not as flexable as BER.pm, because PDUs must
be described up fronta, it is also more powerful. For example an LDAP
filter is a recursive structure, BER.pm cannot encode or decode this
in a single pass, ASN1.pm can.

Convert::ASN1 will parse ASN.1 descriptions and will encode from and
decode to perl data structures using a hierarchy of references.

%description -l pl
Convert::ASN1 ma byæ zamiennikiem wcze¶niejszego Convert::BER tego
samego autora. ASN1.pm nie jest tak elastyczny jak BER.pm, poniewa¿
PDU musz± byæ opisane, jest bardziej u¿yteczny. Na przyk³ad filtr LDAP
jest struktur± rekurencyjn±, BER.pm nie mo¿e kodowaæ ani dekodowaæ
takiej w jednym przebiegu, ASN1.pm mo¿e.

Convert::ASN1 parsuje opisy ASN.1 i koduje/dekoduje do perlowych
struktur danych u¿ywaj±c hierarchii referencji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{perl_vendorlib}/Convert/ASN1
%{perl_vendorlib}/Convert/ASN1/*.pm
%{perl_vendorlib}/Convert/ASN1.pm
%{_mandir}/man3/*
