Summary:	Kplot3d is KDE version of tool for building 3d surface of function z = f(x,y)
Summary(pl):	Kplot3d jest wersj± KDE narzêdzia do rysowania w 3D powierzchni z = f(x,y)
Name:		kplot3d
Version:	0.70
Release:	1
License:	GPL
Group:		Applications/Graphics
# http://members.nbci.com/kplot3d/ is dead
# http://members.xoom.com/kplot3d/ too
Source0:	http://ftp.kde.com/Math_Science/Plotting/Kplot3d/%{name}-%{version}.tar.gz
# Source0-md5:	d519ba0f0c7c84961bc1355c48d0e75d
#URL:		http://members.nbci.com/kplot3d/
BuildRequires:	kdelibs-devel < 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Kplot3d is tool for building 3d surface of function z = f(x,y).
Support shaded and grid (with erasing of invisible lines) modes, fast
realtaime surface rotation, printing result image, save image or data
(in xyz format) to local file. For KDE.

%description -l pl
Kplot3d jest narzêdziem KDE do tworzenia wykresów 3D powierzchni
zadanych funkcj± z = f(x,y). Tryb cieniowany i siatkowy (z usuwaniem
niewidocznych linii), szybkie obroty powierzchni, drukowanie
wynikowego obrazka, zapisywanie do pliku w formacie xyz.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13 \
	--disable-path-check

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplot3d
%{_applnkdir}/Applications/kplot3d.kdelnk
%{_pixmapsdir}/kplot3d.xpm
%{_pixmapsdir}/mini/kplot3d.xpm
%{_datadir}/apps/kplot3d
