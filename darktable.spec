#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : darktable
Version  : 2.2.5
Release  : 12
URL      : https://github.com/darktable-org/darktable/releases/download/release-2.2.5/darktable-2.2.5.tar.xz
Source0  : https://github.com/darktable-org/darktable/releases/download/release-2.2.5/darktable-2.2.5.tar.xz
Summary  : A virtual Lighttable and Darkroom
Group    : Development/Tools
License  : BSD-2-Clause-FreeBSD GPL-3.0 GPL-3.0+ LGPL-2.1 MIT
Requires: darktable-bin
Requires: darktable-lib
Requires: darktable-data
Requires: darktable-doc
Requires: darktable-locales
BuildRequires : beignet-dev
BuildRequires : cmake
BuildRequires : colord-dev
BuildRequires : curl-dev
BuildRequires : desktop-file-utils
BuildRequires : exiv2-dev
BuildRequires : expat-dev
BuildRequires : glib-dev
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : json-glib-dev
BuildRequires : lcms2-dev
BuildRequires : lensfun-dev
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
BuildRequires : ocl-icd-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pugixml-dev
BuildRequires : sqlite-autoconf-dev
Patch1: build.patch

%description
darktable is a virtual lighttable and darkroom for photographers: it manages 
your digital negatives in a database and lets you view them through a zoomable 
lighttable. it also enables you to develop raw images and enhance them.

%package bin
Summary: bin components for the darktable package.
Group: Binaries
Requires: darktable-data

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

%description doc
doc components for the darktable package.


%package lib
Summary: lib components for the darktable package.
Group: Libraries
Requires: darktable-data

%description lib
lib components for the darktable package.


%package locales
Summary: locales components for the darktable package.
Group: Default

%description locales
locales components for the darktable package.


%prep
%setup -q -n darktable-2.2.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496071545
mkdir clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DCMAKE_BUILD_TYPE=RelWithDebInfo  -DDONT_USE_INTERNAL_LUA=Off -DBINARY_PACKAGE_BUILD=ON
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1496071545
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang darktable

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

