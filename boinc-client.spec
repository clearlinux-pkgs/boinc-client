#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
#
Name     : boinc-client
Version  : 7.24.1
Release  : 54
URL      : https://github.com/BOINC/boinc/archive/client_release/7.24/7.24.1/boinc-7.24.1.tar.gz
Source0  : https://github.com/BOINC/boinc/archive/client_release/7.24/7.24.1/boinc-7.24.1.tar.gz
Source1  : boinc-client.tmpfiles
Summary  : Compression functions for BOINC applications
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT NCSA OFL-1.1
Requires: boinc-client-bin = %{version}-%{release}
Requires: boinc-client-config = %{version}-%{release}
Requires: boinc-client-data = %{version}-%{release}
Requires: boinc-client-lib = %{version}-%{release}
Requires: boinc-client-license = %{version}-%{release}
Requires: boinc-client-locales = %{version}-%{release}
Requires: boinc-client-man = %{version}-%{release}
Requires: boinc-client-services = %{version}-%{release}
BuildRequires : cups-dev
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : docbook2X
BuildRequires : freeglut-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libaio-dev
BuildRequires : libxslt
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : perl(XML::NamespaceSupport)
BuildRequires : perl(XML::SAX::Exception)
BuildRequires : perl(XML::SAX::ParserFactory)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-atom)
BuildRequires : pkgconfig(xmu)
BuildRequires : sqlite-autoconf-dev
BuildRequires : wxWidgets
BuildRequires : wxWidgets-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-boinc-manager.desktop.patch

%description
Stripchart version 2.0
----------------------
Author: Matt Lebofsky
BOINC/SETI@home - University of California, Berkeley
mattl@ssl.berkeley.edu

%package bin
Summary: bin components for the boinc-client package.
Group: Binaries
Requires: boinc-client-data = %{version}-%{release}
Requires: boinc-client-config = %{version}-%{release}
Requires: boinc-client-license = %{version}-%{release}
Requires: boinc-client-services = %{version}-%{release}

%description bin
bin components for the boinc-client package.


%package config
Summary: config components for the boinc-client package.
Group: Default

%description config
config components for the boinc-client package.


%package data
Summary: data components for the boinc-client package.
Group: Data

%description data
data components for the boinc-client package.


%package dev
Summary: dev components for the boinc-client package.
Group: Development
Requires: boinc-client-lib = %{version}-%{release}
Requires: boinc-client-bin = %{version}-%{release}
Requires: boinc-client-data = %{version}-%{release}
Provides: boinc-client-devel = %{version}-%{release}
Requires: boinc-client = %{version}-%{release}

%description dev
dev components for the boinc-client package.


%package lib
Summary: lib components for the boinc-client package.
Group: Libraries
Requires: boinc-client-data = %{version}-%{release}
Requires: boinc-client-license = %{version}-%{release}

%description lib
lib components for the boinc-client package.


%package license
Summary: license components for the boinc-client package.
Group: Default

%description license
license components for the boinc-client package.


%package locales
Summary: locales components for the boinc-client package.
Group: Default

%description locales
locales components for the boinc-client package.


%package man
Summary: man components for the boinc-client package.
Group: Default

%description man
man components for the boinc-client package.


%package services
Summary: services components for the boinc-client package.
Group: Systemd services
Requires: systemd

%description services
services components for the boinc-client package.


