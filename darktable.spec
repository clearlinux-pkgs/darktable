#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x18DCA123F949BD3B (pascal@obry.net)
#
Name     : darktable
Version  : 3.4.1
Release  : 59
URL      : https://github.com/darktable-org/darktable/releases/download/release-3.4.1/darktable-3.4.1.tar.xz
Source0  : https://github.com/darktable-org/darktable/releases/download/release-3.4.1/darktable-3.4.1.tar.xz
Source1  : https://github.com/darktable-org/rawspeed/archive/v3.3.tar.gz
Source2  : https://github.com/darktable-org/darktable/releases/download/release-3.4.1/darktable-3.4.1.tar.xz.asc
Summary  : A virtual Lighttable and Darkroom
Group    : Development/Tools
License  : BSD-2-Clause-FreeBSD GPL-3.0 GPL-3.0+ LGPL-2.1 MIT WTFPL
Requires: darktable-bin = %{version}-%{release}
Requires: darktable-data = %{version}-%{release}
Requires: darktable-lib = %{version}-%{release}
Requires: darktable-license = %{version}-%{release}
Requires: darktable-locales = %{version}-%{release}
Requires: darktable-man = %{version}-%{release}
Requires: iso-codes
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
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : gettext-dev
BuildRequires : glib-dev
BuildRequires : glibc-dev
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : iso-codes
BuildRequires : json-glib-dev
BuildRequires : lcms2-dev
BuildRequires : lensfun-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
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
BuildRequires : ocl-icd-dev
BuildRequires : opencl-headers-dev
BuildRequires : openjpeg
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config
BuildRequires : pkgconfig(MagickWand)
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(colord-gtk)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libgphoto2)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libwebp)
BuildRequires : po4a
BuildRequires : pugixml-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev
Patch1: default-fpmath.patch
Patch2: avx2-libs.patch
Patch3: 0001-Fix-build-with-OpenEXR-3.patch

%description
darktable is a virtual lighttable and darkroom for photographers: it manages 
your digital negatives in a database and lets you view them through a zoomable 
lighttable. it also enables you to develop raw images and enhance them.

%package bin
Summary: bin components for the darktable package.
Group: Binaries
Requires: darktable-data = %{version}-%{release}
Requires: darktable-license = %{version}-%{release}

%description bin
bin components for the darktable package.


%package data
Summary: data components for the darktable package.
Group: Data

%description data
data components for the darktable package.


%package doc
Summary: doc components for the darktable package.
Group: Documentation
Requires: darktable-man = %{version}-%{release}

%description doc
doc components for the darktable package.


%package lib
Summary: lib components for the darktable package.
Group: Libraries
Requires: darktable-data = %{version}-%{release}
Requires: darktable-license = %{version}-%{release}

%description lib
lib components for the darktable package.


%package license
Summary: license components for the darktable package.
Group: Default

%description license
license components for the darktable package.


%package locales
Summary: locales components for the darktable package.
Group: Default

%description locales
locales components for the darktable package.


%package man
Summary: man components for the darktable package.
Group: Default

%description man
man components for the darktable package.


