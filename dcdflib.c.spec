Summary:	Library of C Routines for Cumulative Distribution Functions, Inverses etc.
Summary(pl):	Biblioteka funkcji C do dystrybuant, odwrotno¶ci i innych parametrów
Name:		dcdflib.c
Version:	1.1
Release:	2
# partially public domain, but ACM implementations are non-commercial
License:	non-commercial distribution and use
Group:		Libraries
Source0:	ftp://odin.mda.uth.tmc.edu/pub/source/%{name}-%{version}.tar.gz
# Source0-md5:	6e31235713c284b77809e10dd4c7c56b
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library of C Routines for Cumulative Distribution Functions, Inverses
and Other Parameters.

%description -l pl
Biblioteka funkcji C do dystrybuant, odwrotno¶ci i innych parametrów.

%package devel
Summary:	DCDFLIB.C header files
Summary(pl):	Pliki nag³ówkowe DCDFLIB.C
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
DCDFLIB.C header files.

%description devel -l pl
Pliki nag³ówkowe DCDFLIB.C.

%package static
Summary:	DCDFLIB.C static library
Summary(pl):	Biblioteka statyczna DCDFLIB.C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
DCDFLIB.C static library.

%description static -l pl
Biblioteka statyczna DCDFLIB.C.

%prep
%setup -q -n %{name}

%build
cd src
libtool --mode=compile %{__cc} %{rpmcflags} -c ipmpar.c
libtool --mode=compile %{__cc} %{rpmcflags} -c dcdflib.c
libtool --mode=link %{__cc} %{rpmldflags} -o libcdflib.la -rpath %{_libdir} \
	ipmpar.lo dcdflib.lo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cd src
libtool --mode=install install libcdflib.la $RPM_BUILD_ROOT%{_libdir}
install cdflib.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc HOWTOGET README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
