Name:           hestia-php
Version:        7.4.6
Release:        0
Summary:        Hestia internal PHP
Group:          System Environment/Base
URL:            https://www.hestiacp.com
License:        PHP and Zend and BSD and MIT and ASL 1.0 and NCSA
Vendor:         hestiacp.com
Requires:       redhat-release >= 7
Provides:       hestia-php = %{version}
BuildRequires:  systemd-rpm-macros

%description
This package contains internal PHP for Hestia Control Panel web interface.

%prep

%build

%install
cp -rfa %{sourcedir}/usr %{buildroot}

%clean

%pre

%post

%preun

%postun

%files
%defattr(-,root,root)
%attr(755,root,root) /usr/local/hestia/php
%config(noreplace) /usr/local/hestia/php/etc/php-fpm.conf
%config(noreplace) /usr/local/hestia/php/lib/php.ini

%changelog
* Thu Jun 25 2020 Ernesto Nicolás Carrea <equistango@gmail.com> - 7.4.6
- HestiaCP CentOS 8 support
