Summary:	Simple man page generator
Summary(pl.UTF-8):	Prosty generator stron podręcznika man
Name:		scdoc
Version:	1.11.3
Release:	1
License:	MIT
Group:		Applications/Text
Source0:	https://git.sr.ht/~sircmpwn/scdoc/archive/%{version}.tar.gz
# Source0-md5:	4e0928d10d23d24f2c1eb0f311ceef14
URL:		https://git.sr.ht/~sircmpwn/scdoc/
BuildRequires:	gcc >= 5:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scdoc is a simple man page generator for POSIX systems written in C99.

%description -l pl.UTF-8
scdoc to prosty generator stron podręcznika man dla systemów
POSIX-owych, napisany w C99.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -DVERSION='\"%{version}\"' -Wno-error=unused-variable -Wno-error=unused-but-set-variable" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX="%{_prefix}" \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir} \
	PCDIR=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/scdoc
%{_mandir}/man1/scdoc.1*
%{_mandir}/man5/scdoc.5*
%{_pkgconfigdir}/scdoc.pc
