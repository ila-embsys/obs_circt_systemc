#
# spec file for package circt
#

%define sover_major   3
%define sover_minor   0
%define sover_patch   0

%define sover %{sover_major}_%{sover_minor}_%{sover_patch}
%define sover_dot %{sover_major}.%{sover_minor}.%{sover_patch}

Name:           systemc
Version:        0
Release:        0
Summary:        The language for System-level design, modeling and verification
License:        Apache-2.0
Url:            https://github.com/accellera-official/systemc
Source:         %{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  fdupes

%description
SystemC is an HDL (High Definition Language) based on a C++ class library
intended for simulations using standard C++ tools.
This library also includes TLM (Transaction Level Modeling) code.

%package -n lib%{name}%{sover}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n lib%{name}%{sover}
Shared libraries for SystemC

%package devel
Summary:        Development files for SystemC library
Requires:       lib%{name}%{sover} = %{version}

%description devel
This package contains the header files for the
SystemC library.

%package doc
Summary:        Doc files for SystemC library

%description doc
This package contains the Doc files for the
SystemC library.

%prep
%setup -q
echo "https://github.com/accellera-official/systemc/issues/105" > docs/DEVELOPMENT.md
autoupdate

%build
./config/bootstrap
%configure --with-unix-layout
%make_build

%install
%make_install

%fdupes %{buildroot}/%{_datadir}/doc/%{name}/examples

%check
make %{?_smp_mflags} check

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE

# TODO: Make the version scheme correct
%{_libdir}/lib%{name}-%{sover_dot}.so

%files devel
%license LICENSE
%doc AUTHORS.md

%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_includedir}/sysc

%{_includedir}/tlm
%{_includedir}/tlm.h

%dir %{_includedir}/tlm_core
%{_includedir}/tlm_core/*

%dir %{_includedir}/tlm_utils
%{_includedir}/tlm_utils/*

%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/tlm.pc

%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.la

%files doc
%{_datadir}/doc/%{name}

%changelog
