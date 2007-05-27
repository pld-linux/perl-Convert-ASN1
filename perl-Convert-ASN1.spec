%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	ASN1
Summary:	Convert::ASN1 - ASN.1 encode/decode library
Summary(pl.UTF-8):	Convert::ASN1 - biblioteka kodująca/rozkodowująca ASN.1
Name:		perl-Convert-ASN1
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f5c45724db1b09911e489275d19d0f5
URL:		http://search.cpan.org/dist/Convert-ASN1/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq 'perl(Convert::ASN1::Debug)' 'perl(Convert::ASN1::IO)' 'perl(Convert::ASN1::_decode)' 'perl(Convert::ASN1::_encode)'

%description
I consider Convert::ASN1 a replacement for my earlier Convert::BER
module. While ASN1.pm is not as flexable as BER.pm, because PDUs must
be described up front, it is also more powerful. For example an LDAP
filter is a recursive structure, BER.pm cannot encode or decode this
in a single pass, ASN1.pm can.

Convert::ASN1 will parse ASN.1 descriptions and will encode from and
decode to perl data structures using a hierarchy of references.

%description -l pl.UTF-8
Convert::ASN1 ma być zamiennikiem wcześniejszego Convert::BER tego
samego autora. ASN1.pm nie jest tak elastyczny jak BER.pm, ponieważ
PDU muszą być opisane, jest bardziej użyteczny. Na przykład filtr LDAP
jest strukturą rekurencyjną, BER.pm nie może kodować ani dekodować
takiej w jednym przebiegu, ASN1.pm może.

Convert::ASN1 parsuje opisy ASN.1 i koduje/dekoduje do perlowych
struktur danych używając hierarchii referencji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Convert/ASN1/.packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Convert/ASN1.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{perl_vendorlib}/Convert/ASN1
%{perl_vendorlib}/Convert/ASN1/*.pm
%{perl_vendorlib}/Convert/ASN1.pm
%{_mandir}/man3/*
