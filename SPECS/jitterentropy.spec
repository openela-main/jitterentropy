%global libjit_soversion 3
Name:           jitterentropy
Version:        3.6.0
Release:        2%{?dist}
Summary:        Library implementing the jitter entropy source

License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://github.com/smuellerDD/jitterentropy-library
Source0:        %{url}/archive/v%{version}/%{name}-library-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

# Disable Upstream Makefiles debuginfo strip on install
Patch0: jitterentropy-rh-makefile.patch

%description
Library implementing the CPU jitter entropy source

%package devel
Summary: Development headers for jitterentropy library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for jitterentropy

%prep
%autosetup -p0 -n %{name}-library-%{version}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}/usr/include/
%make_install PREFIX=/usr LIBDIR=%{_lib}

%files
%doc README.md CHANGES.md
%license LICENSE LICENSE.bsd LICENSE.gplv2
%{_libdir}/libjitterentropy.so.%{libjit_soversion}*

%files devel
%{_includedir}/*
%{_libdir}/libjitterentropy.so
%{_mandir}/man3/*

%changelog
* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 3.6.0-2
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Fri Oct 25 2024 Vladis Dronov <vdronov@redhat.com> - 3.6.0-1
- Update to the upstream v3.6.0 @ 11829386 (RHEL-64946)

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 3.5.0-4
- Bump release for June 2024 mass rebuild

* Fri May 31 2024 Vladis Dronov <vdronov@redhat.com> - 3.5.0-3
- Update to the upstream v3.5.0 @ 48b2ffc1 (RHEL-30639)

* Mon Apr 01 2024 Vladis Dronov <vdronov@redhat.com> - 3.5.0-2
- Rebuild the package for RHEL-10

* Wed Feb 07 2024 Vladis Dronov <vdronov@redhat.com> - 3.5.0-1
- Update to the upstream v3.5.0 @ b178ef6b (RHEL-30639)
- Use proper SPDX license identifiers

* Fri Jan 26 2024 Vladis Dronov <vdronov@redhat.com> - 3.4.1-7
- Initial import from Fedora 40
