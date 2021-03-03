#define snapshot 20200627
#define beta beta1
%define major 6

%define libconcurrent %mklibname Qt%{major}Concurrent %{major}
%define devconcurrent %mklibname -d Qt%{major}Concurrent
%define libcore %mklibname Qt%{major}Core %{major}
%define devcore %mklibname -d Qt%{major}Core
%define libdbus %mklibname Qt%{major}DBus %{major}
%define devdbus %mklibname -d Qt%{major}DBus
%define devdevicediscoverysupport %mklibname -d Qt%{major}DeviceDiscoverySupport
%define libeglfsdeviceintegration %mklibname Qt%{major}EglFSDeviceIntegration %{major}
%define deveglfsdeviceintegration %mklibname -d Qt%{major}EglFSDeviceIntegration
%define libeglfskmssupport %mklibname Qt%{major}EglFsKmsSupport %{major}
%define deveglfskmssupport %mklibname -d Qt%{major}EglFsKmsSupport
%define devfbsupport %mklibname -d Qt%{major}FbSupport
%define libgui %mklibname Qt%{major}Gui %{major}
%define devgui %mklibname -d Qt%{major}Gui
%define devinputsupport %mklibname -d Qt%{major}InputSupport
%define devkmssupport %mklibname -d Qt%{major}KmsSupport
%define libnetwork %mklibname Qt%{major}Network %{major}
%define devnetwork %mklibname -d Qt%{major}Network
%define libopengl %mklibname Qt%{major}OpenGL %{major}
%define devopengl %mklibname -d Qt%{major}OpenGL
%define libopenglwidgets %mklibname Qt%{major}OpenGLWidgets %{major}
%define devopenglwidgets %mklibname -d Qt%{major}OpenGLWidgets
%define libprintsupport %mklibname Qt%{major}PrintSupport %{major}
%define devprintsupport %mklibname -d Qt%{major}PrintSupport
%define libsql %mklibname Qt%{major}Sql %{major}
%define devsql %mklibname -d Qt%{major}Sql
%define libtest %mklibname Qt%{major}Test %{major}
%define devtest %mklibname -d Qt%{major}Test
%define libwidgets %mklibname Qt%{major}Widgets %{major}
%define devwidgets %mklibname -d Qt%{major}Widgets
%define libxcbqpa %mklibname Qt%{major}XcbQpa %{major}
%define devxcbqpa %mklibname -d Qt%{major}XcbQpa
%define libxml %mklibname Qt%{major}Xml %{major}
%define devxml %mklibname -d Qt%{major}Xml

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtbase
Version:	6.0.2
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtbase-%{snapshot}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtbase-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Patch0:		qtbase-6.0-rc2-examples-compile.patch
Patch1:		qtbase-init-pluginpath.patch
Release:	%{?beta:0.%{beta}.}%{?snapshot:1.%{snapshot}.}1
Group:		System/Libraries
Summary:	Version %{major} of the Qt framework
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	perl
BuildRequires:	icu
BuildRequires:	pkgconfig(libzstd)
# Not really used, but referenced by the paranoid integrity
# check in cmake files
BuildRequires:	%{_lib}zstd-static-devel
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(xcb-atom)
BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(xcb-ewmh)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(odbc)
BuildRequires:	cmake(double-conversion)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpcre2-16)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	cups-devel
BuildRequires:	openvg-devel
BuildRequires:	pkgconfig(libbrotlidec)
BuildRequires:	pkgconfig(libbrotlienc)
BuildRequires:	pkgconfig(libsctp)
# For the QtSQL plugins
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libmariadb)
BuildRequires:	pkgconfig(libpq)
# For the theme only
BuildRequires:	pkgconfig(gtk+-3.0)
License:	LGPLv3/GPLv3/GPLv2

%description
Version %{major} of the Qt framework

%package -n %{libconcurrent}
Summary:	Qt %{major} Concurrent library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libconcurrent}
Qt %{major} Concurrent library

%files -n %{libconcurrent}
%{_libdir}/libQt%{major}Concurrent.so.*
%{_qtdir}/lib/libQt%{major}Concurrent.so.*