%prep
%setup -q -n boinc-client_release-7.24-7.24.1
cd %{_builddir}/boinc-client_release-7.24-7.24.1
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692026933
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%reconfigure --disable-static DOCBOOK2X_MAN='/usr/bin/db2x_xsltproc -s man $< -o $(patsubst %.xml,%.mxml,$<); db2x_manxml $(patsubst %.xml,%.mxml,$<); echo' \
--disable-silent-rules \
--enable-dynamic-client-linkage \
--disable-server \
--disable-fcgi \
--enable-unicode \
--with-ssl \
--with-x
make  %{?_smp_mflags}  CXXFLAGS+="-DwxNB_FLAT=0x0800 -DwxADJUST_MINSIZE=0x0000"

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1692026933
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/boinc-client
cp %{_builddir}/boinc-client_release-7.24-%{version}/COPYING %{buildroot}/usr/share/package-licenses/boinc-client/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/boinc-client/e203d4ef09d404fa5c03cf6590e44231665be689 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/COPYRIGHT %{buildroot}/usr/share/package-licenses/boinc-client/62512a302b5fc9d3f15ad8ae0775aecbf08f7b4d || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/api/ttf/liberation-fonts-ttf-2.00.0/LICENSE %{buildroot}/usr/share/package-licenses/boinc-client/0898cb73de9283d38e6f4cef45ce79efbfafb0b2 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/all/libraries/ckeditor/samples/toolbarconfigurator/lib/codemirror/LICENSE %{buildroot}/usr/share/package-licenses/boinc-client/4dbb477bdccb1d3b4fc6e73b899d1a287b199f98 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/all/libraries/phpmailer/LICENSE %{buildroot}/usr/share/package-licenses/boinc-client/d156a1bf8185f65cd8b9d3c06fd011428d0214f5 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/all/libraries/tinymce/jscripts/tiny_mce/license.txt %{buildroot}/usr/share/package-licenses/boinc-client/05ce47af4fb5f4f4a65b8f7f0a67e9935ff0ae70 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/all/themes/zen/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/bbcode/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/cck/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/ckeditor/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/content_profile/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/context/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/ctools/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/elysia_cron/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/facetapi/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/features/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/filefield/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/flag/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/forum_access/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/htmlpurifier/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/i18nviews/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/jump/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/panels/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/privatemsg/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/tableofcontents/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/views/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/contrib/wysiwyg/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/drupal/sites/default/boinc/modules/node_comment_block/LICENSE.txt %{buildroot}/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/html/inc/random_compat/LICENSE %{buildroot}/usr/share/package-licenses/boinc-client/89ea22f8eed658271c62456bacc37b24a77173a4 || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/mac_installer/License.rtf %{buildroot}/usr/share/package-licenses/boinc-client/857cfa94afe9fb9b3e73cfb170c1d94155aaf94a || :
cp %{_builddir}/boinc-client_release-7.24-%{version}/samples/wrappture/license.terms %{buildroot}/usr/share/package-licenses/boinc-client/3fad046d74e3ba1138e908e168a325e6a14b8ac0 || :
%make_install
%find_lang BOINC-Client
%find_lang BOINC-Manager
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/boinc-client.conf
## install_append content
install -D -m644 boinc-manager.desktop %{buildroot}/usr/share/applications/boinc-manager.desktop

for fullname in packages/generic/sea/boincmgr.[0-9]*x[0-9]*.png; do
IFS=. read prog res ext <<< $(basename ${fullname})
install -D -m644 "${fullname}" %{buildroot}/usr/share/icons/hicolor/${res}/apps/${prog}.${ext}
done
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/boinc
/usr/bin/boinc_client
/usr/bin/boinccmd
/usr/bin/boincmgr
/usr/bin/boincscr

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/boinc-client.conf

