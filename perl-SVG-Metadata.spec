#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SVG
%define	pnam	Metadata
Summary:	SVG::Metadata - Perl module to capture metadata info about an SVG file
Summary(pl):	SVG::Metadata - modu³ Perla do wydobywania informacji na temat pliku SVG
Name:		perl-%{pdir}-%{pnam}
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce172adb1762ec1de485aa6ba1acfb1a
URL:		http://search.cpan.org/dist/SVG-Metadata/
BuildRequires:	perl-XML-Twig >= 3.15
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a way of extracting, browsing and using RDF
metadata embedded in an SVG file.

The SVG spec itself does not provide any particular mechanisms for
handling metadata, but instead relies on embedded, namespaced RDF
sections, as per XML philosophy. Unfortunately, many SVG tools don't
support the concept of RDF metadata; indeed many don't support the
idea of embedded XML "islands" at all. Some will even ignore and drop
the RDF data entirely when encountered.

The motivation for this module is twofold. First, it provides a
mechanism for accessing this metadata from the SVG files. Second, it
provides a means of validating SVG files to detect if they have the
metadata.

The motivation for this script is primarily for the Open Clip Art
Library (http://www.openclipart.org/), as a way of filtering out
submissions that lack metadata from being included in the official
distributions. A secondary motivation is to serve as a testing tool
for SVG editors like Inkscape (http://www.inkscape.org/).

%description -l pl
Ten modu³ dostarcza metodê do wydobywania, przegl±dania i u¿ywania
metadanych RDF osadzonych w pliku SVG.

Sama specyfikacja SVG nie dostarcza ¿adnych konkretnych mechanizmów do
obs³ugi metadanych, ale polega na osadzonych sekcjach RDF z w³asnymi
przestrzeniami nazw, zgodnie z filozofi± XML. Niestety wiele narzêdzi
do SVG nie obs³uguje idei metadanych RDF; w rzeczywisto¶ci wiele w
ogóle nie obs³uguje idei osadzania "wysp" XML. Niektóre nawet ignoruj±
i porzucaj± ca³o¶æ danych RDF.

Motywacja dla tego modu³u jest dwojaka. Po pierwsze, dostarcza
mechanizm do dostêpu do metadanych z plików SVG. Po drugie, dostarcza
¶rodki do sprawdzania poprawno¶ci plików SVG w celu wykrycia, czy maj±
metadane.

Ten skrypt by³ tworzony g³ównie z my¶l± o bibliotee Open Clip Art
(http://www.openclipart.org/), jako sposób filtrowania z oficjalnych
dystrybucji nades³anych prac nie maj±cych metadanych. Drugim
przeznaczeniem by³o wykorzystanie jako narzêdzie testowe dla edytorów
SVG takich jak Inkscape (http://www.inkscape.org/).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

# Note: tests do not pass (no .t files in t/ directory)
#%%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/SVG/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