%package -n %{devconcurrent}
Summary:	Development files for the Qt %{major} Concurrent library
Group:		Development/KDE and Qt
Requires:	%{devcore} = %{EVRD}
Requires:	%{libconcurrent} = %{EVRD}

%description -n %{devconcurrent}
Development files for the Qt %{major} Concurrent library

%files -n %{devconcurrent}
%{_qtdir}/include/QtConcurrent
%{_qtdir}/lib/cmake/Qt%{major}Concurrent
%{_libdir}/cmake/Qt%{major}Concurrent
%{_libdir}/libQt%{major}Concurrent.so
%{_qtdir}/lib/libQt%{major}Concurrent.so
%{_qtdir}/lib/libQt%{major}Concurrent.prl
%{_qtdir}/modules/Concurrent.json

%package -n %{libcore}
Summary:	Qt %{major} Core library
Group:		System/Libraries

%description -n %{libcore}
Qt %{major} Core library

%files -n %{libcore}
%dir %{_qtdir}
%dir %{_qtdir}/lib
%{_qtdir}/lib/libQt%{major}Core.so.*
%{_libdir}/libQt%{major}Core.so.*

%package -n %{devcore}
Summary:	Development files for the Qt %{major} Core library
Group:		Development/KDE and Qt
Requires:	%{libcore} = %{EVRD}
Requires:	%{name}-tools = %{EVRD}
# cmake files still depend on qmake to read variables
Requires:	qmake-qt%{major} = %{EVRD}

%description -n %{devcore}
Development files for the Qt %{major} Core library

%files -n %{devcore}
%{_qtdir}/include/QtCore
%{_qtdir}/bin/qt-configure-module
%{_qtdir}/lib/cmake/Qt%{major}Core
%{_qtdir}/lib/cmake/Qt%{major}CoreTools
%{_qtdir}/lib/cmake/Qt%{major}Core_qobject
%{_qtdir}/lib/cmake/Qt%{major}HostInfo
%{_qtdir}/lib/libQt%{major}Core.prl
%{_qtdir}/lib/libQt%{major}Core.so
%{_qtdir}/lib/libQt%{major}Core_qobject.a
%{_qtdir}/lib/libQt%{major}Core_qobject.prl
%{_libdir}/libQt%{major}Core.so
%{_libdir}/libQt%{major}Core_qobject.a
%{_libdir}/cmake/Qt%{major}
%{_libdir}/cmake/Qt%{major}BuildInternals
%{_libdir}/cmake/Qt%{major}Core
%{_libdir}/cmake/Qt%{major}CoreTools
%{_libdir}/cmake/Qt%{major}Core_qobject
%{_libdir}/cmake/Qt%{major}HostInfo
%dir %{_qtdir}/modules
%{_qtdir}/modules/Core.json
%{_qtdir}/modules/Core_qobject.json
%{_qtdir}/bin/moc
%{_qtdir}/bin/rcc
%dir %{_qtdir}/lib/metatypes
%{_qtdir}/lib/metatypes/qt6core_qobject_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt6core_relwithdebinfo_metatypes.json

%package -n %{libdbus}
Summary:	Qt %{major} D-Bus library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libdbus}
Qt %{major} D-Bus library

%files -n %{libdbus}
%{_libdir}/libQt%{major}DBus.so.*
%{_qtdir}/lib/libQt%{major}DBus.so.*

%package -n %{devdbus}
Summary:	Development files for the Qt %{major} D-Bus library
Group:		Development/KDE and Qt
Requires:	%{libdbus} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devdbus}
Development files for the Qt %{major} D-Bus library

%files -n %{devdbus}
%{_qtdir}/include/QtDBus
%{_qtdir}/lib/cmake/Qt%{major}DBus
%{_qtdir}/lib/cmake/Qt%{major}DBusTools
%{_libdir}/cmake/Qt%{major}DBus
%{_libdir}/cmake/Qt%{major}DBusTools
%{_libdir}/libQt%{major}DBus.so
%{_qtdir}/lib/libQt%{major}DBus.so
%{_qtdir}/lib/libQt%{major}DBus.prl
%{_qtdir}/bin/qdbuscpp2xml
%{_qtdir}/bin/qdbusxml2cpp
%{_qtdir}/modules/DBus.json

