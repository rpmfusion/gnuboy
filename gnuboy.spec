Summary: Nintendo GameBoy Color emulator
Name: gnuboy
Version: 1.0.3
Release: 15%{?dist}
License: GPLv2
Group: Applications/Emulators
URL: http://brightrain.aerifal.cx/~laguna/
Source: http://brightrain.aerifal.cx/~laguna/src/%{name}-%{version}.tar.gz
Patch0: gnuboy-1.0.3-s64.patch
Patch1: gnuboy-1.0.3-xgnuboy.patch
Patch2: gnuboy-1.0.3-manpages.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel >= 1.2.0
BuildRequires: libXt-devel
%ifarch %{ix86} x86_64
BuildRequires: svgalib-devel
%endif

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

%package svgalib
Summary: Nintendo GameBoy Color emulator (svgalib version)
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

%description svgalib
gnuboy (all lowercase) is a portable program for emulating the Nintendo
GameBoy Color software platform. gnuboy is Free Software, distributed
under the terms of the GNU General Public License. Our goal is to provide
a great emulator that runs on many platforms and is accessible for
everyone's enjoyment.

This is the svgalib version.

%prep
%setup -q
%ifarch %{ix86} ppc
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

%build
%ifarch %{ix86} x86_64
%configure --disable-arch --disable-optimize --disable-asm \
	--with-sdl --with-x --with-fb --with-svgalib
%else
%configure --disable-arch --disable-optimize --disable-asm \
	--with-sdl --with-x --with-fb
%endif
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

#install man pages
install -d %{buildroot}%_mandir/man1
install -m 644 sdlgnuboy.1 %{buildroot}%{_mandir}/man1
install -m 644 xgnuboy.1 %{buildroot}%{_mandir}/man1
%ifarch %{ix86} x86_64
install -m 644 sgnuboy.1 %{buildroot}%{_mandir}/man1
%endif

%clean
rm -rf %{buildroot}

%files sdl
%defattr(-, root, root)
%{_bindir}/sdlgnuboy
%{_mandir}/man1/sdlgnuboy.1*
%doc COPYING README 
%doc docs/{CHANGES,CONFIG,CREDITS,FAQ,LIBERTY,README.old,WHATSNEW}
%doc etc/*.rc

%files x
%defattr(-, root, root)
%{_bindir}/xgnuboy
%{_mandir}/man1/xgnuboy.1*
%doc COPYING README
%doc docs/{CHANGES,CONFIG,CREDITS,FAQ,LIBERTY,README.old,WHATSNEW}
%doc etc/*.rc

%files fb
%defattr(-, root, root)
%{_bindir}/fbgnuboy
%doc COPYING README
%doc docs/{CHANGES,CONFIG,CREDITS,FAQ,LIBERTY,README.old,WHATSNEW}
%doc etc/*.rc

%ifarch %{ix86} x86_64
%files svgalib
%defattr(-, root, root)
%{_bindir}/sgnuboy
%{_mandir}/man1/sgnuboy.1*
%doc COPYING README
%doc docs/{CHANGES,CONFIG,CREDITS,FAQ,LIBERTY,README.old,WHATSNEW}
%doc etc/*.rc
%endif

%changelog
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

