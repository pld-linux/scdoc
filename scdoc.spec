Summary:	Simple man page generator
Name:		scdoc
Version:	1.11.2
Release:	1
License:	MIT
Group:		Applications
Source0:	https://git.sr.ht/~sircmpwn/scdoc/archive/%{version}.tar.gz
# Source0-md5:	0f6e8b9bb741f52d975081784757078b
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