%package -n %{libeglfsdeviceintegration}
Summary:	Qt %{major} EglFS device integration library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libeglfsdeviceintegration}
Qt %{major} EglFS device integration library

%files -n %{libeglfsdeviceintegration}
%{_libdir}/libQt%{major}EglFSDeviceIntegration.so.*
%{_qtdir}/lib/libQt%{major}EglFSDeviceIntegration.so.*

%package -n %{deveglfsdeviceintegration}
Summary:	Development files for the Qt %{major} EglFS device integration library
Group:		Development/KDE and Qt
Requires:	%{devcore} = %{EVRD}
Requires:	%{libeglfsdeviceintegration} = %{EVRD}

%description -n %{deveglfsdeviceintegration}
Development files for the Qt %{major} EglFS device integration library

%files -n %{deveglfsdeviceintegration}
%{_qtdir}/include/QtEglFSDeviceIntegration
%{_qtdir}/lib/cmake/Qt%{major}EglFSDeviceIntegration
%{_libdir}/cmake/Qt%{major}EglFSDeviceIntegration
%{_libdir}/libQt%{major}EglFSDeviceIntegration.so
%{_qtdir}/lib/libQt%{major}EglFSDeviceIntegration.so
%{_qtdir}/lib/libQt%{major}EglFSDeviceIntegration.prl
%{_qtdir}/modules/EglFSDeviceIntegration.json

%package -n %{devdevicediscoverysupport}
Summary:	Device discovery support library for Qt %{major}
Group:		Development/KDE and Qt
Requires:	%{devcore} = %{EVRD}

%description -n %{devdevicediscoverysupport}
Device discovery support library for Qt %{major}

%files -n %{devdevicediscoverysupport}
%{_qtdir}/include/QtDeviceDiscoverySupport
%{_qtdir}/lib/cmake/Qt%{major}DeviceDiscoverySupport
%{_libdir}/cmake/Qt%{major}DeviceDiscoverySupport
%{_libdir}/libQt%{major}DeviceDiscoverySupport.a
%{_qtdir}/lib/libQt%{major}DeviceDiscoverySupport.a
%{_qtdir}/lib/libQt%{major}DeviceDiscoverySupport.prl
%{_qtdir}/modules/DeviceDiscoverySupport.json

%package -n %{libeglfskmssupport}
Summary:	Qt %{major} EglFS KMS support library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libeglfskmssupport}
Qt %{major} EglFS KMS support library

%files -n %{libeglfskmssupport}
%{_libdir}/libQt%{major}EglFsKmsSupport.so.*
%{_qtdir}/lib/libQt%{major}EglFsKmsSupport.so.*
%{_libdir}/libQt%{major}EglFsKmsGbmSupport.so.*
%{_qtdir}/lib/libQt6EglFsKmsGbmSupport.so.*

%package -n %{deveglfskmssupport}
Summary:	Development files for the Qt %{major} KMS support library
Group:		Development/KDE and Qt
Requires:	%{devcore} = %{EVRD}
Requires:	%{libeglfskmssupport} = %{EVRD}

%description -n %{deveglfskmssupport}
Development files for the Qt %{major} EglFS KMS support library

%files -n %{deveglfskmssupport}
%{_qtdir}/lib/cmake/Qt%{major}EglFsKmsSupport
%{_libdir}/cmake/Qt%{major}EglFsKmsSupport
%{_libdir}/libQt%{major}EglFsKmsSupport.so
%{_qtdir}/lib/libQt%{major}EglFsKmsSupport.so
%{_qtdir}/lib/libQt%{major}EglFsKmsSupport.prl
%{_qtdir}/include/QtEglFsKmsSupport
%{_qtdir}/modules/EglFsKmsSupport.json
%{_libdir}/cmake/Qt%{major}EglFsKmsGbmSupport
%{_libdir}/libQt%{major}EglFsKmsGbmSupport.so
%{_qtdir}/include/QtEglFsKmsGbmSupport
%{_qtdir}/lib/cmake/Qt%{major}EglFsKmsGbmSupport
%{_qtdir}/lib/libQt%{major}EglFsKmsGbmSupport.prl
%{_qtdir}/lib/libQt%{major}EglFsKmsGbmSupport.so
%{_qtdir}/modules/EglFsKmsGbmSupport.json