%files data
%defattr(-,root,root,-)
/usr/share/applications/boinc-manager.desktop
/usr/share/applications/boinc.desktop
"/usr/share/boinc-manager/skins/Charity Engine/background_image.png"
"/usr/share/boinc-manager/skins/Charity Engine/ce_about.ico"
"/usr/share/boinc-manager/skins/Charity Engine/ce_icon_play.png"
"/usr/share/boinc-manager/skins/Charity Engine/ce_pause.png"
"/usr/share/boinc-manager/skins/Charity Engine/ce_play.png"
"/usr/share/boinc-manager/skins/Charity Engine/ce_stop.png"
"/usr/share/boinc-manager/skins/Charity Engine/dialog_background_image.png"
"/usr/share/boinc-manager/skins/Charity Engine/project_image.png"
"/usr/share/boinc-manager/skins/Charity Engine/skin.xml"
"/usr/share/boinc-manager/skins/Charity Engine/workunit_running_image.png"
"/usr/share/boinc-manager/skins/Charity Engine/workunit_suspended_image.png"
"/usr/share/boinc-manager/skins/Charity Engine/workunit_waiting_image.png"
/usr/share/boinc-manager/skins/Default/background_image.png
/usr/share/boinc-manager/skins/Default/skin.xml
/usr/share/boinc-manager/skins/Default/workunit_running_image.png
/usr/share/boinc-manager/skins/Default/workunit_suspended_image.png
/usr/share/boinc-manager/skins/Default/workunit_waiting_image.png
/usr/share/boinc-manager/skins/GridRepublic/background_image.png
/usr/share/boinc-manager/skins/GridRepublic/dialog_background_image.png
/usr/share/boinc-manager/skins/GridRepublic/gr_about.ico
/usr/share/boinc-manager/skins/GridRepublic/gr_icon_play.png
/usr/share/boinc-manager/skins/GridRepublic/gr_pause.png
/usr/share/boinc-manager/skins/GridRepublic/gr_play.png
/usr/share/boinc-manager/skins/GridRepublic/gr_stop.png
/usr/share/boinc-manager/skins/GridRepublic/project_image.png
/usr/share/boinc-manager/skins/GridRepublic/skin.xml
/usr/share/boinc-manager/skins/GridRepublic/workunit_running_image.png
/usr/share/boinc-manager/skins/GridRepublic/workunit_suspended_image.png
/usr/share/boinc-manager/skins/GridRepublic/workunit_waiting_image.png
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/advanced_link_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/attach_project_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/cancel_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/close_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/connecting_indicator_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/copy_all_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/copy_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/dialog_background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/error_indicator_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/gauge_bg.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/help_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/left_arrow_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/messages_alert_link_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/messages_link_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/preferences_link_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/project_area_background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/project_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/resume_link_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/right_arrow_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/save_button.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/spacer_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/state_indicator_background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/suspend_link_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/tabArea_bg.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/wcg_about.ico"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/wcg_pause.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/wcg_play.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/wcg_stop.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_active_tab.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_animation_background_image copy.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_animation_background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_area_background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_gauge_background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_gauge_progress_indicator_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_suspended_tab.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/graphic/workunit_tab_area_background_image.png"
"/usr/share/boinc-manager/skins/People for a Smarter Planet/skin.xml"
/usr/share/boinc-manager/skins/ProgressThruProcessors/background_image.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/dialog_background_image.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/project_image.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/ptp_about.ico
/usr/share/boinc-manager/skins/ProgressThruProcessors/ptp_icon_play.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/ptp_pause.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/ptp_play.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/ptp_stop.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/skin.xml
/usr/share/boinc-manager/skins/ProgressThruProcessors/workunit_running_image.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/workunit_suspended_image.png
/usr/share/boinc-manager/skins/ProgressThruProcessors/workunit_waiting_image.png
"/usr/share/boinc-manager/skins/World Community Grid/Green_dot.png"
"/usr/share/boinc-manager/skins/World Community Grid/Red_dot.png"
"/usr/share/boinc-manager/skins/World Community Grid/Yellow_dot.png"
"/usr/share/boinc-manager/skins/World Community Grid/background_image.png"
"/usr/share/boinc-manager/skins/World Community Grid/skin.xml"
"/usr/share/boinc-manager/skins/World Community Grid/wcg.ico"
"/usr/share/boinc-manager/skins/World Community Grid/wcg_32.png"
"/usr/share/boinc-manager/skins/World Community Grid/wcg_50.png"
"/usr/share/boinc-manager/skins/World Community Grid/wcg_about.ico"
"/usr/share/boinc-manager/skins/World Community Grid/wcg_pause.png"
"/usr/share/boinc-manager/skins/World Community Grid/wcg_play.png"
"/usr/share/boinc-manager/skins/World Community Grid/wcg_stop.png"
/usr/share/icons/hicolor/16x16/apps/boincmgr.png
/usr/share/icons/hicolor/32x32/apps/boincmgr.png
/usr/share/icons/hicolor/48x48/apps/boincmgr.png
/usr/share/icons/hicolor/64x64/apps/boinc.png
/usr/share/icons/hicolor/scalable/apps/boinc.svg

