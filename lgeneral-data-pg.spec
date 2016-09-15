Summary:	Panzer General game data files for LGeneral game
Summary(pl.UTF-8):	Pliki danych gry Panzer General dla gry LGeneral
Name:		lgeneral-data-pg
Version:	0
Release:	1
# (not real license: material is copyrighted and used to be commercially available,
#  but now copyright owner is no longer interested)
License:	"abandonware"
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/lgeneral/pg-data.tar.gz
# Source0-md5:	40c4be23f60d1dc732aabe13b58fc5e3
URL:		http://lgames.sourceforge.net/LGeneral
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains Panzer General data files for the game.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera pliki z danymi Panzer General dla tej gry.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -r pg-data $RPM_BUILD_ROOT%{_datadir}/lgeneral
%{__rm} $RPM_BUILD_ROOT%{_datadir}/lgeneral/pg-data/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc pg-data/README
%{_datadir}/lgeneral/pg-data