%package -n %{devfbsupport}
Summary:	Framebuffer support library for Qt %{major}
Group:		Development/KDE and Qt
Requires:	%{devcore} = %{EVRD}

%description -n %{devfbsupport}
Framebuffer support library for Qt %{major}

%files -n %{devfbsupport}
%{_qtdir}/include/QtFbSupport
%{_qtdir}/lib/cmake/Qt%{major}FbSupport
%{_libdir}/cmake/Qt%{major}FbSupport
%{_libdir}/libQt%{major}FbSupport.a
%{_qtdir}/lib/libQt%{major}FbSupport.a
%{_qtdir}/lib/libQt%{major}FbSupport.prl
%{_qtdir}/modules/FbSupport.json

%package -n %{libgui}
Summary:	Qt %{major} GUI library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libgui}
Qt %{major} GUI library

%files -n %{libgui}
%{_libdir}/libQt%{major}Gui.so.*
%{_qtdir}/lib/libQt%{major}Gui.so.*
%dir %{_qtdir}/plugins/egldeviceintegrations
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-emu-integration.so
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-kms-egldevice-integration.so
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-kms-integration.so
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-x11-integration.so
%dir %{_qtdir}/plugins/generic
%{_qtdir}/plugins/generic/libqevdevkeyboardplugin.so
%{_qtdir}/plugins/generic/libqevdevmouseplugin.so
%{_qtdir}/plugins/generic/libqevdevtabletplugin.so
%{_qtdir}/plugins/generic/libqevdevtouchplugin.so
%{_qtdir}/plugins/generic/libqlibinputplugin.so
%{_qtdir}/plugins/generic/libqtuiotouchplugin.so
%dir %{_qtdir}/plugins/imageformats
%{_qtdir}/plugins/imageformats/libqgif.so
%{_qtdir}/plugins/imageformats/libqico.so
%{_qtdir}/plugins/imageformats/libqjpeg.so
%dir %{_qtdir}/plugins/platforminputcontexts
%{_qtdir}/plugins/platforminputcontexts/libcomposeplatforminputcontextplugin.so
%{_qtdir}/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so
%dir %{_qtdir}/plugins/platforms
%{_qtdir}/plugins/platforms/libqeglfs.so
%{_qtdir}/plugins/platforms/libqlinuxfb.so
%{_qtdir}/plugins/platforms/libqminimal.so
%{_qtdir}/plugins/platforms/libqminimalegl.so
%{_qtdir}/plugins/platforms/libqoffscreen.so
%{_qtdir}/plugins/platforms/libqvnc.so
%{_qtdir}/plugins/platforms/libqxcb.so
%dir %{_qtdir}/plugins/platformthemes
%{_qtdir}/plugins/platformthemes/libqgtk3.so
%{_qtdir}/plugins/platformthemes/libqxdgdesktopportal.so

%package -n %{devgui}
Summary:	Development files for the Qt %{major} GUI library
Group:		Development/KDE and Qt
Requires:	%{libgui} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devgui}
Development files for the Qt %{major} GUI library

%files -n %{devgui}
%{_qtdir}/include/QtGui
%{_qtdir}/lib/cmake/Qt%{major}Gui
%{_qtdir}/lib/cmake/Qt%{major}GuiTools
%{_libdir}/cmake/Qt%{major}Gui
%{_libdir}/cmake/Qt%{major}GuiTools
%{_libdir}/libQt%{major}Gui.so
%{_qtdir}/lib/libQt%{major}Gui.so
%{_qtdir}/lib/libQt%{major}Gui.prl
%{_qtdir}/modules/Gui.json
%{_qtdir}/lib/metatypes/qt6gui_relwithdebinfo_metatypes.json

%package -n %{devinputsupport}
Summary:	Input support library for Qt %{major}
Group:		Development/KDE and Qt
Requires:	%{devcore} = %{EVRD}

%description -n %{devinputsupport}
Input support library for Qt %{major}

