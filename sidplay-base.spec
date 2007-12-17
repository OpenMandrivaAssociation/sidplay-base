%define name sidplay-base
%define version 1.0.9
%define release %mkrel 5


Summary: A Commodore 64 music player and SID chip emulator
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
URL: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/linux.html
Group: Sound
Source: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tar.bz2
Patch: sidplay-base-1.0.9-tsid.patch.bz2
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

