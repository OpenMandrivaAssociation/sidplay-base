%define name sidplay-base
%define version 1.0.9
%define release 7


Summary: A Commodore 64 music player and SID chip emulator
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
URL: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/linux.html
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tar.bz2
Patch: sidplay-base-1.0.9-tsid.patch.bz2
Patch1: sidplay-base-1.0.9-gcc4.4.patch
BuildRequires: libsidplay-devel < 2
BuildRequires:  tsid-devel >= 0.7
BuildRequires: automake1.4

%description
SIDPLAY is basically a music player. It emulates the Sound Interface
Device (SID) chip and the microprocessor unit of the Commodore 64
computer, so it can load and execute C64 machine code programs which
produce music or sound. Normally these are short pieces of code
pulled out of Commodore games or demonstration programs. Using
SIDPLAY, you can listen to thousands of old and new C64 sound files
by infamous artists such as Hubbard and Paul Norman! In emulation,
their music lives on...

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch -p1 -b .tsid
%patch1 -p1

%build
rm -f configure
automake-1.4
autoconf
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING POINTER audio/README
%{_bindir}/*



%changelog
* Fri May 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.9-6mdv2010.0
+ Revision: 378683
- fix license
- fix build with gcc 4.4

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.9-5mdv2008.1
+ Revision: 127249
- kill re-definition of %%buildroot on Pixel's request
- kill icon tag (unused and breaks build with iurt)
- use %%mkrel
- import sidplay-base


* Wed Jul 06 2005 Lenny Cartier <lenny@mandriva.com> 1.0.9-5mdk
- rebuild

* Sun Jun  6 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.9-4mdk
- fix build
- fix URLs
- new g++

* Tue Oct  7 2003 Götz Waschk <waschk@linux-mandrake.com> 1.0.9-3mdk
- fix buildrequires

* Sat Dec 21 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.9-2mdk
- new tsid

* Tue Nov  5 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.9-1mdk
- rediff patch
- new version

* Fri Aug 16 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.8-6mdk
- rebuild with gcc 3.2-0.2mdk

* Wed Jul 31 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.8-4mdk
- reenable tsid

* Mon Jul 29 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.8-3mdk
- gcc 3.2 build

* Sun May 26 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.8-2mdk
- gcc 3.1
- temporary disable tsid support

* Wed Mar 13 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.8-1mdk
- update patch
- 1.0.8

* Sun Mar 10 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.7-2mdk
- rebuild with new libsidplay

* Sat Mar  9 2002 Götz Waschk <waschk@linux-mandrake.com> 1.0.7-1mdk
- 1.0.7

* Tue Dec 18 2001 Götz Waschk <waschk@linux-mandrake.com> 1.0.5-1mdk
- 1.0.5

* Tue Nov  6 2001 Götz Waschk <waschk@linux-mandrake.com> 1.0.4-4mdk
- s/Copyright/License/
- added support for tsid

* Thu Jan 18 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-3mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- updated depencies for libsidplay1

* Mon Sep 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-2mdk
- macros
- BM

* Fri Jul 14 2000 Götz Waschk <goetz@linux-mandrake.com> 1.0.4-1mdk
- initial mandrake release
