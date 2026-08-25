#define snapshot 20200627
#define beta rc

%ifarch %{aarch64}
%global optflags %{optflags} -march=armv8-a+crypto
%endif

Name:		qt6-qtbase
Version:	6.11.2
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtbase-%{snapshot}.tar.zst
%else
Source:		https://download.qt.io/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtbase-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
# rpm macros
Source100:	macros.qt6
%{load:%{S:100}}
# Extra PGO trainer: chained QByteArray case conversion + typical QSet ops
Source101:	pgo-train-containers.cpp
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}3
Group:		System/Libraries
Summary:	Version %{qtmajor} of the Qt framework
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	perl
BuildRequires:	icu
BuildRequires:	pkgconfig(libzstd)
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
BuildRequires:	pkgconfig(libb2)
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
BuildRequires:	firebird-devel
BuildRequires:	%mklibname -d fbclient
# For the theme only
BuildRequires:	pkgconfig(gtk+-3.0)
License:	LGPLv3/GPLv3/GPLv2

%patchlist
#qtbase-6.0-rc2-examples-compile.patch
#qtbase-init-pluginpath.patch
qtbase-6.2.0-aarch64-buildfix.patch
#aarch64-qhash-fix-build-with-gcc.patch
# Automatically detect whether or not the arcan QPA should be used
https://codeberg.org/vimpostor/qtarcan/raw/branch/master/distr/0001-Use-arcan-platform-plugin-by-default.diff
# QTBUG-149431: setFallbackThemeName() must not change themeName()
# https://codereview.qt-project.org/c/qt/qtbase/+/763319 (6.11.3+)
qtbase-6.11.2-qiconloader-themeName.patch

%description
Version %{qtmajor} of the Qt framework

