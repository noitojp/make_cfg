%global _insdir /usr/local/share/make_cfg

BuildArch: noarch
Name: make_cfg
Version: 0.1.0
Release: 1
Summary: make file template for c or c++.
Group: Development/Libraries
License: BSD
Packager: noito@gmail.com

%description
make file template for c or c++.

%prep
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_insdir}
install -m 644 make.defs ${RPM_BUILD_ROOT}%{_insdir}/
install -m 644 make.rules ${RPM_BUILD_ROOT}%{_insdir}/
install -m 644 Makefile.tmpl ${RPM_BUILD_ROOT}%{_insdir}/

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%{_insdir}/make.defs
%{_insdir}/make.rules
%{_insdir}/Makefile.tmpl

%changelog

