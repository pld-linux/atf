Summary:	Automated Testing Framework
Summary(pl.UTF-8):	Automated Testing Framework - zautomatyzowany szkielet testów
Name:		atf
Version:	0.23
Release:	1
License:	BSD
Group:		Development/Tools
#Source0Download: https://github.com/jmmv/atf/releases
Source0:	https://github.com/jmmv/atf/archive/%{name}-%{version}/atf-%{version}.tar.gz
# Source0-md5:	8c810a0a7b54d436defe1a5582ce5882
URL:		https://github.com/jmmv/atf/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.9
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Automated Testing Framework (ATF) is a collection of libraries to
implement test programs in a variety of languages. At the moment, ATF
offers C, C++ and POSIX shell bindings with which to implement tests.
These bindings all offer a similar set of functionality and any test
program written with them exposes a consistent user interface.

ATF-based test programs rely on a separate runtime engine to execute
them. The runtime engine is in charge of isolating the test programs
from the rest of the system to ensure that their results are
deterministic and that they cannot affect the running system. The
runtime engine is also responsible for gathering the results of all
tests and composing reports. The current runtime of choice is Kyua.

%description -l pl.UTF-8
Automated Testing Framework (ATF) to zbiór bibliotek implementujących
programy testowe w różnych językach. Obecnie ATF oferuje wiązania C,
C++ i powłoki POSIX-owej, z użyciem których są zaimplementowane testy.
Wszystkie te wiązania oferują podobny zbiór funkcjonalności, a dowolny
program testowy napisany z ich użyciem udostępniają spójny interfejs
użytkownika.

Programy testowe oparte na ATF polegają na osobnym silniku
uruchomieniowym do ich wykonywania. Silnik ten odpowiada za izolację
programów testowych od reszty systemu, aby zapewnić determinizm
wyników i brak ich wpływu na działający system. Silnik odpowiada także
za zbieranie wyników wszystkich testów i składanie raportów. Obecnie
wybranym silnikiem jest Kyua.

%package tests
Summary:	Automated Testing Framework - Test suite
Summary(pl.UTF-8):	Automated Testing Framework - zestaw testów
Group:		Development/Tools
Requires:	libatf-c++-devel = %{version}-%{release}
Requires:	libatf-c-devel = %{version}-%{release}
Requires:	libatf-sh-devel = %{version}-%{release}

%description tests
This package installs the run-time tests for all the components of
ATF, which include tests for the C, C++ and POSIX shell libraries and
the run-time tools.

%description tests -l pl.UTF-8
Ten pakiet instaluje testy uruchomieniowe wszystkich komponentów ATF,
w tym testy bibliotek C, C++, powłoki POSIX oraz narzędzi
uruchomieniowych. 

%package -n libatf-c
Summary:	Automated Testing Framework - C bindings
Summary(pl.UTF-8):	Automated Testing Framework - dowiązania dla języka C
Group:		Libraries

%description -n libatf-c
This package provides the run-time libraries to run tests that use the
ATF C bindings.

%description -n libatf-c -l pl.UTF-8
Ten pakiet zawiera biblioteki uruchomieniowe do uruchamiania testów
wykorzystujących wiązania C ATF.

%package -n libatf-c-devel
Summary:	Header files for ATF C bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań C ATF
Group:		Development/Libraries
Requires:	libatf-c = %{version}-%{release}

%description -n libatf-c-devel
Header files for ATF C bindings.

%description -n libatf-c-devel -l pl.UTF-8
Pliki nagłówkowe wiązań C ATF.

%package -n libatf-c-static
Summary:	Static ATF C library
Summary(pl.UTF-8):	Statyczna biblioteka C ATF
Group:		Development/Libraries
Requires:	libatf-c-devel = %{version}-%{release}

%description -n libatf-c-static
Static ATF C library.

%description -n libatf-c-static -l pl.UTF-8
Statyczna biblioteka C ATF.

%package -n libatf-c++
Summary:	Automated Testing Framework - C++ bindings
Summary(pl.UTF-8):	Automated Testing Framework - dowiązania dla języka C++
Group:		Libraries
Requires:	libatf-c = %{version}-%{release}

%description -n libatf-c++
This package provides the run-time libraries to run tests that use the
ATF C++ bindings.

