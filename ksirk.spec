#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		ksirk
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Summary:	Computerized version of a well known strategy board game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/ksirk/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/ksirk/-/archive/%{gitbranch}/ksirk-%{gitbranchd}.tar.bz2#/ksirk-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ksirk-%{version}.tar.xz
%endif
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:	cmake(KDEGames6)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(zlib)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:  qt6-qtmultimedia-gstreamer

%define libiris_ksirk %mklibname iris_ksirk 2
Obsoletes:	%{libiris_ksirk} < %{EVRD}

%rename plasma6-ksirk

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KsirK is a computerized version of the well known strategic board game Risk.
The goal of the game is simply to conquer the world by attacking your neighbors
with your armies.
Features:
- Support for 1-6 human or computer (AI) players
- Multi-player gaming over a network
- You can easily create new skins with SVG graphics and the skin editor
- Hot New Stuff support. You can easily download and install new skins

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/ksirk.renamecategories
%{_datadir}/qlogging-categories6/ksirk.categories
%{_bindir}/ksirk*
%{_datadir}/applications/org.kde.ksirk*.desktop
%{_datadir}/metainfo/org.kde.ksirk.appdata.xml
%{_datadir}/config.kcfg/ksirk*settings.kcfg
%{_datadir}/ksirk
%{_datadir}/ksirkskineditor
%{_iconsdir}/*/*/apps/ksirk.*
%{_datadir}/knsrcfiles/ksirk.knsrc
