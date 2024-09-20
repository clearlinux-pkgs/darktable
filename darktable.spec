#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x18DCA123F949BD3B (pascal@obry.net)
#
Name     : darktable
Version  : 4.8.1
Release  : 92
URL      : https://github.com/darktable-org/darktable/releases/download/release-4.8.1/darktable-4.8.1.tar.xz
Source0  : https://github.com/darktable-org/darktable/releases/download/release-4.8.1/darktable-4.8.1.tar.xz
Source1  : https://github.com/darktable-org/rawspeed/archive/200bfa7408cedeac340eea86570fb633831acf7c/rawspeed-200bfa7408cedeac340eea86570fb633831acf7c.tar.gz
Source2  : https://github.com/darktable-org/darktable/releases/download/release-4.8.1/darktable-4.8.1.tar.xz.asc
Source3  : 18DCA123F949BD3B.pkey
Summary  : A virtual Lighttable and Darkroom
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause-FreeBSD BSD-3-Clause CDDL-1.0 GPL-3.0 GPL-3.0+ LGPL-2.1 MIT WTFPL
Requires: iso-codes
BuildRequires : Imath-dev
BuildRequires : SDL2-dev
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : cmocka-dev
BuildRequires : colord-dev
BuildRequires : cups-dev
BuildRequires : curl-dev
BuildRequires : desktop-file-utils
BuildRequires : doxygen
BuildRequires : exiv2-dev
BuildRequires : expat-dev
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : gettext-dev
BuildRequires : glib-dev
BuildRequires : glibc-dev
BuildRequires : gnupg
BuildRequires : gtk3-dev
BuildRequires : icu4c-dev
BuildRequires : intltool
BuildRequires : json-glib-dev
BuildRequires : lcms2-dev
BuildRequires : lensfun-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libavif-dev
BuildRequires : libffi-dev
BuildRequires : libgphoto2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : librsvg-dev
BuildRequires : libsoup-dev
BuildRequires : libwebp-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : lua-dev
BuildRequires : ncurses-data
BuildRequires : ocl-icd-dev
BuildRequires : opencl-headers-dev
BuildRequires : openjpeg
BuildRequires : openjpeg-dev
BuildRequires : openjpeg-staticdev
BuildRequires : osm-gps-map-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config
BuildRequires : pkgconfig(MagickWand)
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(colord-gtk)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libgphoto2)
BuildRequires : pkgconfig(libgphoto2_port)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(portmidi)
BuildRequires : po4a
BuildRequires : portmidi-dev
BuildRequires : pugixml-dev
BuildRequires : python3-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev
Patch1: default-fpmath.patch

%description
darktable is a virtual lighttable and darkroom for photographers: it manages
your digital negatives in a database and lets you view them through a zoomable
lighttable. it also enables you to develop raw images and enhance them.

%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE3}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE2} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 18DCA123F949BD3B' gpg.status
%setup -q -n darktable-4.8.1
cd %{_builddir}
tar xf %{_sourcedir}/rawspeed-200bfa7408cedeac340eea86570fb633831acf7c.tar.gz
cd %{_builddir}/darktable-4.8.1
mkdir -p src/external/rawspeed
cp -r %{_builddir}/rawspeed-200bfa7408cedeac340eea86570fb633831acf7c/* %{_builddir}/darktable-4.8.1/src/external/rawspeed
%patch -P 1 -p1
pushd ..
cp -a darktable-4.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724196157
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo \
-DDONT_USE_INTERNAL_LUA=Off \
-DBINARY_PACKAGE_BUILD=ON \
-DRAWSPEED_ENABLE_LTO=ON \
-DDONT_USE_INTERNAL_LIBRAW=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo \
-DDONT_USE_INTERNAL_LUA=Off \
-DBINARY_PACKAGE_BUILD=ON \
-DRAWSPEED_ENABLE_LTO=ON \
-DDONT_USE_INTERNAL_LIBRAW=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fno-lto -fno-semantic-interposition "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724196157
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/darktable
cp %{_builddir}/darktable-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/darktable/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/darktable-%{version}/data/pswp/LICENSE %{buildroot}/usr/share/package-licenses/darktable/d9f41c058914394e203adb253057643e047576a3 || :
cp %{_builddir}/darktable-%{version}/src/external/LibRaw-cmake/LICENSE %{buildroot}/usr/share/package-licenses/darktable/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/darktable-%{version}/src/external/LibRaw/LICENSE.CDDL %{buildroot}/usr/share/package-licenses/darktable/c24b9c7ef03687bf0141f85a1b7ed81459944c3c || :
cp %{_builddir}/darktable-%{version}/src/external/LibRaw/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/darktable/39a21f33cadea18adcc23bf808d7d5ea6419c8b1 || :
cp %{_builddir}/darktable-%{version}/src/external/LuaAutoC/LICENSE.md %{buildroot}/usr/share/package-licenses/darktable/6baddc7988322d021a187ff7d1d0fb9e2a784e20 || :
cp %{_builddir}/darktable-%{version}/src/external/OpenCL/LICENSE %{buildroot}/usr/share/package-licenses/darktable/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/darktable-%{version}/src/external/libxcf/LICENSE %{buildroot}/usr/share/package-licenses/darktable/fc356b2c50a063b663cc14dde29bc0ab9e7bec51 || :
cp %{_builddir}/darktable-%{version}/src/external/rawspeed/LICENSE %{buildroot}/usr/share/package-licenses/darktable/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
cp %{_builddir}/darktable-%{version}/src/external/whereami/LICENSE.MIT %{buildroot}/usr/share/package-licenses/darktable/c996ffd4c579d586b7d86e158af6042018c3c422 || :
cp %{_builddir}/darktable-%{version}/src/external/whereami/LICENSE.WTFPLv2 %{buildroot}/usr/share/package-licenses/darktable/75e5bae837deb898dae4cb65c4890b1ab825c6b6 || :
cp %{_builddir}/rawspeed-200bfa7408cedeac340eea86570fb633831acf7c/LICENSE %{buildroot}/usr/share/package-licenses/darktable/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content

ln -s darktable/libdarktable.so %{buildroot}/usr/lib64/libdarktable.so
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
