#
# spec file for package 
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           fontconfig-infinality
Version:        20130104
Release:        1
License:        GPL-2.0+
Summary:        A fontconfig configuration to use with Infinality FreeType patches
Url:            http://www.infinality.net/
Group:          System/X11/Fonts
Source:         %{name}.tar.bz2
BuildArch:      noarch
Requires:       fontconfig
BuildRequires:  fontconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A configurable fontconfig configuration meant to be used in conjunction
with Freetype patches from http://www.infinality.net.
It should drop cleanly into most existing fontconfig setups. While this
package will work without infinality patches, much of it is tailored to
rendering when using those patches, and may not look correct otherwise.

%prep
%setup -q -n %{name}

# Add shebang
sed -i -e '1i#!/bin/bash' infinality/conf.src/generate60/generate60.sh

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/{fonts,profile.d}
mkdir -p %{buildroot}%{_datadir}/doc/%{name}-%{version}-%{release}

cp -R * %{buildroot}%{_sysconfdir}/fonts/

pushd %{buildroot}/etc/fonts/
tar jcf %{buildroot}/usr/share/doc/%{name}-%{version}-%{release}/fontconfig-infinality-%{version}-%{release}.tar.bz2 \
    conf.d conf.avail infinality
popd

#pushd %{buildroot}/etc/fonts/conf.d
#	ln -s  %{_datadir}/fontconfig/conf.avail/10-hinting-full.conf
#popd

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/fonts
%dir %{_sysconfdir}/fonts/conf.avail
%dir %{_sysconfdir}/fonts/conf.d
%dir %{_datadir}/doc/%{name}-%{version}-%{release}
%config %{_sysconfdir}/fonts/infinality
%{_sysconfdir}/fonts/conf.avail/52-infinality.conf
%{_sysconfdir}/fonts/conf.d/52-infinality.conf
#%{_sysconfdir}/fonts/conf.d/10-hinting-full.conf
%{_datadir}/doc/%{name}-%{version}-%{release}/

%changelog

