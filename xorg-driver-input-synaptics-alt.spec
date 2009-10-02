Summary:	XOrg/XFree86 input driver for Synaptics touchpads
Summary(pl.UTF-8):	Sterownik wejściowy XOrg/XFree86 do touchpadów Synaptics
Name:		xorg-driver-input-synaptics-alt
Version:	0.99.3
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://math.berkeley.edu/~vojta/xf86-input-synaptics-%{version}.tar.bz2
# Source0-md5:	ea67c9c3eb6a85125947672cde7d6727
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-xserver-server-devel
%requires_xorg_xserver_xinput
Requires:	xorg-driver-input-synaptics-alt = %{epoch}:%{version}-%{release}
Obsoletes:	X11-synaptics
ExcludeArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XFree86 input driver for Synaptics touchpad

%description -l pl.UTF-8
Sterownik wejściowy XFree86 do touchpada Synaptics.

%prep
%setup -q -n xf86-input-synaptics-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/input/*.so
%{_mandir}/man4/synaptics*
