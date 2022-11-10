Name: libXrender
Summary: X.Org X11 libXrender runtime library
Version: 0.9.11
Release: 1
License: MIT
URL: http://www.x.org
Source0: %{name}-%{version}.tar.zst
BuildRequires: libtool
BuildRequires: pkgconfig(x11) >= 1.6
BuildRequires: pkgconfig(xorg-macros) >= 1.8

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%reconfigure
%make_build

%install
%make_install
rm %{buildroot}%{_docdir}/libXrender/libXrender.txt

%files
%{_libdir}/libXrender.so.*

%files devel
%{_includedir}/X11/extensions/Xrender.h
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
