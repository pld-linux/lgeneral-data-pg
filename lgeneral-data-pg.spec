#
# Conditional build:
%bcond_without	convert		# Convert data to LGeneral format
#
Summary:	Panzer General game data files for LGeneral game
Summary(pl.UTF-8):	Pliki danych gry Panzer General dla gry LGeneral
Name:		lgeneral-data-pg
Version:	0
Release:	2
# (not real license: material is copyrighted and used to be commercially available,
#  but now copyright owner is no longer interested)
License:	"abandonware"
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/lgeneral/pg-data.tar.gz
# Source0-md5:	40c4be23f60d1dc732aabe13b58fc5e3
URL:		http://lgames.sourceforge.net/LGeneral
%if %{with convert}
BuildRequires:	lgeneral-tools
BuildRequires:	xorg-xserver-Xvfb
%endif
Requires:	lgeneral >= 1.3
Obsoletes:	lgeneral-data < 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains Panzer General data files for the game.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera pliki z danymi Panzer General dla tej gry.

%package source
Summary:	Panzer General game data in original form
Summary(pl.UTF-8):	Dane gry Panzer General w oryginalnej postaci
Group:		Applications/Games
Suggests:	lgeneral-tools

%description source
Panzer General game data in original form.

%description source -l pl.UTF-8
Dane gry Panzer General w oryginalnej postaci.

%prep
%setup -q -c

%build
%if %{with convert}
install -d lgeneral/{gfx/{flags,terrain,units},maps,nations,scenarios,sounds,units}

DISP=$(( (RANDOM % 87) + 31 ))
/usr/bin/Xvfb :$DISP &
XVFB_PID=$!
sleep 1
[ -n "$XVFB_PID" ] || exit 1
DISPLAY=:$DISP lgc-pg -s pg-data -d lgeneral
kill $XVFB_PID
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -r pg-data $RPM_BUILD_ROOT%{_datadir}/lgeneral
%{__rm} $RPM_BUILD_ROOT%{_datadir}/lgeneral/pg-data/README

%if %{with convert}
cp -pr lgeneral/* $RPM_BUILD_ROOT%{_datadir}/lgeneral
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with convert}
%files
%defattr(644,root,root,755)
%doc pg-data/README
%{_datadir}/lgeneral/gfx/flags/pg.bmp
%{_datadir}/lgeneral/gfx/terrain/pg
%{_datadir}/lgeneral/gfx/units/pg*.bmp
%{_datadir}/lgeneral/maps/pg
%{_datadir}/lgeneral/maps/pg.tdb
%{_datadir}/lgeneral/nations/pg.ndb
%{_datadir}/lgeneral/scenarios/pg
%{_datadir}/lgeneral/sounds/pg
%{_datadir}/lgeneral/units/pg.udb
%endif

%files source
%defattr(644,root,root,755)
%doc pg-data/README
%{_datadir}/lgeneral/pg-data
