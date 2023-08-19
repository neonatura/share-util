Name:           share-util
Version:        6.5
Release:        1%{?dist}
Summary:        Utility applications for the share library suite.

Group:          System Environment/Libraries
License:        GPLv3+
URL:            http://www.sharelib.net/
Source0:        ftp://ftp.sharelib.net/release/share-util/share-util-6.5.tar.gz

#BuildRequires:  gcc-java, java-1.8.0-openjdk-devel, swig, help2man, doxygen
#Requires:       java-1.8.0-openjdk

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/shattr
%{_bindir}/shcat
%{_bindir}/shcp
%{_bindir}/shdelta
%{_bindir}/shdiff
%{_bindir}/shinfo
%{_bindir}/shln
%{_bindir}/shls
%{_bindir}/shpasswd
%{_bindir}/shpatch
%{_bindir}/shpref
%{_bindir}/shrev
%{_bindir}/shrm
%{_bindir}/shstat
%{_bindir}/shcert
%{_bindir}/shdb
%{_bindir}/shfsck
%{_bindir}/shpkg
%{_bindir}/shalg
%{_bindir}/shgeo
%{_bindir}/shz
%{_bindir}/shapp
%{_mandir}/man1/shattr.1.gz
%{_mandir}/man1/shcat.1.gz
%{_mandir}/man1/shcp.1.gz
%{_mandir}/man1/shdelta.1.gz
%{_mandir}/man1/shdiff.1.gz
%{_mandir}/man1/shinfo.1.gz
%{_mandir}/man1/shalg.1.gz
%{_mandir}/man1/shgeo.1.gz
%{_mandir}/man1/shz.1.gz
%{_mandir}/man1/shln.1.gz
%{_mandir}/man1/shls.1.gz
%{_mandir}/man1/shpasswd.1.gz
%{_mandir}/man1/shpatch.1.gz
%{_mandir}/man1/shpref.1.gz
%{_mandir}/man1/shrev.1.gz
%{_mandir}/man1/shrm.1.gz
%{_mandir}/man1/shstat.1.gz
%{_mandir}/man1/shcert.1.gz
%{_mandir}/man1/shdb.1.gz
%{_mandir}/man1/shfsck.1.gz
%{_mandir}/man1/shpkg.1.gz



%changelog
*  Fri Aug 04 2023 Neo Natura <support@neo-natura.com> - 6.5
- The RPM release of utilities for the libshare software suite.
