#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unicode
%define		pnam	Stringprep
Summary:	Preparation of Internationalized Strings (RFC 3454)
Summary(pl.UTF-8):	Tworzenie umiędzynarodowionych łańcuchów znaków (RFC 3454)
Name:		perl-Unicode-Stringprep
Version:	1.104
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd19b39c9d3dd7caf6db4b2bf3464a72
URL:		http://search.cpan.org/dist/Unicode-Stringprep/
BuildRequires:	perl-devel >= 1:5.8.3
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Unicode-Normalize >= 1
%endif
Requires:	perl-Unicode-Normalize >= 1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the stringprep framework for preparing Unicode
text strings in order to increase the likelihood that string input and
string comparison work in ways that make sense for typical users
throughout the world. The stringprep protocol is useful for protocol
identifier values, company and personal names, internationalized
domain names, and other text strings.

%description -l pl.UTF-8
Ten moduł implementuje szkielet stringprep do przygotowywania
unikodowych łańcuchów znaków tak, aby zwiększyć prawdopodobieństwo, że
wejście i porównywanie łańcuchów działa w sposób sensowny dla typowych
użytkowników na świecie. Protokół stringprep jest przydatny dla
wartości identyfikujących protokół, nazw firm i osób, międzynarodowych
domen i innych łańcuchów tekstowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Unicode/Stringprep.pm
%{perl_vendorlib}/Unicode/Stringprep
%{_mandir}/man3/Unicode::Stringprep*.3pm*
