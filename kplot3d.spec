Summary: Kplot3d is KDE version of tool for building 3d surface of function z = f(x,y).
Name: kplot3d
Version: 0.70
Release: 1
Copyright: GPL
Group: Applications/Graphics
Source: kplot3d-0.70.tar.gz
%description

Kplot3d is tool for building 3d surface of function z = f(x,y).
Support sdaded and grid ( with erasing of invisible lines ) modes,
fast realtaime surface rotation,
printing result image, save image or data (in xyz format) to local file.
For KDE.					

%prep
%setup

%build
./configure
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
cd po
make 
cd ..

%install
make install
cd po 
make install

%files
/usr/share/doc/HTML/en/kplot3d
/usr/share/applnk/Applications/kplot3d.kdelnk
/usr/share/icons/kplot3d.xpm
/usr/share/icons/mini/kplot3d.xpm
/usr/share/locale/ru/LC_MESSAGES/kplot3d.mo
/usr/bin/kplot3d
/usr/share/apps/kplot3d/pics/intro.jpg
