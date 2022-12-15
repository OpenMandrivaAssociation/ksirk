%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		ksirk
Version:	22.12.0
Release:	1
Epoch:		1
Summary:	Computerized version of a well known strategy board game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksirk/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	pkgconfig(qca2-qt5)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(zlib)

%define libiris_ksirk %mklibname iris_ksirk 2
Obsoletes:	%{libiris_ksirk} < %{EVRD}


%description -n ksirk
KsirK is a computerized version of the well known strategic board game Risk.
The goal of the game is simply to conquer the world by attacking your neighbors
with your armies.
Features:
- Support for 1-6 human or computer (AI) players
- Multi-player gaming over a network
- You can easily create new skins with SVG graphics and the skin editor
- Hot New Stuff support. You can easily download and install new skins

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/ksirk.categories
%{_bindir}/ksirk*
%{_datadir}/applications/org.kde.ksirk*.desktop
%{_datadir}/metainfo/org.kde.ksirk.appdata.xml
%{_datadir}/config.kcfg/ksirk*settings.kcfg
%{_datadir}/ksirk
%{_datadir}/ksirkskineditor
%{_iconsdir}/*/*/apps/ksirk.*
%{_datadir}/kxmlgui5/ksirk
%{_datadir}/kxmlgui5/ksirkskineditor
%{_datadir}/knsrcfiles/ksirk.knsrc
# No separate libpackage for a private
# library that can't be used by anything else
%{_libdir}/libiris_ksirk.so*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5 
%ninja

%install
%ninja_install -C build

# We don't need it for now
rm -f %{buildroot}%{_libdir}/libiris_ksirk.so

%find_lang %{name} --all-name --with-html
