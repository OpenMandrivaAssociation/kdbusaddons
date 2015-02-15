%define major 5
%define libname %mklibname KF5DBusAddons %{major}
%define devname %mklibname KF5DBusAddons -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdbusaddons
Version: 5.7.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
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
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR=%{buildroot} ninja -C build install

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_bindir}/kquitapp5

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