%define extra_files_Core \
%{_sysconfdir}/ld.so.conf.d/*.conf

%define extra_devel_files_Core \
%{_qtdir}/bin/qt-configure-module \
%dir %{_qtdir}/libexec \
%{_qtdir}/libexec/moc \
%{_qtdir}/libexec/rcc \
%{_qtdir}/libexec/qt_cyclonedx_generator.py \
%dir %{_qtdir}/metatypes \
%dir %{_qtdir}/modules \
%{_qtdir}/share \
%{_libdir}/pkgconfig/Qt6Platform.pc \
%{_qtdir}/lib/pkgconfig

%define extra_devel_reqprov_Core \
Requires: %{name}-tools = %{EVRD} \
Requires: qmake-qt%{qtmajor} = %{EVRD} \
Requires: cmake(Qt6) \
Provides: cmake(Qt6ConcurrentPrivate) = %{EVRD}

%define extra_devel_reqprov_XcbQpa \
Provides: cmake(Qt6XcbQpaPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_WlShellIntegration \
Provides: cmake(Qt6WlShellIntegrationPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_WaylandClient \
Provides: cmake(Qt6WaylandGlobalPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_Test \
Provides: cmake(Qt6TestInternalsPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_DeviceDiscoverySupport \
Provides: cmake(Qt6DeviceDiscoverySupportPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_EglFSDeviceIntegration \
Provides: cmake(Qt6EglFSDeviceIntegrationPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_EglFsKmsSupport \
Provides: cmake(Qt6EglFsKmsSupportPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_EglFsKmsGbmSupport \
Provides: cmake(Qt6EglFsKmsGbmSupportPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_FbSupport \
Provides: cmake(Qt6FbSupportPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_InputSupport \
Provides: cmake(Qt6InputSupportPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_KmsSupport \
Provides: cmake(Qt6KmsSupportPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_OpenGLWidgets \
Provides: cmake(Qt6OpenGLWidgetsPrivate) = %{EVRD}

%define extra_devel_reqprov_Gui \
Requires: cmake(Qt6DBus) \
Requires: pkgconfig(egl) \
Requires: pkgconfig(glesv2) \
Requires: pkgconfig(xkbcommon) \
Requires: pkgconfig(opengl) \
Requires: pkgconfig(glx) \
Obsoletes: %{_lib}Qt6WaylandEglClientHwIntegration-devel < %{EVRD}

%define extra_devel_reqprov_Widgets \
Requires: cmake(Qt6Gui)

%define extra_files_Gui \
%dir %{_qtdir}/plugins/egldeviceintegrations \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-emu-integration.so \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-kms-egldevice-integration.so \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-kms-integration.so \
%{_qtdir}/plugins/egldeviceintegrations/libqeglfs-x11-integration.so \
%dir %{_qtdir}/plugins/xcbglintegrations \
%{_qtdir}/plugins/xcbglintegrations/libqxcb-egl-integration.so \
%{_qtdir}/plugins/xcbglintegrations/libqxcb-glx-integration.so\
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

%define extra_devel_files_FbSupport \
%{_qtdir}/mkspecs/modules/qt_lib_fb_support_private.pri

%define extra_devel_files_InputSupport \
%{_qtdir}/mkspecs/modules/qt_lib_input_support_private.pri

%define extra_devel_files_EglFsKmsSupport \
%{_qtdir}/mkspecs/modules/qt_lib_eglfs_kms_support_private.pri \
%{_qtdir}/mkspecs/modules/qt_lib_kms_support_private.pri

%define extra_devel_files_EglFsKmsGbmSupport \
%{_qtdir}/mkspecs/modules/qt_lib_eglfs_kms_gbm_support_private.pri

%define extra_devel_files_DeviceDiscoverySupport \
%{_qtdir}/mkspecs/modules/qt_lib_devicediscovery_support_private.pri

%define extra_devel_files_XcbQpa \
%{_qtdir}/mkspecs/modules/qt_lib_xcb_qpa_lib_private.pri

%define extra_devel_files_DBus \
%{_qtdir}/bin/qdbuscpp2xml \
%{_qtdir}/bin/qdbusxml2cpp

%define extra_files_Network \
%dir %{_qtdir}/plugins/networkinformation \
%{_qtdir}/plugins/networkinformation/libqconnman.so \
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

%define extra_devel_reqprov_PrintSupport \
Requires: pkgconfig(cups)

%define extra_devel_reqprov_Sql \
Requires: %{name}-sql-sqlite

%define extra_files_Sql \
%dir %{_qtdir}/plugins/sqldrivers

# FIXME does it make sense to split some of the plugins here
# into separate subpackages?
%define extra_files_WaylandClient \
%{_qtdir}/plugins/platforms/libqwayland.so \
%dir %{_qtdir}/plugins/wayland-decoration-client \
%{_qtdir}/plugins/wayland-decoration-client/libbradient.so \
%dir %{_qtdir}/plugins/wayland-graphics-integration-client \
%{_qtdir}/plugins/wayland-graphics-integration-client/libdmabuf-server.so \
%{_qtdir}/plugins/wayland-graphics-integration-client/libdrm-egl-server.so \
%{_qtdir}/plugins/wayland-graphics-integration-client/libqt-plugin-wayland-egl.so \
%{_qtdir}/plugins/wayland-graphics-integration-client/libshm-emulation-server.so \
%{_qtdir}/plugins/wayland-graphics-integration-client/libvulkan-server.so \
%dir %{_qtdir}/plugins/wayland-shell-integration \
%{_qtdir}/plugins/wayland-shell-integration/libfullscreen-shell-v1.so \
%{_qtdir}/plugins/wayland-shell-integration/libwl-shell-plugin.so \
%{_qtdir}/plugins/wayland-shell-integration/libxdg-shell.so

%define extra_devel_files_Test \
%{_qtdir}/mkspecs/modules/qt_lib_testlib.pri \
%{_qtdir}/mkspecs/modules/qt_lib_testlib_private.pri \
%{_qtdir}/lib/cmake/Qt%{qtmajor}TestInternalsPrivate \
%{_qtdir}/modules/TestInternalsPrivate.json

%define extra_devel_files_WaylandClient \
%{_qtdir}/include/QtWaylandGlobal \
%{_qtdir}/lib/cmake/Qt%{qtmajor}WaylandGlobalPrivate \
%{_qtdir}/lib/cmake/Qt%{qtmajor}WaylandScannerTools \
%{_qtdir}/libexec/qtwaylandscanner \
%{_qtdir}/share/qt6/wayland \
%{_qtdir}/modules/WaylandGlobalPrivate.json \

%define extra_devel_files_Widgets \
%{_qtdir}/libexec/uic

%qt6libs Core Concurrent DBus EglFSDeviceIntegration EglFsKmsSupport EglFsKmsGbmSupport Gui Network OpenGL OpenGLWidgets PrintSupport Sql Test WaylandClient WlShellIntegration Widgets XcbQpa Xml
%qt6staticlibs DeviceDiscoverySupport FbSupport InputSupport KmsSupport

%package sql-sqlite
Summary: QtSQL plugin for accessing SQLite databases
Group: System/Libraries

%description sql-sqlite
QtSQL plugin for accessing SQLite databases

%files sql-sqlite
%{_qtdir}/plugins/sqldrivers/libqsqlite.so

%package sql-firebird
Summary: QtSQL plugin for accessing Firebird and Interbase databases
Group: System/Libraries

%description sql-firebird
QtSQL plugin for accessing Firebird and Interbase databases

%files sql-firebird
%{_qtdir}/plugins/sqldrivers/libqsqlibase.so

%package sql-mariadb
Summary: QtSQL plugin for accessing MariaDB and MySQL databases
Group: System/Libraries

%description sql-mariadb
QtSQL plugin for accessing MariaDB and MySQL databases

%files sql-mariadb
%{_qtdir}/plugins/sqldrivers/libqsqlmysql.so

%package sql-odbc
Summary: QtSQL plugin for accessing databases through ODBC
Group: System/Libraries

%description sql-odbc
QtSQL plugin for accessing databases through ODBC

%files sql-odbc
%{_qtdir}/plugins/sqldrivers/libqsqlodbc.so

%package sql-postgresql
Summary: QtSQL plugin for accessing PostgreSQL databases
Group: System/Libraries

%description sql-postgresql
QtSQL plugin for accessing PostgreSQL databases

%files sql-postgresql
%{_qtdir}/plugins/sqldrivers/libqsqlpsql.so

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
%exclude %{_qtdir}/mkspecs/modules/*
%{_qtdir}/libexec/qt-internal-configure-examples
%{_qtdir}/libexec/qt-internal-configure-tests

%package -n qt%{qtmajor}-cmake
Summary: Cmake extensions for Qt %{qtmajor}
Group: Development/KDE and Qt
Requires: cmake

%description -n qt%{qtmajor}-cmake
Cmake extensions for Qt %{qtmajor}

%files -n qt%{qtmajor}-cmake
%{_qtdir}/bin/qt-cmake
%{_qtdir}/bin/qt-cmake-create
%{_qtdir}/libexec/cmake_automoc_parser
%dir %{_qtdir}/lib/cmake
%{_qtdir}/lib/cmake/Qt6
%{_qtdir}/lib/cmake/Qt6BuildInternals
%{_prefix}/lib/rpm/macros.d/macros.qt6
%{_qtdir}/libexec/qt-cmake-private
%{_qtdir}/libexec/qt-cmake-private-install.cmake
%{_qtdir}/libexec/qt-cmake-standalone-test

%package tools
Summary: Qt %{qtmajor} build tools
Group: Development/KDE and Qt

%description tools
Qt %{qtmajor} build tools

%files tools
%{_qtdir}/bin/androiddeployqt
%{_qtdir}/bin/androiddeployqt%{qtmajor}
%{_qtdir}/bin/androidtestrunner
%{_qtdir}/bin/wasmdeployqt
%{_qtdir}/bin/wasmdeployqt%{qtmajor}
%{_qtdir}/libexec/qlalr
%{_qtdir}/libexec/qt-android-runner.py
%{_qtdir}/bin/qtpaths
%{_qtdir}/bin/qtpaths%{qtmajor}
%{_qtdir}/libexec/qvkgen
%{_qtdir}/libexec/tracegen
%{_qtdir}/libexec/syncqt
%{_qtdir}/libexec/tracepointgen
%{_qtdir}/sbom

%prep
%autosetup -p1 -n qtbase%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}

sed -i -e 's,@QTDIR@,%{_qtdir},g' src/gui/kernel/qguiapplication.cpp

# %pgo only needs tests/benchmarks. Do not configure the autotest
# tree, but keep sources some benches include (baseline/shared, …).
printf '%s\n' '# skipped: PGO trainer uses tests/benchmarks only' > tests/auto/CMakeLists.txt
printf '%s\n' '# skipped: PGO trainer uses tests/benchmarks only' > tests/baseline/CMakeLists.txt

# FIXME This may be interesting in the future:
#	-DQT_FEATURE_cxx2a:BOOL=ON
# As of 6.0.0-rc2 and clang 11.0.1, causes a compile failure

# FIXME This may be interesting for some boards
#	-DQT_FEATURE_opengl_dynamic:BOOL=ON \
#	-DQT_FEATURE_opengles2:BOOL=ON
# But as of 6.6.0-beta2, it disables the X11 GLX plugin and
# enabling any GLES driver breaks video output in QMplay2 and
# obs-studio

# FIXME Investigate
#	-DQT_FEATURE_lttng:BOOL=ON

# -DBUILD_WITH_PCH:BOOL=OFF is a workaround for
# https://github.com/llvm/llvm-project/issues/57505
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_BUILD_TESTS:BOOL=ON \
	-DQT_BUILD_TESTS_BY_DEFAULT:BOOL=OFF \
	-DQT_BUILD_BENCHMARKS:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DQT_FEATURE_aesni:BOOL=ON \
	-DQT_FEATURE_cxx20:BOOL=ON \
	-DQT_FEATURE_dynamicgl:BOOL=ON \
	-DQT_FEATURE_ipc_posix:BOOL=ON \
	-DQT_FEATURE_journald:BOOL=ON \
	-DQT_FEATURE_opengl_dynamic:BOOL=OFF \
	-DQT_FEATURE_opengl_desktop:BOOL=ON \
	-DQT_FEATURE_opengles2:BOOL=OFF \
	-DQT_FEATURE_opengles3:BOOL=OFF \
	-DQT_FEATURE_opengles31:BOOL=OFF \
	-DQT_FEATURE_opengles32:BOOL=OFF \
	-DQT_FEATURE_use_lld_linker:BOOL=ON \
	-DQT_FEATURE_xcb_native_painting:BOOL=ON \
	-DQT_FEATURE_openssl:BOOL=ON \
	-DQT_FEATURE_openssl_linked:BOOL=ON \
	-DQT_FEATURE_openssl_hash:BOOL=ON \
	-DQT_FEATURE_system_libb2:BOOL=ON \
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
	-DINPUT_libb2=system \
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
	-DQT_WILL_INSTALL:BOOL=ON \
	-DBUILD_WITH_PCH:BOOL=OFF

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

# Train on Qt's own microbenchmarks (QString/QObject/QPainter/…).
# Offscreen QPA: no display. Failures are ignored so one broken bench
# does not abort the package. Autotests are a bad profile (error paths).
#
# Do not pass -platform on the command line: QCoreApplication benches
# (QVector/QMap/QByteArray/QSet/QList/QString/…) treat it as an unknown
# test option, print help, and never run — so PGO saw those paths as
# cold and made them slower. QT_QPA_PLATFORM=offscreen is enough for GUI.
%pgo
export LD_LIBRARY_PATH="$(pwd)/build/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export QT_QPA_PLATFORM=offscreen
export QT_PLUGIN_PATH="$(pwd)/build/plugins"
# Build bench executables only (the 'benchmark' target also *runs* them)
benches=$(ninja -C build -t targets | sed 's/:.*//' | sed -n 's|.*/||; s/_benchmark$//p' | grep -v '^benchmark$' | sort -u)
if [ -n "$benches" ]; then
	ninja -C build $benches || :
