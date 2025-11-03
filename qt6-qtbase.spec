#define snapshot 20200627
#define beta rc

%ifarch %{aarch64}
%global optflags %{optflags} -march=armv8-a+crypto
%endif

Name:		qt6-qtbase
Version:	6.10.0
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtbase-%{snapshot}.tar.zst
%else
Source:		https://download.qt.io/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtbase-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
# rpm macros
Source100:	macros.qt6
%{load:%{S:100}}
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}2
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

# From upstream
0001-docs-Fix-links-to-QTest-setThrowOnFail.patch
0002-QDataStream-fix-Werror-Wshorten-64-to-32-on-32-bit-C.patch
0003-CMake-Workaround-Android-CMP0155-issue.patch
0004-uic-test-Update-forms.patch
0005-uic-Python-Handle-surrogates-correctly.patch
0007-Fix-possible-assert-when-inserting-columns-in-QTextD.patch
0008-Relax-timing-check-in-tst_QMovie-multiFrameImage.patch
0009-QDialog-Add-missing-attribute-set-for-explicit-hide-.patch
0010-qiostheme-Set-more-palette-color-roles.patch
0012-a11y-macOS-Implement-accessibilityMinValue-and-acces.patch
0015-QTabBar-fix-handling-hidden-tabs.patch
0016-QMacStyle-protect-against-a-nullptr-context.patch
0017-wayland-Fix-cross-compiling-on-Windows.patch
0018-Wayland-skip-tst_QWindow-modalWindowModallity-on-GNO.patch
0019-Wayland-skip-tst_QWindow-modalWindowEnterEventOnHide.patch
0028-Android-add-color-to-test-widgets-to-visualize-windo.patch
0029-QImageWriter-Don-t-load-handlers-from-plugins-if-we-.patch
0032-Add-camel-case-header-for-qtconcurrenttask.h.patch
0033-Android-add-docs-to-QtActivity.appendApplicationPara.patch
0034-Android-warn-instead-of-assert-on-invalid-winId-on-w.patch
0036-docs-Fix-relates-on-QTEST_THROW_ON_-FAIL-SKIP-macro.patch
0038-CMake-Wrap-SBOM-execute_process-file-paths-in-quotes.patch
0039-util-unicode-remove-replace-_-from-readScripts.patch
0040-util-unicode-readArabicShaping-remove-replace-call.patch
0041-util-unicode-readEastAsianWidth-remove-simplified-ca.patch
0042-util-unicode-createNormalizationCorrections-remove-r.patch
0043-util-unicode-remove-replace-calls-from-remaining-rea.patch
0044-util-unicode-add-missing-assertions-on-field-counts.patch
0045-QLocale-enable-NRVO-in-matchingLocales.patch
0046-docs-mention-why-one-would-want-QTEST_THROW_ON_-FAIL.patch
0047-QJsonObject-fix-Werror-Wshorten-64-to-32-on-32-bit-p.patch
0048-Respect-QT_NO_INT128-in-qtypes.cpp-s-error.patch
0053-macOS-Show-icons-in-menus-on-macOS-26-and-above.patch
0054-Gui-name-mangle-qt_ft_grays_raster.patch
0055-darwin-namespace-permission-request-loader-function.patch
0059-QMetaObject-port-QArgumentType-to-QByteArrayView.patch
0060-tst_QDir-use-COMPARE_EQ-when-comparing-QStringLists.patch
0061-Move-CharBuff-back-into-QLocaleData.patch
0062-syncqt.cpp-Include-algorithm-for-std-transform.patch
0063-CMake-Simplify-the-installation-of-.prl-files.patch
0065-a11y-iOS-Do-not-set-UIAccessibilityTraitAdjustable-f.patch
0074-util-unicode-prepare-qFatal-s-for-being-passed-views.patch
0075-Doc-Document-the-specific-headers-for-the-Qt-Concurr.patch
0076-QMetaObject-Add-missing-include-for-QSpan.patch
0081-cmake-Don-t-create-framework-header-directories-unle.patch
0082-QTextBoundaryFinder-squash-the-bitfield-member.patch
0083-CMake-remove-no_core_dep-relic.patch
0084-expected-do-not-include-qconfig.h.patch
0086-QByteArray-replace-pos-len-don-t-detach-the-underlyi.patch
0087-QStringConverter-allow-appendToBuffer-to-write-to-th.patch
0088-tst_qnetworkreply_local-shorten-the-local-socket-nam.patch
0089-Windows11Style-rework-color-handling-for-Checkbox-Ra.patch
0090-HTTP-don-t-send-content-length-0.patch
0091-Don-t-report-enable-safe-areas-for-graphics-view-pro.patch
0092-iOS-Fix-a11y-representation-of-RadioButton-and-Check.patch
0093-Add-security-tags-to-src-gui-itemmodels.patch
0094-CMake-add-QT_NAMESPACE-property-to-Qt-Core.patch
0096-Tracepointgen-handle-windows-absolute-paths.patch
0098-a11y-Android-Set-a-RangeInfo-by-using-the-ValueInter.patch
0099-Android-Avoid-announcing-simple-text-as-clickable.patch
0100-tst_qmetamethod-don-t-use-indexOfSlot-with-non-slots.patch
0102-Assess-security-level-for-files-under-qtbase-src-plu.patch
0103-QMacStyle-re-adjust-title-margins-for-push-buttons.patch
0106-Work-around-QFileSystemEngine-behavior-on-VxWorks-ho.patch
0107-Introduce-_qt_internal_android_get_platform_tools_pa.patch
0108-Introduce-_qt_internal_android_get_package_source_di.patch
0109-Move-the-Do-not-compress-Qt-binary-resources-file-co.patch
0110-tst_QWidget-account-for-resize-event-after-receiving.patch
0111-Make-QTEST_THROW_ON_FAIL-work-from-within-QtConcurre.patch
0112-Android-Fix-issues-with-the-benchmark.patch
0114-CMake-Fix-wrong-elseif-usage-in-sbom-deterministic-b.patch
0115-Bail-out-on-null-swapchain-in-rhi-flush.patch
0116-CMake-Add-a-test-for-SBOM-generation.patch
0117-CMake-Fix-sbom-project-end-target-finalization-to-be.patch
0118-CMake-Move-SBOM-deferred-finalization-to-the-extend-.patch
0119-CMake-Fix-handling-of-empty-CMAKE_BUILD_TYPE-during-.patch
0120-CMake-Rename-TYPE-to-SBOM_ENTITY_TYPE-in-SBOM-API.patch
0121-CMake-Fix-double-slash-in-SBOM-install-path.patch
0122-CMake-Add-an-SBOM-DOCUMENT_CREATOR_TOOL-project-opti.patch
0123-CMake-Add-an-SBOM-LICENSE_DIR_PATHS-project-option.patch
0124-CMake-Add-non-internal-option-names-for-the-SBOM-pro.patch
0125-CMake-Fix-non_git_version-check.patch
0126-Windows11Style-rework-text-color-handling-for-Button.patch
0127-Support-graphics-reset-notifications-on-EGL.patch
0128-Http-Improve-error-string-when-there-is-no-reason-ph.patch
0129-Assess-security-level-for-files-under-qtbase-src-wid.patch
0130-Add-security-tags-to-the-Qt-Sql-module.patch
0131-Windows-Return-hittest-region-for-CustomizeWindowHin.patch
0132-tst_QWindow-stateChangeSignal-Don-t-QTRY_VERIFY-a-qW.patch
0133-QLibraryInfo-Add-MSVC-2026.patch
0134-QTest-Add-MSVC-2026-blacklist-keyword.patch
0135-util-unicode-split-and-trim-in-readUnicodeFile-to-sa.patch
0136-util-unicode-remove-properties-char16_t-declaration-.patch
0137-Fix-broadcasts-with-dual-socket-IPv6-in-setSocketDes.patch
0138-QByteArray-match-QString-indexOf-behavior-for-large-.patch
0139-Q-StringView-contains-call-the-char-overload-of-inde.patch
0140-tst_QThread-further-improve-test-on-multiple-threads.patch
0141-CMake-Rework-SBOM-version-handling.patch
0142-CRA-review-qtbase-src-widgets-util.patch
0143-Assess-security-level-for-files-under-qtbase-src-wid.patch
0144-qwineventnotifier.h-Use-angle-bracket-include-style.patch
0145-plugins-platforms-wayland-fix-AutoMoc-warning.patch
0146-Add-security-tags-to-the-Qt-GraphicsView-framework.patch
0147-Use-angle-bracket-include-style-in-public-headers.patch
0148-tst_selftests-make-generate.sh-work-in-checkouts-wit.patch
0149-QUnicodeTables-abstract-access-to-Properties-cases.patch
0150-QUnicodeTables-remove-wasm-64-packing-trick.patch
0151-CMake-Handle-library-names-like-libavformat.a-in-.pr.patch
0152-Make-no-ssl-configuration-option-do-its-work.patch
0153-QFuture-allow-implicit-conversion-from-QFuture-T-to-.patch
0157-Android-call-view-s-onApplyWindowInsets-in-QtInputDe.patch
0160-QLockFile-bypass-QFile-remove-and-go-straight-to-the.patch
0161-QLockFile-Win-replace-DeleteFile-with-CreateFile-w-o.patch
0162-Add-security-tags-to-the-Qt-Widgets-styles-including.patch
0163-Coin-Add-update-repo-instructions.patch
0164-QTimer-Doc-Distribute-existing-note-to-useful-places.patch
0165-QLockFile-inline-getLockFileHandle-so-it-s-not-in-th.patch
0166-QFSFileEngine-remove-unused-open-overloads.patch
0167-CRA-review-src-widgets-effects.patch
0168-CRA-review-src-widgets-kernel-qsizepolicy.patch
0169-macdeployqt-Update-referenced-documentation-page.patch
0170-CMake-Fix-non-PCH-build-of-Qt-for-WebAssembly.patch
0171-CMake-Handle-TARGET_SUPPORTS_SHARED_LIBS-for-Emscrip.patch
0173-QList-check-that-freeSpaceAtBegin-eventually-shrinks.patch
0174-QDecompressHelper-export-class-for-private-usage.patch
0175-Add-security-headers-for-src-gui-tools.patch
0176-Mark-qregularexpression.h-as-security-significant.patch
0178-Mark-QStringList-as-security-significant-default.patch
0180-QWidget-fix-propagating-style-with-descendant-select.patch
0181-QWindowsVistaAnimation-adjust-painting-of-the-animat.patch
0182-QToolButton-always-set-to-MenuButtonPopup-when-actio.patch
0183-Mark-qstringalgorithms-headers-as-security-critical.patch
0186-CMake-Opt-in-for-NEW-CMP0156-on-WebAssembly.patch
0187-CRA-review-src-widgets-kernel.patch
0188-CRA-review-src-widgets-kernel-qwidget.patch
0190-wasm-remove-wasm-jspi-memory-limit-workaround.patch
0191-Mark-qdoublescanprint_p.h-as-security-critical.patch
0192-wasm-set-max-memory-to-16GB-for-wasm64.patch
0193-Fix-test-compilation-with-QT_NO_WIDGETS.patch
0194-CRA-review-src-widgets-kernel-qapplication.patch
0195-Windows11Style-don-t-draw-non-editable-QComboBox-as-.patch
0196-QWindows11Style-Handle-inverted-sliders-correctly.patch
0197-CMake-add-inclusion-guards-for-generated-feature-inc.patch
0198-CRA-review-gui-platform-unix-dbusmenu.patch
0199-CRA-review-gui-platform-unix-dbustray.patch
0200-CRA-review-gui-platform-unix.patch
0201-CRA-review-plugins-platforms-xcb.patch
0202-Thread-QResultStore-silence-Wunnecessary-virtual-spe.patch
0204-platforms-windows-remove-unused-private-field.patch
0205-AndroidTestRunner-don-t-print-crashes-by-default.patch
0206-Mark-qbytedata_p.h-as-security-critical.patch
0207-Add-security-headers-for-src-printsupport.patch
0209-Add-some-benchmarks-of-QLocale-number-parsing-with-s.patch
0210-Enable-NPOTT-features-for-OpenGL-ES-3.patch
0211-wasm-fix-memory-corruption-in-Promise-handling.patch
0212-QMacStyle-Draw-disclosure-triangles-according-to-cor.patch
0213-cmake-adjust-c-standards-for-headers-clean.patch
0214-WindowsQPA-Remove-unused-GDIPlus-include-from-qwindo.patch
0215-Add-note-to-the-setWindowFlag-to-reflect-known-effec.patch
0216-CRA-review-plugins-platforminputcontexts.patch
0217-Mark-QUnicodeTables-as-security-significant-default.patch
0218-Mark-Unicode-data-explicitly-not-security-critical.patch
0219-Mark-QUnicodeTools-as-security-critical.patch
0220-Mark-QStringBuilder-as-security-critical.patch
0221-Mark-qformat_impl.h-as-security-significant.patch
0222-Http2-Remove-version-header-handling.patch
0223-tst_http2-goaway-Test-for-expected-error.patch
0224-SKIP-three-qRhi-cases-in-Android-16.patch
0225-Core-Make-retrieveElement-semi-public-and-inline.patch
0226-Doc-Remove-duplicate-see-also-links.patch
0227-Revert-QObject-clarify-what-method-is-in-string-base.patch
0228-Doc-Fix-broken-see-also-links.patch
0229-Doc-Fix-self-linking-see-also-link.patch
0230-QWindows11Style-Rework-animation-logic-and-add-guard.patch
0231-QNetworkInfo-glib-better-support-for-netlink-backend.patch
0232-QRM-fix-Waddress-Wnonnull-compare-warnings-from-gcc.patch
0233-Fix-Android-builds-with-QT_FORCE_BUILD_TOOLS-ON.patch
0234-Android-change-only-the-opacity-of-system-bars-when-.patch
0235-Android-call-handleUiModeChange-only-when-the-uiMode.patch
0236-Android-read-and-apply-theme-s-values-on-handUiModeC.patch
0237-Android-set-system-bars-colors-when-Qt-color-scheme-.patch
0238-QDBusReply-remove-pointless-non-const-error-overload.patch
0239-QDBusReply-apply-Rule-Of-Zero.patch
0241-qtestcase.h-fix-Wconversion-warnings-from-std-chrono.patch
0242-Fix-duplicate-test-data-tag-warningsin-tst_QVariant.patch
0243-Mark-QVariant-as-security-critical.patch
0244-Windows11Style-Fix-QSlider-painting.patch
0245-Windows11Style-don-t-try-to-draw-an-icon-when-the-re.patch
0246-Android-SKIP-tst_QRhiWidget-simple-OpenGL-on-Android.patch
0247-Port-tst_QWinRegistryKey-away-from-QPair.patch
0248-QWinRegistryKey-don-t-use-qSwap.patch
0249-QWinRegistryKey-remove-unused-qpair.h-include.patch
0250-QSysInfo-don-t-pass-QStringLiteral-to-QWinRegistryKe.patch
0251-Add-QCoreTextFontEngine-glyphCount-override.patch
0252-wasm-work-around-wasm64-stringToUTF16-issue.patch
0253-tst_QDateTimeEdit-stepModifierButtons-make-format-ov.patch
0254-Extract-the-content-type-parser-from-qrestreply.cpp.patch
0255-Android-guard-platform-plugin-egl-code-behind-QT_CON.patch
0258-Core-resolve-circular-dependencies-between-qstring.h.patch
0259-QStringView-remove-unused-header.patch
0260-tst_QObject-add-tests-for-string-based-connect-for-i.patch
0261-CRA-review-plugins-platforms-bsdfb.patch
0262-CRA-review-plugins-platforms-directfb.patch
0263-CRA-review-plugins-platforms-minimal.patch
0264-Fix-source-compatibility-of-QTRY_LOOP_IMPL.patch
0265-initialize-ch-to-avoid-uninitialized-variable-warnin.patch
0266-QtContentTypeParser-mark-parse_content_type-inline.patch
0267-tracepointgen-Add-file-path-to-include-directories.patch
0268-QXcbIntegration-remove-duplicate-Qt-StringLiterals-i.patch
0269-QWinRegistryKey-fix-buffer-overflow-in-ctor-and-valu.patch
0270-Do-include-QtNetwork-qhostaddress.h-from-qabstractso.patch
0271-QAbstractSocket-QHostAddress-ensure-definition-of-st.patch
0272-Add-syncqt-headers-to-tracepointgen-dependencies.patch
0273-Tracepointgen-Fix-dash-in-include-regex.patch
0274-docs-Qt-StringLiterals-improve-phrasing.patch
0275-docs-Prefer-Qt-StringLiterals-over-Qt-Literals-Strin.patch
0277-util-unicode-format-debug-messages-as-relative-path-.patch
0278-util-unicode-DRY-terminating-when-unable-to-open-a-f.patch
0279-util-unicode-use-prinft-style-syntax-with-qDebug.patch
0280-Android-Update-to-Gradle-8.14.3.patch
0281-QTreeView-fix-calculating-ViewItemPosition-when-firs.patch
0282-QWidgetAnimator-make-sure-to-remove-all-destroyed-an.patch
0283-QRM-don-t-return-pointer-to-const-from-parentRow.patch
0284-qdatetime-reject-2-digit-years-as-invalid-in-rfc2822.patch
0285-xcb-QXcbDrag-avoid-excessive-calls-to-currentDrag.patch
0286-CMake-Handle-internal-modules-in-qt_internal_wrap_pr.patch
0287-Doc-Mark-QCoreApplicationPrivate-removePostedEvents-.patch
0288-qt-testrunner-detect-test-filename-for-androidtestru.patch
0289-Windows11Style-fix-coloring-mdi-subwindow-buttons.patch
0290-QAbstractSocket-QHostAddress-ensure-definition-of-st.patch
0291-QHostAddress-drop-the-Private-constructor-by-using-N.patch
0292-QRM-explicitly-test-no-op-operations-for-moveRows-Co.patch
0293-Update-contrastPreference-correctly-on-Android.patch
0294-Windows11Style-simplify-CE_ProgressBarContents-paint.patch
0295-Windows11Style-Don-t-set-palette-for-QGraphicsView-i.patch
0296-Network-connection-monitor-fix-races-protect-against.patch
0297-QtGui-doc-Add-alt-text-for-image-tags.patch
0298-Doc-Extend-example-on-QT_DEPLOY_QML_DIR-documentatio.patch
0299-Doc-Document-qt_generate_deploy_script-.-NO_PLUGINS.patch
0300-Windows-with-D3D-Guard-vsync-update-deliveries-more.patch
0301-Expand-QRhiWidget-color-buffer-size-docs.patch
0302-rhi-d3d12-Fix-primitive-restart.patch
0303-Use-size-of-largest-representation-as-NSImage-size-i.patch
0305-macOS-Apply-icon-tint-color-without-intermediate-dra.patch
0306-macOS-Use-SF-Symbols-chevrons-for-toolbar-extension-.patch
0307-Remove-unused-function-from-tst_QNetworkProxyFactory.patch
0308-Wayland-handle-delayed-CSD-creation-following-decora.patch
0309-Fix-getting-color-scheme-in-x-d-p-platform-theme.patch
0310-Fix-tst_QGraphicsProxyWidget-wheelEventPropagation-t.patch
0311-Core-Decouple-QIterable-from-QMetaContainer.patch
0312-Fix-Qt-Designer-startup-crash-when-restoring-main-wi.patch
0313-Silence-NewDeleteLeaks-warning-for-QMetaObject-invok.patch
0314-Windows-QPA-Fix-flicker-when-moving-Windows-with-Hig.patch
0315-corelib-fix-clang-narrowing-conversion-warnings-Wsho.patch
0316-QObject-take-by-QSpan-in-static-helper-function.patch
0317-QObject-fix-Clang-Wshorten-64-to-32-warnings.patch
0318-QLogging-fix-narrowing-conversion-assert.patch
0319-tests-auto-network-port-away-from-QPair.patch
0320-qiostextinputoverlay-plugin-port-away-from-QPair.patch
0321-QObject-use-a-view-instead-of-allocating-a-temporary.patch
0322-QString-fix-overly-eager-arg-int-ish-overload.patch
0323-cmake-enable-msvc_obj_debug_info-when-using-a-compil.patch
0324-Android-Add-support-for-GET_EXTRACTED_TEXT_MONITOR.patch
0325-QPdf-Consider-devicePixelRatio-in-alphalessImage-in-.patch
0327-CMake-Call-source_group-Resources-for-qt_add_resourc.patch
0328-Fix-scrolling-of-QTableWidget-within-QGraphicsView.patch
0329-Handle-subsurfaces-with-scaling-correctly.patch
0330-Revert-QAbstractSocket-QHostAddress-ensure-definitio.patch
0331-QAbstractSocketPrivate-add-QNetworkInterface-paramet.patch
0332-Make-rectfill-consistent-for-RGBx8888.patch
0333-QNativeSocketEngine-enable-dual-stack-as-early-as-po.patch
0334-Properly-set-ReceivePacketInformation-socket-option-.patch
0335-Allow-binding-a-socket-to-a-specific-QNetworkInterfa.patch
0336-QWidget-initPainter-remove-unnecessary-const_cast.patch
0337-Only-skip-writeback-conversion-for-RGBx64-on-opaque-.patch
0338-Make-QImage-pixelColor-and-QImage-pixel-consistent.patch
0339-QFileSystemModel-remove-qpair.h-include.patch
0340-Doc-Add-alternate-text-for-Qt-Widgets-images.patch
0341-QWindowsWindow-requestUpdate-fix-use-after-free.patch
0342-tst_QAccessibility-port-away-from-QPair.patch
0343-QFactoryLoader-fix-clang-Wshorten-64-to-32-warnings.patch
0344-tests-auto-dbus-port-away-from-QPair.patch
0345-Http2-Relay-an-error-for-GOAWAY-with-NO_ERROR.patch
0346-tst_QObject-port-away-from-QPair.patch
0347-tests-auto-itemmodels-port-away-from-QPair.patch
0348-tst_QXmlStream-port-away-from-QPair.patch
0349-tst_QJson-port-away-from-QPair.patch
0350-tst_QArrayData-port-away-from-QPair.patch
0351-tst_QString-port-away-from-QPair.patch
0352-tst_QMap-port-away-from-QPair.patch
0353-tst_QHashFunctions-port-away-from-QPair.patch
0354-tst_Moc-port-away-from-QPair.patch
0355-macdeployqt-Use-canonical-name.patch
0356-tests-auto-widgets-graphicsview-port-away-from-QPair.patch
0357-tst_QurlQuery-port-away-from-QPair.patch
0358-tst_QDir-port-away-from-QPair.patch
0359-tst_QPlainTextEdit-port-away-from-QPair.patch
0360-tst_QTextEdit-port-away-from-QPair.patch
0361-tests-auto-widgets-port-away-from-QPair.patch
0362-Fix-crash-when-trying-to-register-.rcc-from-resource.patch
0363-Fix-documentation-for-QPrinter-PrinterResolution.patch
0364-QNativeSocketEngine-read-Only-treat-readBytes-0-as-a.patch
0365-Teach-QNativeSocketEnginePrivate-fetchConnectionPara.patch
0366-Add-missing-nullptr-guard-to-QTextStreamPrivate-setu.patch
0367-Fix-RGB32-to-RGBxFP-writeback-and-fix-blend-fallback.patch
0368-QDesktopUnixServices-Register-with-host-app-registry.patch
0369-Fix-artifacts-on-distance-fields-with-overlapping-li.patch
0370-Add-tst_QPainter-test-for-drawing-to-image-formats-w.patch
0371-Pass-though-size-correctly-in-NSImage-imageFromQIcon.patch
0372-QCocoaTheme-Resolve-folder-icons-via-NSWorkspace.patch
0373-wayland-Fix-subsurface-buffers-outliving-the-backing.patch
0374-Allow-non-square-size-requests-to-NSImage-imageFromQ.patch
0375-Don-t-override-NSImage-aspect-ratio-in-NSImage-image.patch
0376-QRM-don-t-overwrite-table-row-when-setting-cell-with.patch
0377-QTabBar-Set-style-sheet-style-as-the-proxy-for-the-b.patch
0378-Fix-QLineEdit-frame-color-when-using-gradient-style-.patch
0379-QApplication-avoid-conversion-from-to-QPoint-F.patch
0380-QUndoStack-Notify-changes-when-the-command-is-obsole.patch
0381-QWizard-make-QWizardHeader-a-bit-more-safe.patch
0382-QWizardHeader-mark-the-ctors-explicit.patch
0383-QMacStyle-fix-push-button-s-title-margins-for-small-.patch
0384-Add-security-headers-to-qtbase-src-widgets-widgets.patch
0385-QToolButton-don-t-override-user-set-popup-mode.patch
0386-Fix-crash-in-QWidgetWindow-handleMouseEvent.patch
0387-Windows11Style-replace-unicode-code-points-with-read.patch
0388-QApplication-use-range-based-for-loops-when-possible.patch
0389-QIconLoader-use-range-based-for-loops-where-possible.patch
0390-QAbstractItemView-Fix-isPersistentEditorOpen-for-non.patch
0391-Android-fix-QtQuickView-fields-access-level.patch
0392-macOS-Make-macos-26-arm64-tests-significant-blocking.patch
0393-Doc-Add-more-info-to-QThread-requestInterruption.patch
0394-iOS-Fix-mangling-usage-of-QUIView-in-qioswindow.h.patch
0395-iOS-Fix-namespace-mangling-usage-in-qiosplatformacce.patch
0396-appendNodeText-Don-t-split-emojis-with-surrogate-cha.patch
0397-iOS-Add-missing-header-guards.patch
0398-Windows11Style-Fix-progressbar-label-drawing.patch
0399-Android-don-t-check-keyboard-visibility-in-hasValidF.patch
0400-Doc-Fix-instructions-on-how-to-use-GuiPrivate.patch
0401-QObject-docs-clarify-that-window-system-events-means.patch
0402-CMake-fix-CMP0177-warning-under-qt_internal_create_s.patch
0403-Mark-qcbor-map-array-.cpp-as-security-critical.patch
0404-Mark-qcborcommon_p.h-as-security-critical.patch
0405-Mark-the-remaining-cbor-json-headers-as-security-sig.patch
0406-Mark-QWinRegistryKey-as-security-critical.patch
0407-QWinRegistryKey-disable-moves-and-swap.patch
0408-QWinRegistryKey-de-pessimize-stringValue.patch
0410-Doc-Clarify-usage-of-QTextFormat-FontSizeAdjustment.patch
0411-Doc-Fix-instructions-on-how-to-use-CorePrivate.patch
0412-QUndoStack-use-idiomatic-relational-operators.patch
0413-QUndoStack-fix-two-Coverity-COPY_INSTEAD_OF_MOVE-war.patch
0414-Mark-string-collation-classes-as-security-critical.patch
0415-Mark-remaining-corelib-text-.qdoc-files-are-insignif.patch
0416-HTTP-Adjust-tests-to-handle-or-ignore-header-case.patch
0417-docs-Discourage-using-namespace-Qt.patch
0418-tests-auto-gui-port-away-from-QPair.patch
0420-Prefer-using-namespace-Qt-StringLiterals.patch
0421-QMacStyle-set-NSStepperCell-s-control-size-to-mini.patch
0422-CMake-Relax-handling-of-CMP0156-policy.patch
0423-Doc-Create-a-group-topic-for-listing-user-input-exam.patch
0424-Doc-Fix-CMake-snippet-on-how-to-import-Qt6-Private.patch
0425-QMenu-Do-not-close-menu-when-seperator-was-clicked.patch
0426-Fix-implicit-integer-conversion-loses-build-error-on.patch
0427-Schannel-encode-the-peer-name-for-SNI.patch
0428-Windows-Fix-QWindowWindows-requestUpdate.patch
0429-QJsonParseError-fix-clang-Wshorten-64-to-32-warnings.patch
0430-Avoid-float-rounding-errors-in-QDashStroker.patch
0431-QNativeSocketEnginePrivate-setOption-simplify-ugly-p.patch
0432-QApplication-reset-WA_KeyboardFocusChange-on-focus-c.patch
0433-Adapt-to-reuse-version-6.patch
0434-Doc-Fix-broken-link-to-the-Sinclair-ZX-Spectrum.patch
0435-QCborValue-rewrite-nextUtf32Character-to-avoid-narro.patch
0436-QChar-avoid-char-32-16-_t-narrowing-in-de-composeHel.patch
0437-QChar-fix-the-signature-of-foldCase-char32_t-char32_.patch
0438-QChar-avoid-char-32-16-_t-narrowing-in-foldCase-char.patch
0439-QChar-remove-confusing-foldCase-ch-ch-overload.patch
0440-QChar-avoid-char-32-16-_t-narrowing-in-normalization.patch
0441-QChar-scope-variables-tigher-in-canonicalOrderHelper.patch
0442-QChar-avoid-char-32-16-_t-narrowing-in-canonicalOrde.patch
0443-Brush-up-the-Widget-gallery-example.patch
0444-QCryptographicHash-hashInto-write-directly-into-the-.patch
0445-tst_QSettings-split-the-testEscapes-test-espcapedKey.patch
0446-tst_QSettings-split-the-testEscapes-test-unescapedKe.patch
0447-QMetaObjectBuilder-Fix-detecting-enum-properties-fro.patch
0448-Testlib-disable-App-Nap-for-whole-execution-of-the-t.patch
0449-tst_QSettings-split-the-testEscapes-test-testEscaped.patch
0450-tst_QSettings-split-the-testEscapes-test-testunEscap.patch
0451-Widget-gallery-example-Output-platform.patch
0452-Suppress-Clang-21-Wcharacter-conversion.patch
0453-qalloc.h-add-missing-cstdlib-include.patch
0454-Fix-alpha-value-after-to-FP16-conversions-on-AVX2.patch
0455-wasm-a11y-Fix-warning-about-aria-hidden.patch
0456-QSemaphore-stub-out-tryAcquire-for-no-thread.patch
0457-QChar-fix-Clang-21-Wcharacter-conversion-warnings.patch
0458-QMdiSubWindow-Respect-null-icon-setting-on-Mac.patch
0459-a11y-Android-Use-RANGE_TYPE_PERCENT-for-RangeInfo-of.patch
0460-CMake-Refactor-AUTOGEN-and-metatypes-path-functions.patch
0461-CMake-Use-only-working-VS-generators-for-qt_add_ui-t.patch
0462-CMake-Set-CMAKE_POLICY_VERSION_MINIMUM-with-older-An.patch
0463-CMake-Add-more-compiler-linker-identification-info.patch
0464-Doc-Remove-references-to-Qt-4-books.patch
0465-QPainterPath-Avoid-division-by-zero-in-AtPercent.patch
0466-Windows11Style-fix-drawing-disabled-checked-QRadioBu.patch
0467-QStyleSheetStyle-don-t-draw-SC_SliderGroove-when-not.patch
0468-tst_qtjson-Increase-stack-size-when-run-with-ASan.patch
0469-test-tst_QResourceEngine-clean-up-registerNestedRccF.patch
0470-Tests-qhash-clear-global-variable-use-in-stdHashImpl.patch
0471-Tests-tst_QScopeGuard-clear-global-state-before-each.patch
0472-tests-tst_QProcessEnvironment-allow-test-to-run-with.patch
0473-Test-timer-initialize-static-singleshot-timer-in-ini.patch
0474-QAbstractItemView-Fix-using-declaration-of-update.patch
0475-Docs-Fix-QAndroidNativeInterface-doc-bug.patch
0476-QList-assign-optimize-for-empty-std-initializer_list.patch
0477-tst_QList-call-the-two-arg-qHash-function.patch
0478-tst_QList-add-and-test-NoexceptMovable.patch
0479-Long-live-Q_PRESUME.patch
0480-QTimeZone-remove-remnant-of-QSharedDataPointer-QTime.patch
0481-QObject-use-connectWarning-more.patch
0482-QHostAddress-clear-the-scopeId-too.patch
0483-QObjectPrivate-connectImpl-remove-unnecessary-check-.patch
0484-tst_QHostAddress-extend-qHash-testing.patch
0485-wasm-Set-input-field-size-to-1x1.patch
0486-test-function_ref-fix-repeated-test-invocation.patch
0487-Remove-unused-header-from-qnetworkinformation.cpp.patch
0488-Android-bump-Android-target-API-level-to-36.patch
0489-Android-update-Android-16-and-SDK-36-to-docs.patch
0491-Fix-nullptr-deref-in-QMenu-mouseReleaseEvent.patch
0492-tst_QDirListing-pre-sort-two-expected-QStringListS.patch
0493-tst_QDirListing-de-duplicate-hidden-files-dirs-test-.patch
0494-QFileSystemEngine-Unix-work-around-copy_file_range-r.patch
0495-QSaveFile-remove-QT_NO_QOBJECT-support.patch
0496-util-unicode-xkbdatagen-fix-build-with-REUSE-IgnoreS.patch
0497-Fix-off-by-one-in-QUnicodeTools-getWhiteSpaces.patch
0498-Remove-redundant-calls-in-tst_QWindow-enterLeaveOnWi.patch
0499-Remove-redundant-calls-in-tst_QFocusEvent-to-request.patch
0500-Core-Add-documentation-for-QMetaAssociation.patch
0501-Core-Move-QMetaSequence-docs-and-implementation-to-o.patch
0502-QStringIterator-add-nextOrRawCodeUnit.patch
0503-QUnicodeTools-improve-variable-allocation-in-getWord.patch
0504-QUnicodeTools-improve-variable-allocation-in-getSent.patch
0505-QUnicodeTools-fix-weird-variable-assignment-in-initS.patch
0506-tst_qgraphicsview-Make-testdata-names-unique.patch
0507-QLockFile-add-some-missing-std-move-s.patch
0508-QUnicodeTools-prefer-lineBreakClass-convenience-func.patch
0509-Windows11-Don-t-force-highlightedText-to-be-windowTe.patch
0510-macOS-Map-function-keys-by-their-virtual-key-code-no.patch
0511-Update-and-expand-Apple-icon-engine-mappings.patch
0512-iOS-Guard-QIOSDocumentPickerController-outliving-QIO.patch
0513-Disable-position-resize-Automatic-on-first-expose.patch
0514-macOS-Only-set-nameFieldStringValue-for-NSSavePanel.patch
0515-QUnicodeTools-port-some-functions-to-QStringIterator.patch
0516-QUnicodeTools-don-t-look-up-surrogate-line-break-pro.patch
0517-QUnicodeTools-port-initScripts-to-QStringIterator.patch
0518-gui-rhi-vulkan-use-VK_COLOR_SPACE_PASS_THROUGH_EXT-o.patch
0519-Titlecase-HTTP-1-headers.patch
0520-Android-Fix-double-emission-of-certain-a11y-events.patch
0521-QTest-include-chrono-instead-of-relying-on-transitiv.patch
0522-Windows11Style-use-assetFont-from-WindowsVistaPrivat.patch
0523-tests-build-qrangemodel-test-only-if-Gui-is-availabl.patch
0524-doc-QRangeModel-Fix-link-to-C-tuple-protocol-in-Tree.patch
0525-QGraphicsView-tests-fix-unittests-for-windows-style.patch
0526-QXcbAtom-add-missing-cstdlib-include.patch
0527-tst_Collections-fix-Clang-Wuninitialized-const-point.patch
0528-Windows11Style-adjust-QPushButton-geometry.patch
0529-QWindows11Style-Fix-menu-item-checkmark-icon-paintin.patch
0530-Windows11Style-fix-QMenuBar-highlighting.patch
0531-Windows11Style-don-t-crop-checkbox-with-no-text.patch
0532-Test-QParallelAnimationGroup-increase-timeout.patch
0533-tst_QHeaderView-remove-unused-static-istr.patch
0535-Don-t-claim-that-PCRE2-is-optional.patch
0536-QUnicodeTables-separate-Properties-cases-from-the-re.patch
0537-Windows11Style-draw-pushbutton-menu-in-CE_PushButton.patch
0538-a11y-Don-t-assert-on-text-existing-before-index.patch
0539-a11y-Fix-name-in-qAccessibleTextBoundaryHelper-doc.patch
0540-a11y-Prevent-infinite-loop-in-QAccessibleTextInterfa.patch
0541-QUnicodeTools-port-getSentenceBreaks-to-QStringItera.patch
0542-QUnicodeTools-port-getWordBreaks-to-QStringIterator.patch
0543-tst_QVariant-fix-Clang-Wunused-const-variable.patch
0544-QString-document-how-to-implement-the-2024-German-ru.patch
0545-QLibrary-expose-QLibraryPrivate-unload-to-autotests.patch
0546-Fix-native-a11y-role-of-QAccessible-LayeredPane.patch
0547-Windows11Style-adjust-QComboBox-dropdown-indicator-g.patch
0548-Windows11Style-draw-indicator-for-current-selected-i.patch
0549-QDataStream-remove-description-from-Version-enum-val.patch
0550-CMake-Fix-order-of-Qt6-AdditionalTargetInfo.cmake-fi.patch
0551-QTimer-fix-clang-Wshorten-64-to-32-warnings.patch
0552-Add-note-about-limitations-of-permission-API-types.patch
0553-QFontPrivate-properly-delete-the-assignment-operator.patch