%files dev
%defattr(-,root,root,-)
/usr/include/boinc/app_ipc.h
/usr/include/boinc/average.h
/usr/include/boinc/base64.h
/usr/include/boinc/boinc_api.h
/usr/include/boinc/boinc_opencl.h
/usr/include/boinc/boinc_stdio.h
/usr/include/boinc/cal_boinc.h
/usr/include/boinc/cc_config.h
/usr/include/boinc/cert_sig.h
/usr/include/boinc/cl_boinc.h
/usr/include/boinc/common_defs.h
/usr/include/boinc/coproc.h
/usr/include/boinc/crypt.h
/usr/include/boinc/diagnostics.h
/usr/include/boinc/error_numbers.h
/usr/include/boinc/filesys.h
/usr/include/boinc/graphics2.h
/usr/include/boinc/gui_rpc_client.h
/usr/include/boinc/gutil.h
/usr/include/boinc/hostinfo.h
/usr/include/boinc/md5.h
/usr/include/boinc/md5_file.h
/usr/include/boinc/mem_usage.h
/usr/include/boinc/mfile.h
/usr/include/boinc/miofile.h
/usr/include/boinc/msg_log.h
/usr/include/boinc/network.h
/usr/include/boinc/notice.h
/usr/include/boinc/opencl_boinc.h
/usr/include/boinc/parse.h
/usr/include/boinc/prefs.h
/usr/include/boinc/proc_control.h
/usr/include/boinc/procinfo.h
/usr/include/boinc/project_specific_defines.h
/usr/include/boinc/proxy_info.h
/usr/include/boinc/sched_msgs.h
/usr/include/boinc/stackwalker_imports.h
/usr/include/boinc/str_replace.h
/usr/include/boinc/str_util.h
/usr/include/boinc/svn_version.h
/usr/include/boinc/url.h
/usr/include/boinc/util.h
/usr/include/boinc/version.h
/usr/lib64/libboinc_api.so
/usr/lib64/libboinc_opencl.so
/usr/lib64/pkgconfig/libboinc.pc
/usr/lib64/pkgconfig/libboinc_api.pc
/usr/lib64/pkgconfig/libboinc_crypt.pc
/usr/lib64/pkgconfig/libboinc_opencl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libboinc_api.so.7
/usr/lib64/libboinc_api.so.7.24.1
/usr/lib64/libboinc_opencl.so.7
/usr/lib64/libboinc_opencl.so.7.24.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/boinc-client/05ce47af4fb5f4f4a65b8f7f0a67e9935ff0ae70
/usr/share/package-licenses/boinc-client/0898cb73de9283d38e6f4cef45ce79efbfafb0b2
/usr/share/package-licenses/boinc-client/3fad046d74e3ba1138e908e168a325e6a14b8ac0
/usr/share/package-licenses/boinc-client/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/boinc-client/4dbb477bdccb1d3b4fc6e73b899d1a287b199f98
/usr/share/package-licenses/boinc-client/62512a302b5fc9d3f15ad8ae0775aecbf08f7b4d
/usr/share/package-licenses/boinc-client/857cfa94afe9fb9b3e73cfb170c1d94155aaf94a
/usr/share/package-licenses/boinc-client/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/boinc-client/89ea22f8eed658271c62456bacc37b24a77173a4
/usr/share/package-licenses/boinc-client/919ebd0505421520215536126e8dee39fc1ef529
/usr/share/package-licenses/boinc-client/d156a1bf8185f65cd8b9d3c06fd011428d0214f5
/usr/share/package-licenses/boinc-client/e203d4ef09d404fa5c03cf6590e44231665be689

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/boinc.1
/usr/share/man/man1/boinccmd.1
/usr/share/man/man1/boincmgr.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/boinc-client.service

%files locales -f BOINC-Client.lang -f BOINC-Manager.lang
%defattr(-,root,root,-)

