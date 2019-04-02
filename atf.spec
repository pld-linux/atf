Summary:	Automated Testing Framework
Name:		atf
Version:	0.20
Release:	3
License:	BSD
Group:		Development/Libraries
Source0:	https://github.com/jmmv/atf/releases/download/%{name}-%{version}/atf-%{version}.tar.gz
# Source0-md5:	dd27cf5c6299013dd84053ee1df37759
URL:		https://github.com/jmmv/atf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

%package tests
Summary:	Automated Testing Framework - Test suite
Group:		Development/Libraries
Requires:	libatf-c++-devel = %{version}-%{release}
Requires:	libatf-c-devel = %{version}-%{release}
Requires:	libatf-sh-devel = %{version}-%{release}

%description tests
This package installs the run-time tests for all the components of
ATF, which include tests for the C, C++ and POSIX shell libraries and
the run-time tools. Please see the README.Fedora file in the
documentation directory for further details on how to run the
installed tests.

%package -n libatf-c
Summary:	Automated Testing Framework - C bindings
Summary(pl.UTF-8):	Automated Testing Framework - dowiązania dla języka C
Group:		Development/Libraries

%description -n libatf-c
This package provides the run-time libraries to run tests that use the
ATF C bindings.

%package -n libatf-c-devel
Summary:	Header files for ATF C bindings
Group:		Development/Libraries
Requires:	libatf-c = %{version}-%{release}

%description -n libatf-c-devel
Header files for ATF C bindings.

%package -n libatf-c-static
Summary:	Static ATF C library
Group:		Development/Libraries
Requires:	libatf-c-devel = %{version}-%{release}

%description -n libatf-c-static
Static ATF C library.

%package -n libatf-c++
Summary:	Automated Testing Framework - C++ bindings
Summary(pl.UTF-8):	Automated Testing Framework - dowiązania dla języka C++
Group:		Development/Libraries

%description -n libatf-c++
This package provides the run-time libraries to run tests that use the
ATF C++ bindings.

%package -n libatf-c++-devel
Summary:	Header files for ATF C++ bindings
Group:		Development/Libraries
Requires:	libatf-c++ = %{version}-%{release}

%description -n libatf-c++-devel
Header files for ATF C++ bindings.

%package -n libatf-c++-static
Summary:	Static ATF C++ library
Group:		Development/Libraries
Requires:	libatf-c++-devel = %{version}-%{release}

%description -n libatf-c++-static
Static ATF C++ library.

%package -n libatf-sh
Summary:	Automated Testing Framework - PSOIX shell bindings
Group:		Development/Libraries

%description -n libatf-sh
This package provides the run-time libraries to run tests that use the
ATF POSIX shell bindings.

%package -n libatf-sh-devel
Summary:	Header files for ATF POSIX shell bindings
Group:		Development/Libraries
Requires:	libatf-sh = %{version}-%{release}

%description -n libatf-sh-devel
Header files for ATF POSIX shell bindings.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%files
#%defattr(644,root,root,755)

%files tests
%defattr(644,root,root,755)
%dir %{_libexecdir}/atf
%{_libexecdir}/atf/tests

%files -n libatf-c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatf-c.so.0
%attr(755,root,root) %{_libdir}/libatf-c.so.0.0.0
%{_mandir}/man1/atf-test-program.1*
%{_mandir}/man4/atf-test-case.4*

%files -n libatf-c-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatf-c.so
%{_libdir}/libatf-c.la
%{_includedir}/atf-c
%{_includedir}/atf-c.h
%{_aclocaldir}/atf-c.m4
%{_aclocaldir}/atf-common.m4
%{_pkgconfigdir}/atf-c.pc
%{_mandir}/man3/atf-c-api.3*

%files -n libatf-c-static
%defattr(644,root,root,755)
%{_libdir}/libatf-c.a

%files -n libatf-c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatf-c++.so.1
%attr(755,root,root) %{_libdir}/libatf-c++.so.1.0.0

%files -n libatf-c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatf-c++.so
%{_libdir}/libatf-c++.la
%{_includedir}/atf-c++
%{_includedir}/atf-c++.hpp
%{_aclocaldir}/atf-c++.m4
%{_pkgconfigdir}/atf-c++.pc
%{_mandir}/man3/atf-c++-api.3*

%files -n libatf-c++-static
%defattr(644,root,root,755)
%{_libdir}/libatf-c++.a

%files -n libatf-sh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atf-sh
%attr(755,root,root) %{_libexecdir}/atf-check
%{_mandir}/man1/atf-check.1*
%{_mandir}/man1/atf-sh.1*
%{_datadir}/atf

%files -n libatf-sh-devel
%defattr(644,root,root,755)
%{_aclocaldir}/atf-sh.m4
%{_pkgconfigdir}/atf-sh.pc
%{_mandir}/man3/atf-sh-api.3*
