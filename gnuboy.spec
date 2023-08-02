Summary: Nintendo GameBoy Color emulator
Name: gnuboy
Version: 1.0.3
Release: 31%{?dist}
License: GPLv2
URL: http://brightrain.aerifal.cx/~laguna/
Source: http://brightrain.aerifal.cx/~laguna/src/%{name}-%{version}.tar.gz
Patch0: gnuboy-1.0.3-s64.patch
Patch1: gnuboy-1.0.3-xgnuboy.patch
Patch2: gnuboy-1.0.3-manpages.patch
BuildRequires: SDL-devel >= 1.2.0
BuildRequires: libXext-devel
BuildRequires: libXt-devel
BuildRequires: gcc

%package sdl
Summary: Nintendo GameBoy Color emulator (SDL version)
Group: Applications/Emulators
Obsoletes: gnuboy < 1.0.3-12
Provides: gnuboy = %{version}-%{release}

%package x
Summary: Nintendo GameBoy Color emulator (X version)
Group: Applications/Emulators

%package fb
Summary: Nintendo GameBoy Color emulator (frame buffer version)
Group: Applications/Emulators

%description
gnuboy (all lowercase) is a portable program for emulating the Nintendo
GameBoy Color software platform. gnuboy is Free Software, distributed
under the terms of the GNU General Public License. Our goal is to provide
a great emulator that runs on many platforms and is accessible for
everyone's enjoyment.

%description sdl
gnuboy (all lowercase) is a portable program for emulating the Nintendo
GameBoy Color software platform. gnuboy is Free Software, distributed
under the terms of the GNU General Public License. Our goal is to provide
a great emulator that runs on many platforms and is accessible for
everyone's enjoyment.

This is the SDL version.

%description x
gnuboy (all lowercase) is a portable program for emulating the Nintendo
GameBoy Color software platform. gnuboy is Free Software, distributed
under the terms of the GNU General Public License. Our goal is to provide
a great emulator that runs on many platforms and is accessible for
everyone's enjoyment.

This is the X version.

%description fb
gnuboy (all lowercase) is a portable program for emulating the Nintendo
GameBoy Color software platform. gnuboy is Free Software, distributed
under the terms of the GNU General Public License. Our goal is to provide
a great emulator that runs on many platforms and is accessible for
everyone's enjoyment.

This is the frame buffer version.


%prep
%setup -q
%ifarch %{ix86} ppc
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

%build
%configure --disable-arch --disable-optimize --disable-asm \
	--with-sdl --with-x --with-fb
%make_build

%install
%makeinstall

#install man pages
install -d %{buildroot}%_mandir/man1
install -m 644 sdlgnuboy.1 %{buildroot}%{_mandir}/man1
install -m 644 xgnuboy.1 %{buildroot}%{_mandir}/man1

%files sdl
%{_bindir}/sdlgnuboy
%{_mandir}/man1/sdlgnuboy.1*
%license COPYING
%doc README
%doc docs/{CHANGES,CONFIG,CREDITS,FAQ,LIBERTY,README.old,WHATSNEW}
%doc etc/*.rc

%files x
%{_bindir}/xgnuboy
%{_mandir}/man1/xgnuboy.1*
%license COPYING
%doc README
%doc docs/{CHANGES,CONFIG,CREDITS,FAQ,LIBERTY,README.old,WHATSNEW}
%doc etc/*.rc

%files fb
%{_bindir}/fbgnuboy
%license COPYING
%doc README
%doc docs/{CHANGES,CONFIG,CREDITS,FAQ,LIBERTY,README.old,WHATSNEW}
%doc etc/*.rc

%changelog
* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 24 2020 Andrea Musuruane <musuruan@gmail.com> - 1.0.3-25
- Dropped svgalib dependency (BZ #5567)
- Clean up spec file

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.3-16
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0.3-14
- rebuild for new F11 features

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.0.3-13
- rebuild for buildsys cflags issue

* Fri Oct 05 2007 Andrea Musuruane <musuruan@gmail.com> 1.0.3-12
- bumping release to be higher than freshrpms (RPM Fusion merge)
- changed license due to new Fedora guidelines
- removed %%{?dist} tag from changelog

* Mon Apr 30 2007 Andrea Musuruane <musuruan@gmail.com> 1.0.3-5
- patch to force the definition of __s64 does not apply to x86_64

* Sat Apr 28 2007 Andrea Musuruane <musuruan@gmail.com> 1.0.3-4
- svgalib is only available to x86 and x64_64 archs.

* Wed Apr 25 2007 Andrea Musuruane <musuruan@gmail.com> 1.0.3-3
- added missing libXt-devel to BR

* Fri Apr 20 2007 Andrea Musuruane <musuruan@gmail.com> 1.0.3-2
- enabled X, fb and svgalib versions
- split versions into different subpackages
- added a patch by Nicholas J. Kain to run xgnuboy
- added man pages from Debian
- added patch to force definition of __s64 since when using -ansi on i386 it
  doesn't get defined anymore (from freshrpms.net package)

* Fri Oct 20 2006 Andrea Musuruane <musuruan@gmail.com> 1.0.3-1
- initial package

