#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	nPth - New GNU Portable Threads Library
Summary(pl.UTF-8):	nPth - nowa przenośna biblioteka wątków GNU
Name:		npth
Version:	1.1
Release:	1
License:	LGPL v3+ or GPL v2+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/npth/%{name}-%{version}.tar.bz2
# Source0-md5:	aaffc8ef3e955ab50a1905809f268a23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nPth is the New GNU Portable Threads Library. This is a library to
provide the GNU Pth API and thus a non-preemptive threads
implementation.

In contrast to GNU Pth it is based on the system's standard threads
implementation. This allows the use of libraries which are not
compatible to GNU Pth. Experience with a Windows Pth emulation showed
that this is a solid way to provide a co-routine based framework.

%description -l pl.UTF-8
nPth (New GNU Portable Threads Library) to nowa przenośna biblioteka
wątków GNU. Jej celem jest dostarczenie API GNU Pth, a tym samym
implementacji niewywłaszczalnych wątków.

W przeciwieństwie do GNU Pth jest oparta na standardowej systemowej
implementacji wątków. Pozwala to na używanie bibliotek
niekompatybilnych z GNU Pth (doświadczenia z emulacją Pth na Windows
pokazały, że to jest solidna metoda zapewnienia szkieletu opartego na
korutynach).

%package devel
Summary:	Header files for nPth library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki nPth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nPth library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki nPth.

%package static
Summary:	Static nPth library
Summary(pl.UTF-8):	Statyczna biblioteka nPth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nPth library.

%description static -l pl.UTF-8
Statyczna biblioteka nPth.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libnpth.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnpth.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/npth-config
%attr(755,root,root) %{_libdir}/libnpth.so
%{_libdir}/libnpth.la
%{_includedir}/npth.h
%{_aclocaldir}/npth.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnpth.a
%endif
