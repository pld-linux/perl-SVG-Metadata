#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	SVG
%define		pnam	Metadata
Summary:	SVG::Metadata - Perl module to capture metadata info about an SVG file
Summary(pl.UTF-8):	SVG::Metadata - moduł Perla do wydobywania informacji na temat pliku SVG
Name:		perl-%{pdir}-%{pnam}
Version:	0.28
Release:	2
# same as perl
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1100e73fd31a8ea2fc6402ad198c678f
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

%description -l pl.UTF-8
Ten moduł dostarcza metodę do wydobywania, przeglądania i używania
metadanych RDF osadzonych w pliku SVG.

Sama specyfikacja SVG nie dostarcza żadnych konkretnych mechanizmów do
obsługi metadanych, ale polega na osadzonych sekcjach RDF z własnymi
przestrzeniami nazw, zgodnie z filozofią XML. Niestety wiele narzędzi
do SVG nie obsługuje idei metadanych RDF; w rzeczywistości wiele w
ogóle nie obsługuje idei osadzania "wysp" XML. Niektóre nawet ignorują
i porzucają całość danych RDF.

Motywacja dla tego modułu jest dwojaka. Po pierwsze, dostarcza
mechanizm do dostępu do metadanych z plików SVG. Po drugie, dostarcza
środki do sprawdzania poprawności plików SVG w celu wykrycia, czy mają
metadane.

Ten skrypt był tworzony głównie z myślą o bibliotee Open Clip Art
(http://www.openclipart.org/), jako sposób filtrowania z oficjalnych
dystrybucji nadesłanych prac nie mających metadanych. Drugim
przeznaczeniem było wykorzystanie jako narzędzie testowe dla edytorów
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