%prep
%setup -q -n darktable-3.4.1
cd %{_builddir}
tar xf %{_sourcedir}/v3.3.tar.gz
cd %{_builddir}/darktable-3.4.1
mkdir -p src/external/rawspeed
cp -r %{_builddir}/rawspeed-3.3/* %{_builddir}/darktable-3.4.1/src/external/rawspeed
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622936713
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo  -DDONT_USE_INTERNAL_LUA=Off -DBINARY_PACKAGE_BUILD=ON  -DRAWSPEED_ENABLE_LTO=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
export FFLAGS="$FFLAGS -march=haswell -m64"
export FCFLAGS="$FCFLAGS -march=haswell -m64"
%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo  -DDONT_USE_INTERNAL_LUA=Off -DBINARY_PACKAGE_BUILD=ON  -DRAWSPEED_ENABLE_LTO=ON
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1622936713
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/darktable
cp %{_builddir}/darktable-3.4.1/LICENSE %{buildroot}/usr/share/package-licenses/darktable/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/darktable-3.4.1/data/pswp/LICENSE %{buildroot}/usr/share/package-licenses/darktable/d9f41c058914394e203adb253057643e047576a3
cp %{_builddir}/darktable-3.4.1/src/external/LuaAutoC/LICENSE.md %{buildroot}/usr/share/package-licenses/darktable/6baddc7988322d021a187ff7d1d0fb9e2a784e20
cp %{_builddir}/darktable-3.4.1/src/external/OpenCL/LICENSE %{buildroot}/usr/share/package-licenses/darktable/7235f6784b4eae4c40a259dcecc7a20e6c487263
cp %{_builddir}/darktable-3.4.1/src/external/libxcf/LICENSE %{buildroot}/usr/share/package-licenses/darktable/fc356b2c50a063b663cc14dde29bc0ab9e7bec51
cp %{_builddir}/darktable-3.4.1/src/external/rawspeed/LICENSE %{buildroot}/usr/share/package-licenses/darktable/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/darktable-3.4.1/src/external/whereami/LICENSE.MIT %{buildroot}/usr/share/package-licenses/darktable/c996ffd4c579d586b7d86e158af6042018c3c422
cp %{_builddir}/darktable-3.4.1/src/external/whereami/LICENSE.WTFPLv2 %{buildroot}/usr/share/package-licenses/darktable/75e5bae837deb898dae4cb65c4890b1ab825c6b6
cp %{_builddir}/rawspeed-3.3/LICENSE %{buildroot}/usr/share/package-licenses/darktable/3704f4680301a60004b20f94e0b5b8c7ff1484a9
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd
%find_lang darktable
## install_append content
#for i in %{buildroot}/usr/lib64/haswell/darktable/*.so; do mv $i $i.avx2 ; done
#mv %{buildroot}/usr/lib64/haswell/darktable/*.so.avx2 %{buildroot}/usr/lib64/darktable/

#for i in %{buildroot}/usr/lib64/haswell/darktable/plugins/*.so; do mv $i $i.avx2 ; done
#mv %{buildroot}/usr/lib64/haswell/darktable/plugins/*.so.avx2 %{buildroot}/usr/lib64/darktable/plugins/


#for i in %{buildroot}/usr/lib64/haswell/darktable/plugins/lighttable/*.so; do mv $i $i.avx2 ; done
#mv %{buildroot}/usr/lib64/haswell/darktable/plugins/lighttable/*.so.avx2 %{buildroot}/usr/lib64/darktable/plugins/lighttable/


#for i in %{buildroot}/usr/lib64/haswell/darktable/views/*.so; do mv $i $i.avx2 ; done
#mv %{buildroot}/usr/lib64/haswell/darktable/views/*.so.avx2 %{buildroot}/usr/lib64/darktable/views/


ln -s darktable/libdarktable.so %{buildroot}/usr/lib64/libdarktable.so
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/darktable
/usr/bin/darktable-chart
/usr/bin/darktable-cli
/usr/bin/darktable-cltest
/usr/bin/darktable-cmstest
/usr/bin/darktable-generate-cache
/usr/bin/darktable-rs-identify
/usr/bin/haswell/darktable
/usr/bin/haswell/darktable-chart
/usr/bin/haswell/darktable-cli
/usr/bin/haswell/darktable-cltest
/usr/bin/haswell/darktable-cmstest
/usr/bin/haswell/darktable-generate-cache
/usr/bin/haswell/darktable-rs-identify

%files data
%defattr(-,root,root,-)
/usr/share/appdata/darktable.appdata.xml
/usr/share/applications/darktable.desktop
/usr/share/darktable/darktable.bash
/usr/share/darktable/darktablerc
/usr/share/darktable/gdb_commands
/usr/share/darktable/kernels/atrous.cl
/usr/share/darktable/kernels/basecurve.cl
/usr/share/darktable/kernels/basic.cl
/usr/share/darktable/kernels/basicadj.cl
/usr/share/darktable/kernels/bilateral.cl
/usr/share/darktable/kernels/blendop.cl
/usr/share/darktable/kernels/bloom.cl
/usr/share/darktable/kernels/color_conversion.cl
/usr/share/darktable/kernels/colorreconstruction.cl
/usr/share/darktable/kernels/colorspace.cl
/usr/share/darktable/kernels/colorspaces.cl
/usr/share/darktable/kernels/common.h
/usr/share/darktable/kernels/demosaic_markesteijn.cl
/usr/share/darktable/kernels/demosaic_other.cl
/usr/share/darktable/kernels/demosaic_ppg.cl
/usr/share/darktable/kernels/demosaic_vng.cl
/usr/share/darktable/kernels/denoiseprofile.cl
/usr/share/darktable/kernels/dwt.cl
/usr/share/darktable/kernels/extended.cl
/usr/share/darktable/kernels/filmic.cl
/usr/share/darktable/kernels/gaussian.cl
/usr/share/darktable/kernels/guided_filter.cl
/usr/share/darktable/kernels/hazeremoval.cl
/usr/share/darktable/kernels/highpass.cl
/usr/share/darktable/kernels/liquify.cl
/usr/share/darktable/kernels/locallaplacian.cl
/usr/share/darktable/kernels/lut3d.cl
/usr/share/darktable/kernels/negadoctor.cl
/usr/share/darktable/kernels/nlmeans.cl
/usr/share/darktable/kernels/noise_generator.h
/usr/share/darktable/kernels/programs.conf
/usr/share/darktable/kernels/retouch.cl
/usr/share/darktable/kernels/rgb_norms.h
/usr/share/darktable/kernels/rgbcurve.cl
/usr/share/darktable/kernels/rgblevels.cl
/usr/share/darktable/kernels/sharpen.cl
/usr/share/darktable/kernels/soften.cl
/usr/share/darktable/latex/photobook.cls
/usr/share/darktable/lua/darktable/debug.lua
/usr/share/darktable/luarc
/usr/share/darktable/noiseprofiles.json
/usr/share/darktable/pixmaps/dt_logo_128x128.png
/usr/share/darktable/pixmaps/dt_text.svg
/usr/share/darktable/pixmaps/idbutton-1.png
/usr/share/darktable/pixmaps/idbutton-1.svg
/usr/share/darktable/pixmaps/idbutton-2.png
/usr/share/darktable/pixmaps/idbutton-2.svg
/usr/share/darktable/pixmaps/idbutton-3.png
/usr/share/darktable/pixmaps/idbutton-3.svg
/usr/share/darktable/pixmaps/idbutton.png
/usr/share/darktable/pixmaps/idbutton.svg
/usr/share/darktable/pixmaps/plugins/darkroom/ashift.png
/usr/share/darktable/pixmaps/plugins/darkroom/ashift.svg
/usr/share/darktable/pixmaps/plugins/darkroom/atrous.png
/usr/share/darktable/pixmaps/plugins/darkroom/atrous.svg
/usr/share/darktable/pixmaps/plugins/darkroom/basecurve.png
/usr/share/darktable/pixmaps/plugins/darkroom/basecurve.svg
/usr/share/darktable/pixmaps/plugins/darkroom/bilateral.png
/usr/share/darktable/pixmaps/plugins/darkroom/bilateral.svg
/usr/share/darktable/pixmaps/plugins/darkroom/bloom.png
/usr/share/darktable/pixmaps/plugins/darkroom/bloom.svg
/usr/share/darktable/pixmaps/plugins/darkroom/borders.png
/usr/share/darktable/pixmaps/plugins/darkroom/borders.svg
/usr/share/darktable/pixmaps/plugins/darkroom/cacorrect.png
/usr/share/darktable/pixmaps/plugins/darkroom/cacorrect.svg
/usr/share/darktable/pixmaps/plugins/darkroom/channelmixer.png
/usr/share/darktable/pixmaps/plugins/darkroom/channelmixer.svg
/usr/share/darktable/pixmaps/plugins/darkroom/clahe.png
/usr/share/darktable/pixmaps/plugins/darkroom/clahe.svg
/usr/share/darktable/pixmaps/plugins/darkroom/clipping.png
/usr/share/darktable/pixmaps/plugins/darkroom/clipping.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colisa.png
/usr/share/darktable/pixmaps/plugins/darkroom/colisa.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colorcorrection.png
/usr/share/darktable/pixmaps/plugins/darkroom/colorcorrection.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colorin.png
/usr/share/darktable/pixmaps/plugins/darkroom/colorin.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colormapping.png
/usr/share/darktable/pixmaps/plugins/darkroom/colormapping.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colorout.png
/usr/share/darktable/pixmaps/plugins/darkroom/colorout.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colorreconstruct.png
/usr/share/darktable/pixmaps/plugins/darkroom/colorreconstruct.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colortransfer.png
/usr/share/darktable/pixmaps/plugins/darkroom/colortransfer.svg
/usr/share/darktable/pixmaps/plugins/darkroom/colorzones.png
/usr/share/darktable/pixmaps/plugins/darkroom/colorzones.svg
/usr/share/darktable/pixmaps/plugins/darkroom/default.svg
/usr/share/darktable/pixmaps/plugins/darkroom/demosaic.png
/usr/share/darktable/pixmaps/plugins/darkroom/demosaic.svg
/usr/share/darktable/pixmaps/plugins/darkroom/dither.png
/usr/share/darktable/pixmaps/plugins/darkroom/dither.svg
/usr/share/darktable/pixmaps/plugins/darkroom/exposure.png
/usr/share/darktable/pixmaps/plugins/darkroom/exposure.svg
/usr/share/darktable/pixmaps/plugins/darkroom/flip.png
/usr/share/darktable/pixmaps/plugins/darkroom/flip.svg
/usr/share/darktable/pixmaps/plugins/darkroom/graduatednd.png
/usr/share/darktable/pixmaps/plugins/darkroom/graduatednd.svg
/usr/share/darktable/pixmaps/plugins/darkroom/grain.png
/usr/share/darktable/pixmaps/plugins/darkroom/grain.svg
/usr/share/darktable/pixmaps/plugins/darkroom/hazeremoval.png
/usr/share/darktable/pixmaps/plugins/darkroom/hazeremoval.svg
/usr/share/darktable/pixmaps/plugins/darkroom/highlights.png
/usr/share/darktable/pixmaps/plugins/darkroom/highlights.svg
/usr/share/darktable/pixmaps/plugins/darkroom/highpass.png
/usr/share/darktable/pixmaps/plugins/darkroom/highpass.svg
/usr/share/darktable/pixmaps/plugins/darkroom/hotpixels.png
/usr/share/darktable/pixmaps/plugins/darkroom/hotpixels.svg
/usr/share/darktable/pixmaps/plugins/darkroom/invert.png
/usr/share/darktable/pixmaps/plugins/darkroom/invert.svg
/usr/share/darktable/pixmaps/plugins/darkroom/lens.png
/usr/share/darktable/pixmaps/plugins/darkroom/lens.svg
/usr/share/darktable/pixmaps/plugins/darkroom/levels.png
/usr/share/darktable/pixmaps/plugins/darkroom/levels.svg
/usr/share/darktable/pixmaps/plugins/darkroom/liquify.png
/usr/share/darktable/pixmaps/plugins/darkroom/liquify.svg
/usr/share/darktable/pixmaps/plugins/darkroom/lowlight.png
/usr/share/darktable/pixmaps/plugins/darkroom/lowlight.svg
/usr/share/darktable/pixmaps/plugins/darkroom/lowpass.png
/usr/share/darktable/pixmaps/plugins/darkroom/lowpass.svg
/usr/share/darktable/pixmaps/plugins/darkroom/monochrome.png
/usr/share/darktable/pixmaps/plugins/darkroom/monochrome.svg
/usr/share/darktable/pixmaps/plugins/darkroom/nlmeans.png
/usr/share/darktable/pixmaps/plugins/darkroom/nlmeans.svg
/usr/share/darktable/pixmaps/plugins/darkroom/overexposed.png
/usr/share/darktable/pixmaps/plugins/darkroom/overexposed.svg
/usr/share/darktable/pixmaps/plugins/darkroom/profile_gamma.png
/usr/share/darktable/pixmaps/plugins/darkroom/profile_gamma.svg
/usr/share/darktable/pixmaps/plugins/darkroom/rawdenoise.png
/usr/share/darktable/pixmaps/plugins/darkroom/rawdenoise.svg
/usr/share/darktable/pixmaps/plugins/darkroom/rawimport.png
/usr/share/darktable/pixmaps/plugins/darkroom/rawimport.svg
/usr/share/darktable/pixmaps/plugins/darkroom/rawprepare.png
/usr/share/darktable/pixmaps/plugins/darkroom/rawprepare.svg
/usr/share/darktable/pixmaps/plugins/darkroom/relight.png
/usr/share/darktable/pixmaps/plugins/darkroom/relight.svg
/usr/share/darktable/pixmaps/plugins/darkroom/shadhi.png
/usr/share/darktable/pixmaps/plugins/darkroom/shadhi.svg
/usr/share/darktable/pixmaps/plugins/darkroom/sharpen.png
/usr/share/darktable/pixmaps/plugins/darkroom/sharpen.svg
/usr/share/darktable/pixmaps/plugins/darkroom/soften.png
/usr/share/darktable/pixmaps/plugins/darkroom/soften.svg
/usr/share/darktable/pixmaps/plugins/darkroom/splittoning.png
/usr/share/darktable/pixmaps/plugins/darkroom/splittoning.svg
/usr/share/darktable/pixmaps/plugins/darkroom/spots.png
/usr/share/darktable/pixmaps/plugins/darkroom/spots.svg
/usr/share/darktable/pixmaps/plugins/darkroom/temperature.png
/usr/share/darktable/pixmaps/plugins/darkroom/temperature.svg
/usr/share/darktable/pixmaps/plugins/darkroom/template.png
/usr/share/darktable/pixmaps/plugins/darkroom/template.svg
/usr/share/darktable/pixmaps/plugins/darkroom/tonecurve.png
/usr/share/darktable/pixmaps/plugins/darkroom/tonecurve.svg
/usr/share/darktable/pixmaps/plugins/darkroom/tonemap.png
/usr/share/darktable/pixmaps/plugins/darkroom/tonemap.svg
/usr/share/darktable/pixmaps/plugins/darkroom/velvia.png
/usr/share/darktable/pixmaps/plugins/darkroom/velvia.svg
/usr/share/darktable/pixmaps/plugins/darkroom/vignette.png
/usr/share/darktable/pixmaps/plugins/darkroom/vignette.svg
/usr/share/darktable/pixmaps/plugins/darkroom/watermark.png
/usr/share/darktable/pixmaps/plugins/darkroom/watermark.svg
/usr/share/darktable/pixmaps/plugins/darkroom/zonesystem.png
/usr/share/darktable/pixmaps/plugins/darkroom/zonesystem.svg
/usr/share/darktable/pswp/LICENSE
/usr/share/darktable/pswp/default-skin/default-skin.css
/usr/share/darktable/pswp/default-skin/default-skin.png
/usr/share/darktable/pswp/default-skin/default-skin.svg
/usr/share/darktable/pswp/default-skin/preloader.gif
/usr/share/darktable/pswp/photoswipe-ui-default.js
/usr/share/darktable/pswp/photoswipe-ui-default.min.js
/usr/share/darktable/pswp/photoswipe.css
/usr/share/darktable/pswp/photoswipe.js
/usr/share/darktable/pswp/photoswipe.min.js
/usr/share/darktable/rawspeed/cameras.xml
/usr/share/darktable/rawspeed/showcameras.xsl
/usr/share/darktable/style/bullet.gif
/usr/share/darktable/style/close.gif
/usr/share/darktable/style/closelabel.gif
/usr/share/darktable/style/donate-button.gif
/usr/share/darktable/style/download-icon.gif
/usr/share/darktable/style/favicon.ico
/usr/share/darktable/style/image-1.jpg
/usr/share/darktable/style/lightbox.css
/usr/share/darktable/style/loading.gif
/usr/share/darktable/style/nextlabel.gif
/usr/share/darktable/style/prevlabel.gif
/usr/share/darktable/style/style.css
/usr/share/darktable/style/thumb-1.jpg
/usr/share/darktable/themes/darktable-elegant-dark.css
/usr/share/darktable/themes/darktable-elegant-darker.css
/usr/share/darktable/themes/darktable-elegant-grey.css
/usr/share/darktable/themes/darktable-icons-dark.css
/usr/share/darktable/themes/darktable-icons-darker.css
/usr/share/darktable/themes/darktable-icons-grey.css
/usr/share/darktable/themes/darktable-icons.css
/usr/share/darktable/themes/darktable.css
/usr/share/darktable/tools/common.sh
/usr/share/darktable/tools/purge_from_cache.sh
/usr/share/darktable/tools/purge_non_existing_images.sh
/usr/share/darktable/tools/purge_unused_tags.sh
/usr/share/darktable/watermarks/darktable.svg
/usr/share/darktable/watermarks/hasselblad.svg
/usr/share/darktable/watermarks/promo.svg
/usr/share/darktable/watermarks/simple-text.svg
/usr/share/icons/hicolor/16x16/apps/darktable.png
/usr/share/icons/hicolor/22x22/apps/darktable.png
/usr/share/icons/hicolor/24x24/apps/darktable.png
/usr/share/icons/hicolor/256x256/apps/darktable.png
/usr/share/icons/hicolor/32x32/apps/darktable.png
/usr/share/icons/hicolor/48x48/apps/darktable.png
/usr/share/icons/hicolor/64x64/apps/darktable.png
/usr/share/icons/hicolor/scalable/apps/darktable-1.svg
/usr/share/icons/hicolor/scalable/apps/darktable-2.svg
/usr/share/icons/hicolor/scalable/apps/darktable-3.svg
/usr/share/icons/hicolor/scalable/apps/darktable.svg

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/darktable/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/darktable/haswell/libdarktable.so
/usr/lib64/darktable/libdarktable.so
/usr/lib64/darktable/plugins/imageio/format/libcopy.so
/usr/lib64/darktable/plugins/imageio/format/libexr.so
/usr/lib64/darktable/plugins/imageio/format/libexr.so.avx2
/usr/lib64/darktable/plugins/imageio/format/libjpeg.so
/usr/lib64/darktable/plugins/imageio/format/libpdf.so
/usr/lib64/darktable/plugins/imageio/format/libpdf.so.avx2
/usr/lib64/darktable/plugins/imageio/format/libpfm.so
/usr/lib64/darktable/plugins/imageio/format/libpng.so
/usr/lib64/darktable/plugins/imageio/format/libpng.so.avx2
/usr/lib64/darktable/plugins/imageio/format/libppm.so
/usr/lib64/darktable/plugins/imageio/format/libtiff.so
/usr/lib64/darktable/plugins/imageio/format/libtiff.so.avx2
/usr/lib64/darktable/plugins/imageio/format/libwebp.so
/usr/lib64/darktable/plugins/imageio/format/libxcf.so
/usr/lib64/darktable/plugins/imageio/format/libxcf.so.avx2
/usr/lib64/darktable/plugins/imageio/storage/libdisk.so
/usr/lib64/darktable/plugins/imageio/storage/libemail.so
/usr/lib64/darktable/plugins/imageio/storage/libgallery.so
/usr/lib64/darktable/plugins/imageio/storage/liblatex.so
/usr/lib64/darktable/plugins/imageio/storage/libpiwigo.so
/usr/lib64/darktable/plugins/libashift.so
/usr/lib64/darktable/plugins/libashift.so.avx2
/usr/lib64/darktable/plugins/libatrous.so
/usr/lib64/darktable/plugins/libatrous.so.avx2
/usr/lib64/darktable/plugins/libbasecurve.so
/usr/lib64/darktable/plugins/libbasecurve.so.avx2
/usr/lib64/darktable/plugins/libbasicadj.so
/usr/lib64/darktable/plugins/libbasicadj.so.avx2
/usr/lib64/darktable/plugins/libbilat.so
/usr/lib64/darktable/plugins/libbilateral.so
/usr/lib64/darktable/plugins/libbilateral.so.avx2
/usr/lib64/darktable/plugins/libbloom.so
/usr/lib64/darktable/plugins/libbloom.so.avx2
/usr/lib64/darktable/plugins/libborders.so
/usr/lib64/darktable/plugins/libborders.so.avx2
/usr/lib64/darktable/plugins/libcacorrect.so
/usr/lib64/darktable/plugins/libcacorrect.so.avx2
/usr/lib64/darktable/plugins/libchannelmixer.so
/usr/lib64/darktable/plugins/libchannelmixer.so.avx2
/usr/lib64/darktable/plugins/libchannelmixerrgb.so
/usr/lib64/darktable/plugins/libchannelmixerrgb.so.avx2
/usr/lib64/darktable/plugins/libclahe.so
/usr/lib64/darktable/plugins/libclahe.so.avx2
/usr/lib64/darktable/plugins/libclipping.so
/usr/lib64/darktable/plugins/libclipping.so.avx2
/usr/lib64/darktable/plugins/libcolisa.so
/usr/lib64/darktable/plugins/libcolisa.so.avx2
/usr/lib64/darktable/plugins/libcolorbalance.so
/usr/lib64/darktable/plugins/libcolorbalance.so.avx2
/usr/lib64/darktable/plugins/libcolorchecker.so
/usr/lib64/darktable/plugins/libcolorchecker.so.avx2
/usr/lib64/darktable/plugins/libcolorcontrast.so
/usr/lib64/darktable/plugins/libcolorcontrast.so.avx2
/usr/lib64/darktable/plugins/libcolorcorrection.so
/usr/lib64/darktable/plugins/libcolorcorrection.so.avx2
/usr/lib64/darktable/plugins/libcolorin.so
/usr/lib64/darktable/plugins/libcolorin.so.avx2
/usr/lib64/darktable/plugins/libcolorize.so
/usr/lib64/darktable/plugins/libcolormapping.so
/usr/lib64/darktable/plugins/libcolormapping.so.avx2
/usr/lib64/darktable/plugins/libcolorout.so
/usr/lib64/darktable/plugins/libcolorout.so.avx2
/usr/lib64/darktable/plugins/libcolorreconstruct.so
/usr/lib64/darktable/plugins/libcolortransfer.so
/usr/lib64/darktable/plugins/libcolortransfer.so.avx2
/usr/lib64/darktable/plugins/libcolorzones.so
/usr/lib64/darktable/plugins/libcolorzones.so.avx2
/usr/lib64/darktable/plugins/libdefringe.so
/usr/lib64/darktable/plugins/libdefringe.so.avx2
/usr/lib64/darktable/plugins/libdemosaic.so
/usr/lib64/darktable/plugins/libdemosaic.so.avx2
/usr/lib64/darktable/plugins/libdenoiseprofile.so
/usr/lib64/darktable/plugins/libdenoiseprofile.so.avx2
/usr/lib64/darktable/plugins/libdither.so
/usr/lib64/darktable/plugins/libdither.so.avx2
/usr/lib64/darktable/plugins/libequalizer.so
/usr/lib64/darktable/plugins/libequalizer.so.avx2
/usr/lib64/darktable/plugins/libexposure.so
/usr/lib64/darktable/plugins/libexposure.so.avx2
/usr/lib64/darktable/plugins/libfilmic.so
/usr/lib64/darktable/plugins/libfilmic.so.avx2
/usr/lib64/darktable/plugins/libfilmicrgb.so
/usr/lib64/darktable/plugins/libfilmicrgb.so.avx2
/usr/lib64/darktable/plugins/libfinalscale.so
/usr/lib64/darktable/plugins/libflip.so
/usr/lib64/darktable/plugins/libflip.so.avx2
/usr/lib64/darktable/plugins/libgamma.so
/usr/lib64/darktable/plugins/libglobaltonemap.so
/usr/lib64/darktable/plugins/libgraduatednd.so
/usr/lib64/darktable/plugins/libgraduatednd.so.avx2
/usr/lib64/darktable/plugins/libgrain.so
/usr/lib64/darktable/plugins/libgrain.so.avx2
/usr/lib64/darktable/plugins/libhazeremoval.so
/usr/lib64/darktable/plugins/libhazeremoval.so.avx2
/usr/lib64/darktable/plugins/libhighlights.so
/usr/lib64/darktable/plugins/libhighlights.so.avx2
/usr/lib64/darktable/plugins/libhighpass.so
/usr/lib64/darktable/plugins/libhighpass.so.avx2
/usr/lib64/darktable/plugins/libhotpixels.so
/usr/lib64/darktable/plugins/libhotpixels.so.avx2
/usr/lib64/darktable/plugins/libinvert.so
/usr/lib64/darktable/plugins/libinvert.so.avx2
/usr/lib64/darktable/plugins/liblens.so
/usr/lib64/darktable/plugins/liblens.so.avx2
/usr/lib64/darktable/plugins/liblevels.so
/usr/lib64/darktable/plugins/libliquify.so
/usr/lib64/darktable/plugins/libliquify.so.avx2
/usr/lib64/darktable/plugins/liblowlight.so
/usr/lib64/darktable/plugins/liblowlight.so.avx2
/usr/lib64/darktable/plugins/liblowpass.so
/usr/lib64/darktable/plugins/liblowpass.so.avx2
/usr/lib64/darktable/plugins/liblut3d.so
/usr/lib64/darktable/plugins/liblut3d.so.avx2
/usr/lib64/darktable/plugins/libmask_manager.so
/usr/lib64/darktable/plugins/libmonochrome.so
/usr/lib64/darktable/plugins/libmonochrome.so.avx2
/usr/lib64/darktable/plugins/libnegadoctor.so
/usr/lib64/darktable/plugins/libnegadoctor.so.avx2
/usr/lib64/darktable/plugins/libnlmeans.so
/usr/lib64/darktable/plugins/liboverexposed.so
/usr/lib64/darktable/plugins/libprofile_gamma.so
/usr/lib64/darktable/plugins/libprofile_gamma.so.avx2
/usr/lib64/darktable/plugins/librawdenoise.so
/usr/lib64/darktable/plugins/librawdenoise.so.avx2
/usr/lib64/darktable/plugins/librawoverexposed.so
/usr/lib64/darktable/plugins/librawoverexposed.so.avx2
/usr/lib64/darktable/plugins/librawprepare.so
/usr/lib64/darktable/plugins/librawprepare.so.avx2
/usr/lib64/darktable/plugins/librelight.so
/usr/lib64/darktable/plugins/libretouch.so
/usr/lib64/darktable/plugins/libretouch.so.avx2
/usr/lib64/darktable/plugins/librgbcurve.so
/usr/lib64/darktable/plugins/librgbcurve.so.avx2
/usr/lib64/darktable/plugins/librgblevels.so
/usr/lib64/darktable/plugins/librotatepixels.so
/usr/lib64/darktable/plugins/librotatepixels.so.avx2
/usr/lib64/darktable/plugins/libscalepixels.so
/usr/lib64/darktable/plugins/libscalepixels.so.avx2
/usr/lib64/darktable/plugins/libshadhi.so
/usr/lib64/darktable/plugins/libshadhi.so.avx2
/usr/lib64/darktable/plugins/libsharpen.so
/usr/lib64/darktable/plugins/libsharpen.so.avx2
/usr/lib64/darktable/plugins/libsoften.so
/usr/lib64/darktable/plugins/libsoften.so.avx2
/usr/lib64/darktable/plugins/libsplittoning.so
/usr/lib64/darktable/plugins/libspots.so
/usr/lib64/darktable/plugins/libspots.so.avx2
/usr/lib64/darktable/plugins/libtemperature.so
/usr/lib64/darktable/plugins/libtemperature.so.avx2
/usr/lib64/darktable/plugins/libtonecurve.so
/usr/lib64/darktable/plugins/libtonecurve.so.avx2
/usr/lib64/darktable/plugins/libtoneequal.so
/usr/lib64/darktable/plugins/libtoneequal.so.avx2
/usr/lib64/darktable/plugins/libtonemap.so
/usr/lib64/darktable/plugins/libtonemap.so.avx2
/usr/lib64/darktable/plugins/libvelvia.so
/usr/lib64/darktable/plugins/libvelvia.so.avx2
/usr/lib64/darktable/plugins/libvibrance.so
/usr/lib64/darktable/plugins/libvignette.so
/usr/lib64/darktable/plugins/libwatermark.so
/usr/lib64/darktable/plugins/libwatermark.so.avx2
/usr/lib64/darktable/plugins/libzonesystem.so
/usr/lib64/darktable/plugins/libzonesystem.so.avx2
/usr/lib64/darktable/plugins/lighttable/libbackgroundjobs.so
/usr/lib64/darktable/plugins/lighttable/libcamera.so
/usr/lib64/darktable/plugins/lighttable/libcollect.so
/usr/lib64/darktable/plugins/lighttable/libcollect.so.avx2
/usr/lib64/darktable/plugins/lighttable/libcolorlabels.so
/usr/lib64/darktable/plugins/lighttable/libcolorpicker.so
/usr/lib64/darktable/plugins/lighttable/libcolorpicker.so.avx2
/usr/lib64/darktable/plugins/lighttable/libcopy_history.so
/usr/lib64/darktable/plugins/lighttable/libdarktable_label.so
/usr/lib64/darktable/plugins/lighttable/libduplicate.so
/usr/lib64/darktable/plugins/lighttable/libexport.so
/usr/lib64/darktable/plugins/lighttable/libfilmstrip.so
/usr/lib64/darktable/plugins/lighttable/libfilter.so
/usr/lib64/darktable/plugins/lighttable/libgeotagging.so
/usr/lib64/darktable/plugins/lighttable/libglobal_toolbox.so
/usr/lib64/darktable/plugins/lighttable/libhinter.so
/usr/lib64/darktable/plugins/lighttable/libhistogram.so
/usr/lib64/darktable/plugins/lighttable/libhistogram.so.avx2
/usr/lib64/darktable/plugins/lighttable/libhistory.so
/usr/lib64/darktable/plugins/lighttable/libimage.so
/usr/lib64/darktable/plugins/lighttable/libimage_infos.so
/usr/lib64/darktable/plugins/lighttable/libimport.so
/usr/lib64/darktable/plugins/lighttable/libioporder.so
/usr/lib64/darktable/plugins/lighttable/liblighttable_mode.so
/usr/lib64/darktable/plugins/lighttable/liblive_view.so
/usr/lib64/darktable/plugins/lighttable/libmasks.so
/usr/lib64/darktable/plugins/lighttable/libmetadata.so
/usr/lib64/darktable/plugins/lighttable/libmetadata_view.so
/usr/lib64/darktable/plugins/lighttable/libmodule_toolbox.so
/usr/lib64/darktable/plugins/lighttable/libmodulegroups.so
/usr/lib64/darktable/plugins/lighttable/libnavigation.so
/usr/lib64/darktable/plugins/lighttable/libprint_settings.so
/usr/lib64/darktable/plugins/lighttable/libprint_settings.so.avx2
/usr/lib64/darktable/plugins/lighttable/libratings.so
/usr/lib64/darktable/plugins/lighttable/librecentcollect.so
/usr/lib64/darktable/plugins/lighttable/libselect.so
/usr/lib64/darktable/plugins/lighttable/libsession.so
/usr/lib64/darktable/plugins/lighttable/libsnapshots.so
/usr/lib64/darktable/plugins/lighttable/libsnapshots.so.avx2
/usr/lib64/darktable/plugins/lighttable/libstyles.so
/usr/lib64/darktable/plugins/lighttable/libtagging.so
/usr/lib64/darktable/plugins/lighttable/libtimeline.so
/usr/lib64/darktable/plugins/lighttable/libtimeline.so.avx2
/usr/lib64/darktable/plugins/lighttable/libview_toolbox.so
/usr/lib64/darktable/plugins/lighttable/libviewswitcher.so
/usr/lib64/darktable/views/libdarkroom.so
/usr/lib64/darktable/views/libdarkroom.so.avx2
/usr/lib64/darktable/views/libknight.so
/usr/lib64/darktable/views/liblighttable.so
/usr/lib64/darktable/views/libprint.so
/usr/lib64/darktable/views/libslideshow.so
/usr/lib64/darktable/views/libtethering.so
/usr/lib64/darktable/views/libtethering.so.avx2
/usr/lib64/libdarktable.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/darktable/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/darktable/6baddc7988322d021a187ff7d1d0fb9e2a784e20
/usr/share/package-licenses/darktable/7235f6784b4eae4c40a259dcecc7a20e6c487263
/usr/share/package-licenses/darktable/75e5bae837deb898dae4cb65c4890b1ab825c6b6
/usr/share/package-licenses/darktable/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/darktable/c996ffd4c579d586b7d86e158af6042018c3c422
/usr/share/package-licenses/darktable/d9f41c058914394e203adb253057643e047576a3
/usr/share/package-licenses/darktable/fc356b2c50a063b663cc14dde29bc0ab9e7bec51

%files man
%defattr(0644,root,root,0755)
/usr/share/man/de/man1/darktable-cli.1
/usr/share/man/de/man1/darktable-cltest.1
/usr/share/man/de/man1/darktable-cmstest.1
/usr/share/man/de/man1/darktable-generate-cache.1
/usr/share/man/de/man1/darktable.1
/usr/share/man/es/man1/darktable-cli.1
/usr/share/man/es/man1/darktable-cltest.1
/usr/share/man/es/man1/darktable-cmstest.1
/usr/share/man/es/man1/darktable-generate-cache.1
/usr/share/man/es/man1/darktable.1
/usr/share/man/fr/man1/darktable-cli.1
/usr/share/man/fr/man1/darktable-cltest.1
/usr/share/man/fr/man1/darktable-cmstest.1
/usr/share/man/fr/man1/darktable-generate-cache.1
/usr/share/man/fr/man1/darktable.1
/usr/share/man/man1/darktable-cli.1
/usr/share/man/man1/darktable-cltest.1
/usr/share/man/man1/darktable-cmstest.1
/usr/share/man/man1/darktable-generate-cache.1
/usr/share/man/man1/darktable.1

%files locales -f darktable.lang
%defattr(-,root,root,-)

