Summary: A gtk2 frontend for rdesktop
Name: grdesktop
Version: 0.23
Release: %mkrel 5
Group: Networking/Remote access
License: GPL
Source0: %{name}-%{version}.tar.bz2
Patch: grdesktop-0.23-desktopentry.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.nongnu.org/grdesktop/
Requires: rdesktop
BuildRequires: libgnomeui2-devel
BuildRequires: scrollkeeper
BuildRequires: ImageMagick

%description
grdesktop is a frontend, written in C using the GTK+ 2 toolkit, for
the remote desktop client (rdesktop).
It can save several connections (including their options), and browse
the network for available terminal servers.

%prep
%setup -q
%patch -p1

%build
%configure2_5x --with-keymap-path=%_datadir/rdesktop/keymaps
%make

%install
rm -rf %buildroot
%makeinstall_std
mv %buildroot%_datadir/locale/de/LC_MESSAGES/@GETTEXT_PACKAGE@.mo %buildroot%_datadir/locale/de/LC_MESSAGES/grdesktop.mo
mv %buildroot%_datadir/locale/es/LC_MESSAGES/@GETTEXT_PACKAGE@.mo %buildroot%_datadir/locale/es/LC_MESSAGES/grdesktop.mo
mv %buildroot%_datadir/locale/fr/LC_MESSAGES/@GETTEXT_PACKAGE@.mo %buildroot%_datadir/locale/fr/LC_MESSAGES/grdesktop.mo

%find_lang %name --with-gnome 
mkdir -p %buildroot{%_iconsdir,%_liconsdir,%_miconsdir}
ln -s %_datadir/pixmaps/%name/icon.png %buildroot%_liconsdir/%name.png
convert -scale 32x32 pixmaps/icon.png %buildroot%_iconsdir/%name.png
convert -scale 16x16 pixmaps/icon.png %buildroot%_miconsdir/%name.png


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_scrollkeeper
%post_install_gconf_schemas %name
%update_menus
%endif

%preun
%preun_uninstall_gconf_schemas %name

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%_sysconfdir/gconf/schemas/grdesktop.schemas
%{_bindir}/grdesktop
%{_mandir}/man1/grdesktop.1*
%_datadir/application-registry/grdesktop.applications
%_datadir/applications/grdesktop.desktop
%_datadir/mime-info/grdesktop.keys
%_datadir/mime-info/grdesktop.mime
%{_datadir}/pixmaps/grdesktop/
%dir %_datadir/omf/grdesktop
%_datadir/omf/grdesktop/%name-C.omf
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