%files -n %{devinputsupport}
%{_qtdir}/include/QtInputSupport
%{_qtdir}/lib/cmake/Qt%{major}InputSupport
%{_libdir}/cmake/Qt%{major}InputSupport
%{_libdir}/libQt%{major}InputSupport.a
%{_qtdir}/lib/libQt%{major}InputSupport.a
%{_qtdir}/lib/libQt%{major}InputSupport.prl
%{_qtdir}/modules/InputSupport.json

%package -n %{devkmssupport}
Summary:	KMS support library for Qt %{major}
Group:		Development/KDE and Qt
Requires:	%{devcore} = %{EVRD}

%description -n %{devkmssupport}
KMS support library for Qt %{major}

%files -n %{devkmssupport}
%{_qtdir}/include/QtKmsSupport
%{_qtdir}/lib/cmake/Qt%{major}KmsSupport
%{_libdir}/cmake/Qt%{major}KmsSupport
%{_libdir}/libQt%{major}KmsSupport.a
%{_qtdir}/lib/libQt%{major}KmsSupport.a
%{_qtdir}/lib/libQt%{major}KmsSupport.prl
%{_qtdir}/modules/KmsSupport.json

%package -n %{libnetwork}
Summary:	Qt %{major} Network library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libnetwork}
Qt %{major} Network library

%files -n %{libnetwork}
%{_libdir}/libQt%{major}Network.so.*
%{_qtdir}/lib/libQt%{major}Network.so.*

%package -n %{devnetwork}
Summary:	Development files for the Qt %{major} Network library
Group:		Development/KDE and Qt
Requires:	%{libnetwork} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devnetwork}
Development files for the Qt %{major} Network library

%files -n %{devnetwork}
%{_qtdir}/include/QtNetwork
%{_qtdir}/lib/cmake/Qt%{major}Network
%{_libdir}/cmake/Qt%{major}Network
%{_libdir}/libQt%{major}Network.so
%{_qtdir}/lib/libQt%{major}Network.so
%{_qtdir}/lib/libQt%{major}Network.prl
%{_qtdir}/modules/Network.json

%package -n %{libopengl}
Summary:	Qt %{major} OpenGL library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libopengl}
Qt %{major} OpenGL library

%files -n %{libopengl}
%{_libdir}/libQt%{major}OpenGL.so.*
%{_qtdir}/lib/libQt%{major}OpenGL.so.*

%package -n %{devopengl}
Summary:	Development files for the Qt %{major} OpenGL library
Group:		Development/KDE and Qt
Requires:	%{libopengl} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devopengl}
Development files for the Qt %{major} OpenGL library

%files -n %{devopengl}
%{_qtdir}/include/QtOpenGL
%{_qtdir}/lib/cmake/Qt%{major}OpenGL
%{_libdir}/cmake/Qt%{major}OpenGL
%{_libdir}/libQt%{major}OpenGL.so
%{_qtdir}/lib/libQt%{major}OpenGL.so
%{_qtdir}/lib/libQt%{major}OpenGL.prl
%{_qtdir}/modules/OpenGL.json

%package -n %{libopenglwidgets}
Summary:	Qt %{major} OpenGL Widgets library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libopenglwidgets}
Qt %{major} OpenGL Widgets library

%files -n %{libopenglwidgets}
%{_libdir}/libQt%{major}OpenGLWidgets.so.*
%{_qtdir}/lib/libQt%{major}OpenGLWidgets.so.*

%package -n %{devopenglwidgets}
Summary:	Development files for the Qt %{major} OpenGL Widgets library
Group:		Development/KDE and Qt
Requires:	%{libopenglwidgets} = %{EVRD}
Requires:	%{devcore} = %{EVRD}
Requires:	%{devopengl} = %{EVRD}

%description -n %{devopenglwidgets}
Development files for the Qt %{major} OpenGL Widgets library

%files -n %{devopenglwidgets}
%{_qtdir}/include/QtOpenGLWidgets
%{_qtdir}/lib/cmake/Qt%{major}OpenGLWidgets
%{_libdir}/cmake/Qt%{major}OpenGLWidgets
%{_libdir}/libQt%{major}OpenGLWidgets.so
%{_qtdir}/lib/libQt%{major}OpenGLWidgets.so
%{_qtdir}/lib/libQt%{major}OpenGLWidgets.prl
%{_qtdir}/modules/OpenGLWidgets.json

