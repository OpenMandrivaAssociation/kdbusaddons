%define major 4
%define libname %mklibname KF5DBusAddons %{major}
%define devname %mklibname KF5DBusAddons -d
%define debug_package %{nil}

Name: kdbusaddons
Version: 4.96.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 D-BUS Add-On library
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: qmake5
BuildRequires: ninja
Requires: %{libname} = %{EVRD}
Requires: %{apilibname} = %{EVRD}

%description
The KDE Frameworks 5 D-BUS Add-On library.

%package -n %{libname}
Summary: The KDE Frameworks 5 D-BUS Add-On library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 D-BUS Add-On library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR=%{buildroot} ninja -C build install
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5/

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
