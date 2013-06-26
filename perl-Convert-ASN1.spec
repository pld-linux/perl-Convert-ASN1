#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	ASN1
Summary:	Convert::ASN1 - ASN.1 encode/decode library
Summary(pl.UTF-8):	Convert::ASN1 - biblioteka kodująca/rozkodowująca ASN.1
Name:		perl-Convert-ASN1
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c846c8c1125e6a075444abe65d99b63
URL:		http://search.cpan.org/dist/Convert-ASN1/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.636
%if %{with tests}
BuildRequires:	perl-Math-BigInt >= 1.997
BuildRequires:	perl-Test-Simple >= 0.90
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	Convert::ASN1::Debug Convert::ASN1::IO Convert::ASN1::_decode Convert::ASN1::_encode

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Convert/ASN1.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Convert/ASN1/.packlist

%{?with_tests:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%dir %{perl_vendorlib}/Convert/ASN1
%{perl_vendorlib}/Convert/ASN1/*.pm
%{perl_vendorlib}/Convert/ASN1.pm
%{_mandir}/man3/Convert::ASN1*.3pm*