%package -n %{libprintsupport}
Summary:	Qt %{major} printing support library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libprintsupport}
Qt %{major} printing support library

%files -n %{libprintsupport}
%{_libdir}/libQt%{major}PrintSupport.so.*
%{_qtdir}/lib/libQt%{major}PrintSupport.so.*
%dir %{_qtdir}/plugins/printsupport
%{_qtdir}/plugins/printsupport/libcupsprintersupport.so

%package -n %{devprintsupport}
Summary:	Development files for the Qt %{major} printing support library
Group:		Development/KDE and Qt
Requires:	%{libprintsupport} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devprintsupport}
Development files for the Qt %{major} printing support library

%files -n %{devprintsupport}
%{_qtdir}/include/QtPrintSupport
%{_qtdir}/lib/cmake/Qt%{major}PrintSupport
%{_libdir}/cmake/Qt%{major}PrintSupport
%{_libdir}/libQt%{major}PrintSupport.so
%{_qtdir}/lib/libQt%{major}PrintSupport.so
%{_qtdir}/lib/libQt%{major}PrintSupport.prl
%{_qtdir}/modules/PrintSupport.json

%package -n %{libsql}
Summary:	Qt %{major} SQL library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libsql}
Qt %{major} SQL library

%files -n %{libsql}
%{_libdir}/libQt%{major}Sql.so.*
%{_qtdir}/lib/libQt%{major}Sql.so.*
%dir %{_qtdir}/plugins/sqldrivers
%{_qtdir}/plugins/sqldrivers/libqsqlite.so
%{_qtdir}/plugins/sqldrivers/libqsqlmysql.so
%{_qtdir}/plugins/sqldrivers/libqsqlodbc.so
%{_qtdir}/plugins/sqldrivers/libqsqlpsql.so

%package -n %{devsql}
Summary:	Development files for the Qt %{major} SQL library
Group:		Development/KDE and Qt
Requires:	%{libsql} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devsql}
Development files for the Qt %{major} SQL library

%files -n %{devsql}
%{_qtdir}/include/QtSql
%{_qtdir}/lib/cmake/Qt%{major}Sql
%{_libdir}/cmake/Qt%{major}Sql
%{_libdir}/libQt%{major}Sql.so
%{_qtdir}/lib/libQt%{major}Sql.so
%{_qtdir}/lib/libQt%{major}Sql.prl
%{_qtdir}/modules/Sql.json

%package -n %{libtest}
Summary:	Qt %{major} Test library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libtest}
Qt %{major} Test library

%files -n %{libtest}
%{_libdir}/libQt%{major}Test.so.*
%{_qtdir}/lib/libQt%{major}Test.so.*

%package -n %{devtest}
Summary:	Development files for the Qt %{major} Test library
Group:		Development/KDE and Qt
Requires:	%{libtest} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devtest}
Development files for the Qt %{major} Test library

%files -n %{devtest}
%{_qtdir}/include/QtTest
%{_qtdir}/lib/cmake/Qt%{major}Test
%{_libdir}/cmake/Qt%{major}Test
%{_libdir}/libQt%{major}Test.so
%{_qtdir}/lib/libQt%{major}Test.so
%{_qtdir}/lib/libQt%{major}Test.prl
%{_qtdir}/modules/Test.json

%package -n %{libwidgets}
Summary:	Qt %{major} Widgets library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libwidgets}
Qt %{major} Widgets library

%files -n %{libwidgets}
%{_libdir}/libQt%{major}Widgets.so.*
%{_qtdir}/lib/libQt%{major}Widgets.so.*

%package -n %{devwidgets}
Summary:	Development files for the Qt %{major} Widgets library
Group:		Development/KDE and Qt
Requires:	%{libwidgets} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devwidgets}
Development files for the Qt %{major} Widgets library

%files -n %{devwidgets}
%{_qtdir}/include/QtWidgets
%{_qtdir}/lib/cmake/Qt%{major}Widgets
%{_qtdir}/lib/cmake/Qt%{major}WidgetsTools
%{_libdir}/cmake/Qt%{major}Widgets
%{_libdir}/cmake/Qt%{major}WidgetsTools
%{_libdir}/libQt%{major}Widgets.so
%{_qtdir}/lib/libQt%{major}Widgets.so
%{_qtdir}/lib/libQt%{major}Widgets.prl
%{_qtdir}/bin/uic
%{_qtdir}/modules/Widgets.json
%{_qtdir}/lib/metatypes/qt6widgets_relwithdebinfo_metatypes.json

