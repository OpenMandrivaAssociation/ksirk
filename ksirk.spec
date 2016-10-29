Name:		ksirk
Version:	16.08.2
Release:	1
Epoch:		1
Summary:	Computerized version of a well known strategy board game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksirk/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	cmake(KDEGames)
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
%{_bindir}/ksirk*                                                                                      
%{_datadir}/applications/kde4/ksirk*.desktop                                                           
%{_datadir}/config.kcfg/ksirk*settings.kcfg                                                            
%{_datadir}/config/ksirk.knsrc                                                                         
%{_datadir}/apps/ksirk*                                                                                
%{_iconsdir}/*/*/apps/ksirk.png                                                                        
%doc %{_docdir}/*/*/ksirk                                                                              
%doc %{_docdir}/*/*/ksirkskineditor

#------------------------------------------------------------------------------

%define iris_ksirk_major 2
%define libiris_ksirk %mklibname iris_ksirk %{iris_ksirk_major}

%package -n %{libiris_ksirk}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libiris_ksirk}
KDE 4 library.

%files -n %{libiris_ksirk}
%{_libdir}/libiris_ksirk.so.%{iris_ksirk_major}*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

# We don't need it for now
rm -f %{buildroot}%{_libdir}/libiris_ksirk.so

