# can not trace the source or homepage symbianflo
# eventually to be flagged as dead project

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

Buildarch: noarch

Requires:	freeplayer-common

%description
Alternative UI for freeplayer

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/freeplayer/http-fbx

for i in config settings options; do
  mv $i.html %{buildroot}%{_datadir}/freeplayer/http-fbx/$i-freemode.html
done

cp -rp *.html %{buildroot}%{_datadir}/freeplayer/http-fbx
cp -rp *.m3u %{buildroot}%{_datadir}/freeplayer/http-fbx
cp -rp aides %{buildroot}%{_datadir}/freeplayer/http-fbx
cp -rp freezic %{buildroot}%{_datadir}/freeplayer/http-fbx
cp -rp radios %{buildroot}%{_datadir}/freeplayer/http-fbx
cp -rp tele %{buildroot}%{_datadir}/freeplayer/http-fbx
cp -rp favoris %{buildroot}%{_datadir}/freeplayer/http-fbx
cp -rp imgs %{buildroot}%{_datadir}/freeplayer/http-fbx



%files
%doc LICENCE.TXT
%{_datadir}/freeplayer/http-fbx