%package -n %{libxcbqpa}
Summary:	Qt %{major} XCB QPA Library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libxcbqpa}
Qt %{major} XCB QPA library

%files -n %{libxcbqpa}
%{_libdir}/libQt%{major}XcbQpa.so.*
%{_qtdir}/lib/libQt%{major}XcbQpa.so.*
%dir %{_qtdir}/plugins/xcbglintegrations
%{_qtdir}/plugins/xcbglintegrations/libqxcb-egl-integration.so
%{_qtdir}/plugins/xcbglintegrations/libqxcb-glx-integration.so

%package -n %{devxcbqpa}
Summary:	Development files for the Qt %{major} XCB QPA library
Group:		Development/KDE and Qt
Requires:	%{libxcbqpa} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devxcbqpa}
Development files for the Qt %{major} XCB QPA library

%files -n %{devxcbqpa}
%{_qtdir}/lib/cmake/Qt%{major}XcbQpa
%{_libdir}/cmake/Qt%{major}XcbQpa
%{_libdir}/libQt%{major}XcbQpa.so
%{_qtdir}/lib/libQt%{major}XcbQpa.so
%{_qtdir}/lib/libQt%{major}XcbQpa.prl
%{_qtdir}/modules/XcbQpa.json

%package -n %{libxml}
Summary:	Qt %{major} XML library
Group:		System/Libraries
Requires:	%{libcore} = %{EVRD}

%description -n %{libxml}
Qt %{major} XML library

%files -n %{libxml}
%{_libdir}/libQt%{major}Xml.so.*
%{_qtdir}/lib/libQt%{major}Xml.so.*

%package -n %{devxml}
Summary:	Development files for the Qt %{major} XML library
Group:		Development/KDE and Qt
Requires:	%{libxml} = %{EVRD}
Requires:	%{devcore} = %{EVRD}

%description -n %{devxml}
Development files for the Qt %{major} XML library

%files -n %{devxml}
%{_qtdir}/include/QtXml
%{_qtdir}/lib/cmake/Qt%{major}Xml
%{_libdir}/cmake/Qt%{major}Xml
%{_libdir}/libQt%{major}Xml.so
%{_qtdir}/lib/libQt%{major}Xml.so
%{_qtdir}/lib/libQt%{major}Xml.prl
%{_qtdir}/modules/Xml.json

%package doc
Summary: Documentation for the Qt %{major} framework
Group: Documentation

%description doc
Documentation for the Qt %{major} framework

%files doc
%{_qtdir}/doc

%package examples
Summary: Examples for the Qt %{major} framework
Group: Documentation

%description examples
Documentation for the Qt %{major} framework

%files examples
%{_qtdir}/examples

%package -n qmake-qt%{major}
Summary: The legacy qmake build tool for Qt %{major}
Group: Development/Tools

%description -n qmake-qt%{major}
The legacy qmake build tool for Qt %{major}

%files -n qmake-qt%{major}
%{_qtdir}/bin/qmake
%{_qtdir}/mkspecs
%{_qtdir}/bin/qt-internal-configure-tests

%package -n qt%{major}-cmake
Summary: Cmake extensions for Qt %{major}
Group: Development/KDE and Qt

%description -n qt%{major}-cmake
Cmake extensions for Qt %{major}

%files -n qt%{major}-cmake
%{_qtdir}/bin/qt-cmake
%{_qtdir}/bin/qt-cmake-private
%{_qtdir}/bin/qt-cmake-private-install.cmake
%{_qtdir}/bin/qt-cmake-standalone-test
%{_qtdir}/bin/cmake_automoc_parser
%{_qtdir}/lib/cmake/Qt%{major}
%{_qtdir}/lib/cmake/Qt%{major}BuildInternals
%dir %{_qtdir}/libexec
%{_qtdir}/libexec/android_emulator_launcher.sh
%{_qtdir}/libexec/ensure_pro_file.cmake

%package tools
Summary: Qt %{major} build tools
Group: Development/KDE and Qt

