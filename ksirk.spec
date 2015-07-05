Name:		ksirk
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Computerized version of a well known strategy board game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksirk/
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	pkgconfig(qca2)

%description -n ksirk
KsirK is a computerized version of the well known strategic board game Risk.
The goal of the game is simply to conquer the world by attacking your neighbors
with your armies.

Features :
- Support for 1-6 human or computer (AI) players
- Multi-player gaming over a network
- You can easily create new skins with SVG graphics and the skin editor
- Hot New Stuff support. You can easily download and install new skins

%files
%{_kde_bindir}/ksirk*
%{_kde_applicationsdir}/ksirk*.desktop
%{_kde_datadir}/config.kcfg/ksirk*settings.kcfg
%{_kde_configdir}/ksirk.knsrc
%{_kde_appsdir}/ksirk*
%{_kde_iconsdir}/*/*/apps/ksirk.png
%{_kde_docdir}/*/*/ksirk
%{_kde_docdir}/*/*/ksirkskineditor

#------------------------------------------------------------------------------

%define iris_ksirk_major 2
%define libiris_ksirk %mklibname iris_ksirk %{iris_ksirk_major}

%package -n %{libiris_ksirk}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libiris_ksirk}
KDE 4 library.

%files -n %{libiris_ksirk}
%{_kde_libdir}/libiris_ksirk.so.%{iris_ksirk_major}*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# We don't need it for now
rm -f %{buildroot}%{_kde_libdir}/libiris_ksirk.so


%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

