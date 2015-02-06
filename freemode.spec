%define name 	freemode
%define version 3.0
%define release 8

Summary: Alternative UI for freeplayer
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group:   Video
Url:     http://www.moktoipas.com/freemode/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch

Requires:	freeplayer-common

%description
Alternative UI for freeplayer

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
for i in config settings options; do
  mv $i.html $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx/$i-freemode.html
done
cp -rp *.html $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
cp -rp *.m3u $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
cp -rp aides $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
cp -rp freezic $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
cp -rp radios $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
cp -rp tele $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
cp -rp favoris $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx
cp -rp imgs $RPM_BUILD_ROOT/%{_datadir}/freeplayer/http-fbx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENCE.TXT
%{_datadir}/freeplayer/http-fbx




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-7mdv2011.0
+ Revision: 618342
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 3.0-6mdv2010.0
+ Revision: 428890
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.0-5mdv2009.0
+ Revision: 245397
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.0-3mdv2008.1
+ Revision: 136423
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import freemode


* Fri Apr  7 2006 Jerome Martin <jmartin@mandriva.org> 3.0-3mdk
- Updated with new freeplayer-common package

* Thu Feb  2 2006 Jerome Martin <jmartin@mandriva.org> 3.0-2mdk
- Fixed

* Mon Dec 19 2005 Jerome Martin <jmartin@mandriva.org> 3.0-1mdk
- Initial version

