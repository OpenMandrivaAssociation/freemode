%define name 	freemode
%define version 3.0
%define release %mkrel 3

Summary: Alternative UI for freeplayer
Name: 	 %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group:   Video
Url:     http://www.moktoipas.com/freemode/
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


