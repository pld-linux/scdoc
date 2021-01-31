Summary:	Simple man page generator
Name:		scdoc
Version:	1.11.1
Release:	1
License:	MIT
Group:		Applications
Source0:	https://git.sr.ht/~sircmpwn/scdoc/archive/%{version}.tar.gz
# Source0-md5:	ce8369cb5d2406786f61cf805ceae66f
URL:		https://git.sr.ht/~sircmpwn/scdoc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scdoc is a simple man page generator for POSIX systems written in C99.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -DVERSION='\"%{version}\"'" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX="%{_prefix}" \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	PCDIR=$RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/scdoc
%{_mandir}/man1/scdoc.1*
%{_mandir}/man5/scdoc.5*
%{_pkgconfigdir}/scdoc.pc