%description tools
Qt %{major} build tools

%files tools
%{_qtdir}/bin/androiddeployqt
%{_qtdir}/bin/androidtestrunner
%{_qtdir}/bin/qlalr
%{_qtdir}/bin/qvkgen
%{_qtdir}/bin/syncqt.pl
%{_qtdir}/bin/tracegen
%{_qtdir}/libexec/syncqt.pl
%{_libexecdir}/syncqt.pl

%prep
%autosetup -p1 -n qtbase%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}

sed -i -e 's,@QTDIR@,%{_qtdir},g' src/gui/kernel/qguiapplication.cpp

# FIXME This may be interesting in the future:
#	-DQT_FEATURE_cxx2a:BOOL=ON
# As of 6.0.0-rc2 and clang 11.0.1, causes a compile failure

# FIXME This may be interesting for some boards
#	-DQT_FEATURE_opengl_dynamic:BOOL=ON \
#	-DQT_FEATURE_opengles2:BOOL=ON
# But as of 6.0.0-rc2, it disables the even more useful X11 GLX plugin
# opengles2 disables it in cmake, the others cause bogus linkage

# FIXME Investigate
#	-DQT_FEATURE_lttng:BOOL=ON

%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DQT_FEATURE_aesni:BOOL=ON \
	-DQT_FEATURE_dynamicgl:BOOL=ON \
	-DQT_FEATURE_ipc_posix:BOOL=ON \
	-DQT_FEATURE_journald:BOOL=ON \
	-DQT_FEATURE_opengl_desktop:BOOL=ON \
	-DQT_FEATURE_opengles3:BOOL=ON \
	-DQT_FEATURE_opengles31:BOOL=ON \
	-DQT_FEATURE_opengles32:BOOL=ON \
	-DQT_FEATURE_use_lld_linker:BOOL=ON \
	-DQT_FEATURE_xcb_native_painting:BOOL=ON \
	-DQT_FEATURE_openssl:BOOL=ON \
	-DQT_FEATURE_openssl_linked:BOOL=ON \
	-DQT_FEATURE_system_zlib:BOOL=ON \
	-DQT_FEATURE_system_sqlite:BOOL=ON \
	-DQT_FEATURE_libproxy:BOOL=ON \
	-DQT_FEATURE_ltcg:BOOL=ON \
	-DQT_FEATURE_sctp:BOOL=ON \
	-DINPUT_doubleconversion=system \
	-DINPUT_freetype=system \
	-DINPUT_harfbuzz=system \
	-DINPUT_libjpeg=system \
	-DINPUT_libpng=system \
	-DINPUT_sqlite=system \
	-DQT_INPUT_openssl=linked \
%ifarch %{armx}
	-DQT_FEATURE_neon:BOOL=ON \
%endif
	-DQT_USE_BUNDLED_BundledFreetype:BOOL=OFF \
	-DQT_USE_BUNDLED_BundledHarfbuzz:BOOL=OFF \
	-DQT_USE_BUNDLED_BundledLibpng:BOOL=OFF \
	-DQT_USE_BUNDLED_BundledPcre2:BOOL=OFF \
	-DQT_WILL_INSTALL:BOOL=ON

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
# Static helper lib without headers -- useless
rm -f %{buildroot}%{_libdir}/qt6/%{_lib}/libpnp_basictools.a
# Put stuff where tools will find it
# We can't do the same for %{_includedir} right now because that would
# clash with qt5 (both would want to have /usr/include/QtCore and friends)
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir}/cmake
for i in %{buildroot}%{_qtdir}/lib/*.so* %{buildroot}%{_qtdir}/lib/*.a; do
	ln -s qt%{major}/lib/$(basename ${i}) %{buildroot}%{_libdir}/
done
for i in %{buildroot}%{_qtdir}/lib/cmake/*; do
	ln -s ../qt%{major}/lib/cmake/$(basename ${i}) %{buildroot}%{_libdir}/cmake/
done
# Put syncqt where the other Qt packages can find it
mkdir -p %{buildroot}%{_libexecdir}
ln -s ../%{_lib}/qt%{major}/libexec/syncqt.pl %{buildroot}%{_libexecdir}/