%files data
%defattr(-,root,root,-)
/usr/share/appdata/darktable.appdata.xml
/usr/share/applications/darktable.desktop
/usr/share/darktable/darktable.css
/usr/share/darktable/darktablerc
/usr/share/darktable/gdb_commands
/usr/share/darktable/kernels/atrous.cl
/usr/share/darktable/kernels/basecurve.cl
/usr/share/darktable/kernels/basic.cl
/usr/share/darktable/kernels/bilateral.cl
/usr/share/darktable/kernels/blendop.cl
/usr/share/darktable/kernels/bloom.cl
/usr/share/darktable/kernels/colorreconstruction.cl
/usr/share/darktable/kernels/colorspace.cl
/usr/share/darktable/kernels/common.h
/usr/share/darktable/kernels/demosaic_markesteijn.cl
/usr/share/darktable/kernels/demosaic_other.cl
/usr/share/darktable/kernels/demosaic_ppg.cl
/usr/share/darktable/kernels/demosaic_vng.cl
/usr/share/darktable/kernels/denoiseprofile.cl
/usr/share/darktable/kernels/extended.cl
/usr/share/darktable/kernels/gaussian.cl
/usr/share/darktable/kernels/highpass.cl
/usr/share/darktable/kernels/liquify.cl
/usr/share/darktable/kernels/nlmeans.cl
/usr/share/darktable/kernels/programs.conf
/usr/share/darktable/kernels/sharpen.cl
/usr/share/darktable/kernels/soften.cl
/usr/share/darktable/latex/photobook.cls
/usr/share/darktable/lua/darktable/debug.lua
/usr/share/darktable/lua/darktable/external/pygy_require/.gitignore
/usr/share/darktable/lua/darktable/external/pygy_require/README.md
/usr/share/darktable/lua/darktable/external/pygy_require/require.lua
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.1-1.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.2-1.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.3-1.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.4-1.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.4-2.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.4-3.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.4-4.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.4-5.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.5-1.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.6-1.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.7-1.rockspec
/usr/share/darktable/lua/darktable/external/pygy_require/rockspecs/require-0.1.7-2.rockspec
/usr/share/darktable/luarc
/usr/share/darktable/noiseprofiles.json
/usr/share/darktable/pixmaps/dt_logo_128x128.png
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
%defattr(-,root,root,-)
%doc /usr/share/doc/darktable/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/darktable/libdarktable.so
/usr/lib64/darktable/plugins/imageio/format/libcopy.so
/usr/lib64/darktable/plugins/imageio/format/libjpeg.so
/usr/lib64/darktable/plugins/imageio/format/libpdf.so
/usr/lib64/darktable/plugins/imageio/format/libpfm.so
/usr/lib64/darktable/plugins/imageio/format/libpng.so
/usr/lib64/darktable/plugins/imageio/format/libppm.so
/usr/lib64/darktable/plugins/imageio/format/libwebp.so
/usr/lib64/darktable/plugins/imageio/storage/libdisk.so
/usr/lib64/darktable/plugins/imageio/storage/libemail.so
/usr/lib64/darktable/plugins/imageio/storage/libfacebook.so
/usr/lib64/darktable/plugins/imageio/storage/libgallery.so
/usr/lib64/darktable/plugins/imageio/storage/liblatex.so
/usr/lib64/darktable/plugins/imageio/storage/libpicasa.so
/usr/lib64/darktable/plugins/libashift.so
/usr/lib64/darktable/plugins/libatrous.so
/usr/lib64/darktable/plugins/libbasecurve.so
/usr/lib64/darktable/plugins/libbilat.so
/usr/lib64/darktable/plugins/libbilateral.so
/usr/lib64/darktable/plugins/libbloom.so
/usr/lib64/darktable/plugins/libborders.so
/usr/lib64/darktable/plugins/libcacorrect.so
/usr/lib64/darktable/plugins/libchannelmixer.so
/usr/lib64/darktable/plugins/libclahe.so
/usr/lib64/darktable/plugins/libclipping.so
/usr/lib64/darktable/plugins/libcolisa.so
/usr/lib64/darktable/plugins/libcolorbalance.so
/usr/lib64/darktable/plugins/libcolorchecker.so
/usr/lib64/darktable/plugins/libcolorcontrast.so
/usr/lib64/darktable/plugins/libcolorcorrection.so
/usr/lib64/darktable/plugins/libcolorin.so
/usr/lib64/darktable/plugins/libcolorize.so
/usr/lib64/darktable/plugins/libcolormapping.so
/usr/lib64/darktable/plugins/libcolorout.so
/usr/lib64/darktable/plugins/libcolorreconstruct.so
/usr/lib64/darktable/plugins/libcolortransfer.so
/usr/lib64/darktable/plugins/libcolorzones.so
/usr/lib64/darktable/plugins/libdefringe.so
/usr/lib64/darktable/plugins/libdemosaic.so
/usr/lib64/darktable/plugins/libdenoiseprofile.so
/usr/lib64/darktable/plugins/libdither.so
/usr/lib64/darktable/plugins/libequalizer.so
/usr/lib64/darktable/plugins/libexposure.so
/usr/lib64/darktable/plugins/libfinalscale.so
/usr/lib64/darktable/plugins/libflip.so
/usr/lib64/darktable/plugins/libgamma.so
/usr/lib64/darktable/plugins/libglobaltonemap.so
/usr/lib64/darktable/plugins/libgraduatednd.so
/usr/lib64/darktable/plugins/libgrain.so
/usr/lib64/darktable/plugins/libhighlights.so
/usr/lib64/darktable/plugins/libhighpass.so
/usr/lib64/darktable/plugins/libhotpixels.so
/usr/lib64/darktable/plugins/libinvert.so
/usr/lib64/darktable/plugins/liblens.so
/usr/lib64/darktable/plugins/liblevels.so
/usr/lib64/darktable/plugins/libliquify.so
/usr/lib64/darktable/plugins/liblowlight.so
/usr/lib64/darktable/plugins/liblowpass.so
/usr/lib64/darktable/plugins/libmonochrome.so
/usr/lib64/darktable/plugins/libnlmeans.so
/usr/lib64/darktable/plugins/liboverexposed.so
/usr/lib64/darktable/plugins/libprofile_gamma.so
/usr/lib64/darktable/plugins/librawdenoise.so
/usr/lib64/darktable/plugins/librawoverexposed.so
/usr/lib64/darktable/plugins/librawprepare.so
/usr/lib64/darktable/plugins/librelight.so
/usr/lib64/darktable/plugins/librotatepixels.so
/usr/lib64/darktable/plugins/libscalepixels.so
/usr/lib64/darktable/plugins/libshadhi.so
/usr/lib64/darktable/plugins/libsharpen.so
/usr/lib64/darktable/plugins/libsoften.so
/usr/lib64/darktable/plugins/libsplittoning.so
/usr/lib64/darktable/plugins/libspots.so
/usr/lib64/darktable/plugins/libtemperature.so
/usr/lib64/darktable/plugins/libtonecurve.so
/usr/lib64/darktable/plugins/libtonemap.so
/usr/lib64/darktable/plugins/libvelvia.so
/usr/lib64/darktable/plugins/libvibrance.so
/usr/lib64/darktable/plugins/libvignette.so
/usr/lib64/darktable/plugins/libwatermark.so
/usr/lib64/darktable/plugins/libzonesystem.so
/usr/lib64/darktable/plugins/lighttable/libbackgroundjobs.so
/usr/lib64/darktable/plugins/lighttable/libcollect.so
/usr/lib64/darktable/plugins/lighttable/libcolorlabels.so
/usr/lib64/darktable/plugins/lighttable/libcolorpicker.so
/usr/lib64/darktable/plugins/lighttable/libcopy_history.so
/usr/lib64/darktable/plugins/lighttable/libdarktable_label.so
/usr/lib64/darktable/plugins/lighttable/libexport.so
/usr/lib64/darktable/plugins/lighttable/libfilmstrip.so
/usr/lib64/darktable/plugins/lighttable/libfilter.so
/usr/lib64/darktable/plugins/lighttable/libgeotagging.so
/usr/lib64/darktable/plugins/lighttable/libglobal_toolbox.so
/usr/lib64/darktable/plugins/lighttable/libhinter.so
/usr/lib64/darktable/plugins/lighttable/libhistogram.so
/usr/lib64/darktable/plugins/lighttable/libhistory.so
/usr/lib64/darktable/plugins/lighttable/libimage.so
/usr/lib64/darktable/plugins/lighttable/libimport.so
/usr/lib64/darktable/plugins/lighttable/liblighttable_mode.so
/usr/lib64/darktable/plugins/lighttable/libmasks.so
/usr/lib64/darktable/plugins/lighttable/libmetadata.so
/usr/lib64/darktable/plugins/lighttable/libmetadata_view.so
/usr/lib64/darktable/plugins/lighttable/libmodule_toolbox.so
/usr/lib64/darktable/plugins/lighttable/libmodulegroups.so
/usr/lib64/darktable/plugins/lighttable/libmodulelist.so
/usr/lib64/darktable/plugins/lighttable/libnavigation.so
/usr/lib64/darktable/plugins/lighttable/libratings.so
/usr/lib64/darktable/plugins/lighttable/librecentcollect.so
/usr/lib64/darktable/plugins/lighttable/libselect.so
/usr/lib64/darktable/plugins/lighttable/libsession.so
/usr/lib64/darktable/plugins/lighttable/libsnapshots.so
/usr/lib64/darktable/plugins/lighttable/libstyles.so
/usr/lib64/darktable/plugins/lighttable/libtagging.so
/usr/lib64/darktable/plugins/lighttable/libview_toolbox.so
/usr/lib64/darktable/plugins/lighttable/libviewswitcher.so
/usr/lib64/darktable/views/libdarkroom.so
/usr/lib64/darktable/views/libknight.so
/usr/lib64/darktable/views/liblighttable.so
/usr/lib64/darktable/views/libslideshow.so

%files locales -f darktable.lang
%defattr(-,root,root,-)

