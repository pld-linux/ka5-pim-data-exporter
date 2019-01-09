%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		pim-data-exporter
Summary:	pim-data-exporter
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8c4963ed326c37815f1c4c5754fc837a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= 18.12.0
BuildRequires:	ka5-kcontacts-devel >= 18.12.0
BuildRequires:	ka5-kidentitymanagement-devel >= 18.12.0
BuildRequires:	ka5-kmailtransport-devel >= 18.12.0
BuildRequires:	ka5-kmime-devel >= 18.12.0
BuildRequires:	ka5-kpimtextedit-devel >= 18.12.0
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	ka5-mailcommon-devel >= 18.12.0
BuildRequires:	ka5-pimcommon-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-karchive-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kitemviews-devel >= 5.51.0
BuildRequires:	kf5-knotifications-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains utlities needed by KDE PIM to export data for
backup and archival.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/pimsettingexporter.categories
/etc/xdg/pimsettingexporter.renamecategories
%attr(755,root,root) %{_bindir}/pimsettingexporter
%attr(755,root,root) %{_bindir}/pimsettingexporterconsole
%attr(755,root,root) %ghost %{_libdir}/libpimsettingexporterprivate.so.5
%attr(755,root,root) %{_libdir}/libpimsettingexporterprivate.so.5.*.*
%{_desktopdir}/org.kde.pimsettingexporter.desktop
%{_datadir}/config.kcfg/pimsettingexporterglobalconfig.kcfg
%{_datadir}/kconf_update/pimsettingexporter-15.08-kickoff.sh
%{_datadir}/kconf_update/pimsettingexporter.upd
%{_datadir}/metainfo/org.kde.pimsettingexporter.appdata.xml
