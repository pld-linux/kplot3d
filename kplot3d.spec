Summary:	Kplot3d is KDE version of tool for building 3d surface of function z = f(x,y)
Summary(pl):	Kplot3d jest wersj± KDE narzêdzia do rysowania w 3D powierzchni z = f(x,y)
Name:		kplot3d
Version:	0.70
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://members.nbci.com/kplot3d/%{name}-%{version}.tar.gz
URL:		http://members.nbci.com/kplot3d/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
./configure
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"
cd po
%{__make} 
cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install
cd po 
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/doc/HTML/en/kplot3d
%{_applnkdir}/Applications/kplot3d.kdelnk
%{_datadir}/icons/kplot3d.xpm
%{_datadir}/icons/mini/kplot3d.xpm
%{_datadir}/locale/ru/LC_MESSAGES/kplot3d.mo
%attr(755,root,root) %{_bindir}/kplot3d
%{_datadir}/apps/kplot3d/pics/intro.jpg
