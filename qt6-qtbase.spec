#define snapshot 20200627
#define beta rc

Name:		qt6-qtbase
Version:	6.3.1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtbase-%{snapshot}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtbase-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
# rpm macros
Source100:	macros.qt6
%{load:%{S:100}}
Patch0:		qtbase-6.0-rc2-examples-compile.patch
Patch1:		qtbase-init-pluginpath.patch
Patch2:		qtbase-6.2.0-aarch64-buildfix.patch
Patch3:		aarch64-qhash-fix-build-with-gcc.patch
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
Group:		System/Libraries
Summary:	Version %{qtmajor} of the Qt framework
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
BuildRequires:	pkgconfig(egl)
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
Version %{qtmajor} of the Qt framework

%define extra_files_Core \
%{_sysconfdir}/ld.so.conf.d/*.conf

%define extra_devel_files_Core \
%{_qtdir}/bin/qt-configure-module \
%dir %{_qtdir}/libexec \
%{_qtdir}/libexec/moc \
%{_qtdir}/libexec/rcc \
%dir %{_qtdir}/modules \
%dir %{_qtdir}/lib/metatypes

%define extra_devel_reqprov_Core \
Requires: %{name}-tools = %{EVRD} \
Requires: qmake-qt%{qtmajor} = %{EVRD} \

%define extra_files_Gui \
%dir %{_qtdir}/plugins/egldeviceintegrations \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-emu-integration.so \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-kms-egldevice-integration.so \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-kms-integration.so \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-x11-integration.so \
%dir %{_qtdir}/plugins/xcbglintegrations \
%{_qtdir}/plugins/xcbglintegrations/libqxcb-egl-integration.so \
%dir %{_qtdir}/plugins/generic \
%{_qtdir}/plugins/generic/libqevdevkeyboardplugin.so \
%{_qtdir}/plugins/generic/libqevdevmouseplugin.so \
%{_qtdir}/plugins/generic/libqevdevtabletplugin.so \
%{_qtdir}/plugins/generic/libqevdevtouchplugin.so \
%{_qtdir}/plugins/generic/libqlibinputplugin.so \
%{_qtdir}/plugins/generic/libqtuiotouchplugin.so \
%dir %{_qtdir}/plugins/imageformats \
%{_qtdir}/plugins/imageformats/libqgif.so \
%{_qtdir}/plugins/imageformats/libqico.so \
%{_qtdir}/plugins/imageformats/libqjpeg.so \
%dir %{_qtdir}/plugins/platforminputcontexts \
%{_qtdir}/plugins/platforminputcontexts/libcomposeplatforminputcontextplugin.so \
%{_qtdir}/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so \
%dir %{_qtdir}/plugins/platforms \
%{_qtdir}/plugins/platforms/libqeglfs.so \
%{_qtdir}/plugins/platforms/libqlinuxfb.so \
%{_qtdir}/plugins/platforms/libqminimal.so \
%{_qtdir}/plugins/platforms/libqminimalegl.so \
%{_qtdir}/plugins/platforms/libqoffscreen.so \
%{_qtdir}/plugins/platforms/libqvkkhrdisplay.so \
%{_qtdir}/plugins/platforms/libqvnc.so \
%{_qtdir}/plugins/platforms/libqxcb.so \
%dir %{_qtdir}/plugins/platformthemes \
%{_qtdir}/plugins/platformthemes/libqxdgdesktopportal.so

%define extra_devel_files_DBus \
%{_qtdir}/bin/qdbuscpp2xml \
%{_qtdir}/bin/qdbusxml2cpp

%define extra_files_Network \
%dir %{_qtdir}/plugins/networkinformation \
%{_qtdir}/plugins/networkinformation/libqnetworkmanager.so \
%{_qtdir}/plugins/networkinformation/libqglib.so \
%dir %{_qtdir}/plugins/tls \
%{_qtdir}/plugins/tls/libqcertonlybackend.so \
%{_qtdir}/plugins/tls/libqopensslbackend.so \

%define extra_devel_files_Network \
%{_qtdir}/lib/cmake/Qt6HostInfo

%define extra_files_PrintSupport \
%dir %{_qtdir}/plugins/printsupport \
%{_qtdir}/plugins/printsupport/libcupsprintersupport.so

%define extra_files_Sql \
%dir %{_qtdir}/plugins/sqldrivers \
%{_qtdir}/plugins/sqldrivers/libqsqlite.so \
%{_qtdir}/plugins/sqldrivers/libqsqlmysql.so \
%{_qtdir}/plugins/sqldrivers/libqsqlodbc.so \
%{_qtdir}/plugins/sqldrivers/libqsqlpsql.so

%define extra_devel_files_Widgets \
%{_qtdir}/libexec/uic

%qt6libs Core Concurrent DBus EglFSDeviceIntegration EglFsKmsSupport EglFsKmsGbmSupport Gui Network OpenGL OpenGLWidgets PrintSupport Sql Test Widgets XcbQpa Xml
%qt6staticlibs DeviceDiscoverySupport FbSupport InputSupport KmsSupport


%package doc
Summary: Documentation for the Qt %{qtmajor} framework
Group: Documentation

%description doc
Documentation for the Qt %{qtmajor} framework

%files doc
%{_qtdir}/doc


%package examples
Summary: Examples for the Qt %{qtmajor} framework
Group: Documentation

%description examples
Documentation for the Qt %{qtmajor} framework

%files examples
%{_qtdir}/examples


%package theme-gtk3
Summary: GTK3 Theme for Qt %{qtmajor}
Group: User Interface/Desktops
Requires: %{mklibname Qt%{qtmajor}Gui} = %{EVRD}

%description theme-gtk3
GTK3 Theme for Qt %{qtmajor}

%files theme-gtk3
%{_qtdir}/plugins/platformthemes/libqgtk3.so


%package -n qmake-qt%{qtmajor}
Summary: The legacy qmake build tool for Qt %{qtmajor}
Group: Development/Tools

%description -n qmake-qt%{qtmajor}
The legacy qmake build tool for Qt %{qtmajor}

%files -n qmake-qt%{qtmajor}
%{_bindir}/qmake-qt6
%{_qtdir}/bin/qmake
%{_qtdir}/bin/qmake6
%{_qtdir}/mkspecs
%{_qtdir}/libexec/qt-internal-configure-tests
%{_qtdir}/libexec/ensure_pro_file.cmake


%package -n qt%{qtmajor}-cmake
Summary: Cmake extensions for Qt %{qtmajor}
Group: Development/KDE and Qt

%description -n qt%{qtmajor}-cmake
Cmake extensions for Qt %{qtmajor}

%files -n qt%{qtmajor}-cmake
%{_qtdir}/bin/qt-cmake
%{_qtdir}/bin/qt-cmake-private
%{_qtdir}/bin/qt-cmake-private-install.cmake
%{_qtdir}/bin/qt-cmake-standalone-test
%{_qtdir}/libexec/cmake_automoc_parser
%dir %{_qtdir}/lib/cmake
%{_qtdir}/lib/cmake/Qt6
%{_qtdir}/lib/cmake/Qt6BuildInternals
%{_qtdir}/libexec/android_emulator_launcher.sh
%{_prefix}/lib/rpm/macros.d/macros.qt6


%package tools
Summary: Qt %{qtmajor} build tools
Group: Development/KDE and Qt

%description tools
Qt %{qtmajor} build tools

%files tools
%{_qtdir}/bin/androiddeployqt
%{_qtdir}/bin/androidtestrunner
%{_qtdir}/libexec/qlalr
%{_qtdir}/bin/qtpaths
%{_qtdir}/bin/qtpaths%{qtmajor}
%{_qtdir}/libexec/qvkgen
%{_qtdir}/libexec/syncqt.pl
%{_qtdir}/libexec/tracegen

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
	-DQT_FEATURE_cxx20:BOOL=ON \
	-DQT_FEATURE_dynamicgl:BOOL=ON \
	-DQT_FEATURE_ipc_posix:BOOL=ON \
	-DQT_FEATURE_journald:BOOL=ON \
	-DQT_FEATURE_opengl_dynamic:BOOL=ON \
	-DQT_FEATURE_opengl_desktop:BOOL=ON \
	-DQT_FEATURE_opengles2:BOOL=ON \
	-DQT_FEATURE_opengles3:BOOL=ON \
	-DQT_FEATURE_opengles31:BOOL=ON \
	-DQT_FEATURE_opengles32:BOOL=ON \
	-DQT_FEATURE_use_lld_linker:BOOL=ON \
	-DQT_FEATURE_xcb_native_painting:BOOL=ON \
	-DQT_FEATURE_openssl:BOOL=ON \
	-DQT_FEATURE_openssl_linked:BOOL=ON \
	-DQT_FEATURE_system_jpeg:BOOL=ON \
	-DQT_FEATURE_system_png:BOOL=ON \
	-DQT_FEATURE_system_zlib:BOOL=ON \
	-DQT_FEATURE_system_sqlite:BOOL=ON \
	-DQT_FEATURE_system_xcb_xinput:BOOL=ON \
	-DQT_FEATURE_libproxy:BOOL=ON \
	-DQT_FEATURE_ltcg:BOOL=ON \
	-DQT_FEATURE_sctp:BOOL=ON \
	-DQT_FEATURE_gc_binaries:BOOL=ON \
	-DQT_FEATURE_futimes:BOOL=ON \
	-DQT_FEATURE_renameat2:BOOL=ON \
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
%ifarch %{x86_64}
	-DQT_FEATURE_sse2:BOOL=ON \
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

# Add rpm macros
mkdir -p %{buildroot}%{_prefix}/lib/rpm/macros.d/
cp %{S:100} %{buildroot}%{_prefix}/lib/rpm/macros.d/macros.qt6

# Make sure the libraries can be found
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat >%{buildroot}%{_sysconfdir}/ld.so.conf.d/qt%{qtmajor}.conf <<EOF
%{_qtdir}/lib
EOF

# Put qmake-qt6 where some stuff (e.g. LO) looks for it
mkdir -p %{buildroot}%{_bindir}
ln -s %{_qtdir}/bin/qmake %{buildroot}%{_bindir}/qmake-qt6
