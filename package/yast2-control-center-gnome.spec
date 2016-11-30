#
# spec file for package yast2-control-center-gnome
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-control-center-gnome
Version:        3.1.11
Release:        0

Summary:        YaST2 - Control Center (GNOME version)
License:        GPL-2.0+
Group:          System/YaST

Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
Requires:       yast2-control-center
Requires:       yast2_theme
Supplements:    gnome-main-menu
Provides:       yast2-control-center-binary
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A nicely GNOME integrated YaST control center, with several new ease of
use features.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

lang=("af" "ar" "bg" "be" "bn" "bs" "ca" "cs" "cy" "da" "de" "el" "en_GB" "en_US" "eo" "es" "et" "fi" "fr" "gl" "gu" "he" "hi" "hr" "hu" "id" "it" "ja" "ka" "km" "ko" "lo" "lt" "mk" "mr" "nb" "nl" "pa" "pl" "pt" "ro" "ru" "si" "sk" "sl" "sr" "sr@Latn" "sv" "ta" "tr" "uk" "vi" "wa" "xh" "zh_CN" "zh_TW" "zu")

for i in %{buildroot}%{_datadir}/desktop-directories/*.directory; do
   %suse_update_desktop_file "$i"
done
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/YaST-gnome-merged

for i in ${lang[@]}; do
   file=po/$i.po
   mkdir -p %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES
   msgfmt -o %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/yast2-control-center-gnome.mo $file
done

%files
%defattr (-, root, root)
%doc COPYING README.md
%{_sysconfdir}/xdg/menus/*.menu
%{_sysconfdir}/xdg/menus/YaST-gnome-merged
%{_libexecdir}/YaST2/bin/y2controlcenter-gnome
%{_datadir}/desktop-directories/yast-gnome*.directory
%{_datadir}/yast2-control-center-gnome/
%{_datadir}/locale/

%changelog