%description -n libatf-c++ -l pl.UTF-8
Ten pakiet zawiera biblioteki uruchomieniowe do uruchamiania testów
wykorzystujących wiązania C++ ATF.

%package -n libatf-c++-devel
Summary:	Header files for ATF C++ bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań C++ ATF
Group:		Development/Libraries
Requires:	libatf-c++ = %{version}-%{release}
Requires:	libatf-c-devel = %{version}-%{release}
Requires:	libstdc++-devel >= 6:5

%description -n libatf-c++-devel
Header files for ATF C++ bindings.

%description -n libatf-c++-devel -l pl.UTF-8
Pliki nagłówkowe wiązań C++ ATF.

%package -n libatf-c++-static
Summary:	Static ATF C++ library
Summary(pl.UTF-8):	Statyczna biblioteka C++ ATF
Group:		Development/Libraries
Requires:	libatf-c++-devel = %{version}-%{release}

%description -n libatf-c++-static
Static ATF C++ library.

%description -n libatf-c++-static -l pl.UTF-8
Statyczna biblioteka C++ ATF.

%package -n libatf-sh
Summary:	Automated Testing Framework - PSOIX shell bindings
Summary(pl.UTF-8):	Automated Testing Framework - dowiązania dla powłoki POSIX
Group:		Libraries
Requires:	libatf-c = %{version}-%{release}
Requires:	libatf-c++ = %{version}-%{release}

%description -n libatf-sh
This package provides the run-time libraries to run tests that use the
ATF POSIX shell bindings.

%description -n libatf-sh -l pl.UTF-8
Ten pakiet zawiera biblioteki uruchomieniowe do uruchamiania testów
wykorzystujących wiązania ATF do powłoki POSIX.

%package -n libatf-sh-devel
Summary:	Development files for ATF POSIX shell bindings
Summary(pl.UTF-8):	Pliki programistyczne nagłówkowe wiązań ATF dla powłoki POSIX
Group:		Development/Libraries
Requires:	libatf-sh = %{version}-%{release}

%description -n libatf-sh-devel
Development files for ATF POSIX shell bindings.

%description -n libatf-sh-devel -l pl.UTF-8
Pliki programistyczne nagłówkowe wiązań ATF dla powłoki POSIX.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA= \
	testsdir=%{_libexecdir}/atf/tests \
	pkgtestsdir=%{_libexecdir}/atf/tests

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libatf-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libatf-c -p /sbin/ldconfig
%postun	-n libatf-c -p /sbin/ldconfig

%post	-n libatf-c++ -p /sbin/ldconfig
%postun	-n libatf-c++ -p /sbin/ldconfig

%files tests
%defattr(644,root,root,755)
%dir %{_libexecdir}/atf
%{_libexecdir}/atf/tests

%files -n libatf-c
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS.md README.md
%attr(755,root,root) %{_libdir}/libatf-c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatf-c.so.1
%{_mandir}/man1/atf-test-program.1*
%{_mandir}/man4/atf-test-case.4*

%files -n libatf-c-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatf-c.so
%{_includedir}/atf-c
%{_includedir}/atf-c.h
%{_aclocaldir}/atf-c.m4
%{_aclocaldir}/atf-common.m4
%{_pkgconfigdir}/atf-c.pc
%{_mandir}/man3/atf-c.3*
%{_mandir}/man7/atf.7*

%files -n libatf-c-static
%defattr(644,root,root,755)
%{_libdir}/libatf-c.a

%files -n libatf-c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatf-c++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatf-c++.so.2

%files -n libatf-c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatf-c++.so
%{_includedir}/atf-c++
%{_includedir}/atf-c++.hpp
%{_aclocaldir}/atf-c++.m4
%{_pkgconfigdir}/atf-c++.pc
%{_mandir}/man3/atf-c++.3*

%files -n libatf-c++-static
%defattr(644,root,root,755)
%{_libdir}/libatf-c++.a

%files -n libatf-sh
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS.md README.md
%attr(755,root,root) %{_bindir}/atf-sh
%attr(755,root,root) %{_libexecdir}/atf-check
%{_mandir}/man1/atf-check.1*
%{_mandir}/man1/atf-sh.1*
%{_datadir}/atf

%files -n libatf-sh-devel
%defattr(644,root,root,755)
%{_aclocaldir}/atf-sh.m4
%{_pkgconfigdir}/atf-sh.pc
%{_mandir}/man3/atf-sh.3*
