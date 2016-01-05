# based on PLD Linux spec git://git.pld-linux.org/packages/nettle.git
Summary:  Low-level cryptographic library
Name:     nettle
Version:  2.7.1
Release:  1
Epoch:    1
License:  GPL v2+ (parts on LGPL v2.1+)
Group:    Libraries
Source0:  http://ftp.gnu.org/gnu/nettle/%{name}-%{version}.tar.gz
# Source0-md5:  003d5147911317931dd453520eb234a5
URL:      http://www.lysator.liu.se/~nisse/lsh/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  m4
%if 0
BuildRequires:  ghostscript
BuildRequires:  tetex-dvips
BuildRequires:  texinfo-texi2dvi
%endif
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nettle is a cryptographic library that is designed to fit easily in
more or less any context: In crypto toolkits for object-oriented
languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
or even in kernel space. Nettle does only one thing, the low-level
crypto stuff, providing simple but general interface to it. In
particular, Nettle doesn't do algorithm selection. It doesn't do
memory allocation. It doesn't do any I/O. All these is up to
application.

%package devel
Summary:  Header files for nettle library
Group:    Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for nettle library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
  --enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
  DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post  devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun  devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/nettle-hash
%attr(755,root,root) %{_bindir}/nettle-lfib-stream
%attr(755,root,root) %{_bindir}/pkcs1-conv
%attr(755,root,root) %{_bindir}/sexp-conv

%attr(755,root,root) %ghost %{_libdir}/libhogweed.so.?
%attr(755,root,root) %ghost %{_libdir}/libnettle.so.?
%attr(755,root,root) %{_libdir}/libhogweed.so.*.*
%attr(755,root,root) %{_libdir}/libnettle.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhogweed.so
%attr(755,root,root) %{_libdir}/libnettle.so
%{_includedir}/nettle
%{_infodir}/nettle.info*
%{_pkgconfigdir}/*.pc