fi
find_bench() {
	find build/tests/benchmarks -type f -name "$1" -executable 2>/dev/null | head -1
}
# Extra weight for containers PGO otherwise treats as cold vs QPainter.
# Skip quadratic / 100MB rows that burn the timeout before useful paths.
train() {
	local t=$1 bin=$2
	shift 2
	[ -n "$bin" ] && [ -x "$bin" ] || return 0
	timeout "$t" "$bin" "$@" >/dev/null 2>&1 || :
}
train 60 "$(find_bench tst_bench_qvector)" -iterations 8
train 60 "$(find_bench tst_bench_qmap)" -iterations 8
# Full QSet bench (intersect/unite/contains_then_insert). 90s so the
# 1e6 rows finish — 45s only got through intersect.
train 90 "$(find_bench tst_bench_qset)" -iterations 4
# Include chained toUpper().toLower() (the remaining ~0.07x hole) and
# toLongLong; skip only the 100MB append:100000000 row.
train 60 "$(find_bench tst_bench_qbytearray)" -iterations 8 \
	append:1 append:10 append:100 append:1000 append:10000 \
	append:100000 append:1000000 append:10000000 \
	toUpper toLower toUpperThenLower toLowerThenUpper \
	toLongLong toULongLong toPercentEncoding \
	latin1Uppercasing_qt54 latin1Uppercasing_xlate \
	latin1Uppercasing_xlate_checked latin1Uppercasing_category \
	latin1Uppercasing_bitcheck operator_assign_char
