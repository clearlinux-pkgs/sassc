#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sassc
Version  : 3.6.1
Release  : 6
URL      : https://github.com/sass/sassc/archive/3.6.1/sassc-3.6.1.tar.gz
Source0  : https://github.com/sass/sassc/archive/3.6.1/sassc-3.6.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: sassc-bin = %{version}-%{release}
Requires: sassc-license = %{version}-%{release}
BuildRequires : libsass
BuildRequires : libsass-dev

%description
SassC
=======
[![Unix CI](https://secure.travis-ci.org/sass/sassc.svg?branch=master)](http://travis-ci.org/sass/sassc)
[![Windows CI](https://ci.appveyor.com/api/projects/status/github/sass/sassc?svg=true)](https://ci.appveyor.com/project/sass/sassc/branch/master)

%package bin
Summary: bin components for the sassc package.
Group: Binaries
Requires: sassc-license = %{version}-%{release}

%description bin
bin components for the sassc package.


%package license
Summary: license components for the sassc package.
Group: Default

%description license
license components for the sassc package.


%prep
%setup -q -n sassc-3.6.1
cd %{_builddir}/sassc-3.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586220654
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1586220654
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sassc
cp %{_builddir}/sassc-3.6.1/LICENSE %{buildroot}/usr/share/package-licenses/sassc/4d640cc322117dec7f97632e6ed4319131a16ad2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sassc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sassc/4d640cc322117dec7f97632e6ed4319131a16ad2