%description
Version %{qtmajor} of the Qt framework

%define extra_files_Core \
%{_sysconfdir}/ld.so.conf.d/*.conf

%define extra_devel_files_Core \
%{_qtdir}/bin/qt-configure-module \
%dir %{_qtdir}/libexec \
%{_qtdir}/libexec/moc \
%{_qtdir}/libexec/rcc \
%dir %{_qtdir}/metatypes \
%dir %{_qtdir}/modules \
%{_libdir}/pkgconfig/Qt6Platform.pc \
%{_qtdir}/lib/pkgconfig

%define extra_devel_reqprov_Core \
Requires: %{name}-tools = %{EVRD} \
Requires: qmake-qt%{qtmajor} = %{EVRD} \
Requires: cmake(Qt6)

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
%{_qtdir}/libexec/qt-testrunner.py \
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

%define extra_devel_files_ExampleIcons \
%{_qtdir}/lib/objects-RelWithDebInfo/ExampleIconsPrivate_resources_1 \
%{_qtdir}/mkspecs/modules/qt_lib_example_icons_private.pri

%qt6libs Core Concurrent DBus EglFSDeviceIntegration EglFsKmsSupport EglFsKmsGbmSupport Gui Network OpenGL OpenGLWidgets PrintSupport Sql Test WaylandClient WlShellIntegration Widgets XcbQpa Xml
%qt6staticlibs DeviceDiscoverySupport ExamplesAssetDownloader FbSupport ExampleIcons InputSupport KmsSupport

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
%{_qtdir}/mkspecs/modules/README
%{_qtdir}/libexec/qt-internal-configure-examples
%{_qtdir}/libexec/qt-internal-configure-tests
%{_qtdir}/libexec/ensure_pro_file.cmake

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
%{_qtdir}/libexec/qlalr
%{_qtdir}/libexec/qt-android-runner.py
%{_qtdir}/bin/qtpaths
%{_qtdir}/bin/qtpaths%{qtmajor}
%{_qtdir}/libexec/qvkgen
%{_qtdir}/libexec/tracegen
%{_qtdir}/libexec/sanitizer-testrunner.py
%{_qtdir}/libexec/syncqt
%{_qtdir}/libexec/tracepointgen
%{_qtdir}/sbom

%prep
%autosetup -p1 -n qtbase%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}

sed -i -e 's,@QTDIR@,%{_qtdir},g' src/gui/kernel/qguiapplication.cpp

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
	-DQT_WILL_INSTALL:BOOL=ON \
	-DBUILD_WITH_PCH:BOOL=OFF

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