train 60 "$(find_bench tst_bench_qlist)" -iterations 6 \
	removeAll_primitive removeAll_movable removeAll_complex \
	appendOne_int appendOne_primitive appendOne_movable \
	appendOne_complex appendOne_QString \
	prependOne_int prependOne_QString \
	appendPrependOne_int \
	removeFirstGeneral_int removeFirstSpecial_int
# Typical QByteArray / QSet use the upstream benches do not cover
# (chained case conversion, insert/lookup/remove, modest set algebra).
c++ -O2 -std=c++20 -fPIC -pthread \
	-Ibuild/include -Ibuild/include/QtCore -DQT_CORE_LIB \
	%{S:101} -Lbuild/lib -Wl,-rpath,"$(pwd)/build/lib" -lQt6Core \
	-o build/pgo-train-containers \
	&& timeout 60 build/pgo-train-containers >/dev/null 2>&1 || :
find build/tests/benchmarks -type f -executable ! -name '*.so*' ! -name '*Wrapper*' 2>/dev/null \
| while read -r bin; do
	case "$bin" in
	*testlib*|*dbus*|*sql*) continue ;;
	# Already trained above with more iterations; skip the huge rows here.
	*tst_bench_qvector|*tst_bench_qmap|*tst_bench_qset|*tst_bench_qbytearray|*tst_bench_qlist) continue ;;
	esac
	timeout 90 "$bin" -iterations 1 >/dev/null 2>&1 || :
done

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

%qt6_postinstall
ln -s ../../pkgconfig %{buildroot}%{_qtdir}/lib/pkgconfig

# FIXME
# Replace the %{_qtdir}/lib/pkgconfig from qt6-qtbase <= 6.5.0-1
# with a symlink. This should be removed once we stop supporting
# updating from a version of OMV with qt6-qtbase <= 6.5.0-1
%pretrans -p <lua>
st = posix.stat("%{_qtdir}/lib/pkgconfig")
if st and st.type == "directory" then
	for i,p in pairs(posix.dir("%{_qtdir}/lib/pkgconfig")) do
		if(p ~= "." and p ~= "..") then
			os.rename("%{_qtdir}/lib/pkgconfig/" .. p, "%{_libdir}/pkgconfig/" .. p)
		end
	end
	posix.rmdir("%{_qtdir}/lib/pkgconfig")
	posix.symlink("../../pkgconfig", "%{_qtdir}/lib/pkgconfig")
end
