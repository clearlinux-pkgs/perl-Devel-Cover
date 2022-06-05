#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Cover
Version  : 1.37
Release  : 35
URL      : https://cpan.metacpan.org/authors/id/P/PJ/PJCJ/Devel-Cover-1.37.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PJ/PJCJ/Devel-Cover-1.37.tar.gz
Summary  : 'Code coverage metrics for Perl'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-Cover-bin = %{version}-%{release}
Requires: perl-Devel-Cover-man = %{version}-%{release}
Requires: perl-Devel-Cover-perl = %{version}-%{release}
Requires: perl(B::Debug)
Requires: perl(Sereal::Decoder)
Requires: perl(Sereal::Encoder)
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Debug)
BuildRequires : perl(HTML::Entities)

%description
# Devel::Cover
## Code coverage metrics for Perl
This module provides code coverage metrics for Perl.  Code coverage metrics
describe how thoroughly tests exercise code.  By using Devel::Cover you can
discover areas of code not exercised by your tests and determine which tests to
create to increase coverage.  Code coverage can be considered an indirect
measure of quality.

%package bin
Summary: bin components for the perl-Devel-Cover package.
Group: Binaries

%description bin
bin components for the perl-Devel-Cover package.


%package dev
Summary: dev components for the perl-Devel-Cover package.
Group: Development
Requires: perl-Devel-Cover-bin = %{version}-%{release}
Provides: perl-Devel-Cover-devel = %{version}-%{release}
Requires: perl-Devel-Cover = %{version}-%{release}

%description dev
dev components for the perl-Devel-Cover package.


%package man
Summary: man components for the perl-Devel-Cover package.
Group: Default

%description man
man components for the perl-Devel-Cover package.


%package perl
Summary: perl components for the perl-Devel-Cover package.
Group: Default
Requires: perl-Devel-Cover = %{version}-%{release}

%description perl
perl components for the perl-Devel-Cover package.


%prep
%setup -q -n Devel-Cover-1.37
cd %{_builddir}/Devel-Cover-1.37

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cover
/usr/bin/cpancover
/usr/bin/gcov2perl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Cover.3
/usr/share/man/man3/Devel::Cover::Annotation::Git.3
/usr/share/man/man3/Devel::Cover::Annotation::Random.3
/usr/share/man/man3/Devel::Cover::Annotation::Svk.3
/usr/share/man/man3/Devel::Cover::Branch.3
/usr/share/man/man3/Devel::Cover::Collection.3
/usr/share/man/man3/Devel::Cover::Condition.3
/usr/share/man/man3/Devel::Cover::Condition_and_2.3
/usr/share/man/man3/Devel::Cover::Condition_and_3.3
/usr/share/man/man3/Devel::Cover::Condition_or_2.3
/usr/share/man/man3/Devel::Cover::Condition_or_3.3
/usr/share/man/man3/Devel::Cover::Condition_xor_4.3
/usr/share/man/man3/Devel::Cover::Criterion.3
/usr/share/man/man3/Devel::Cover::DB.3
/usr/share/man/man3/Devel::Cover::DB::Digests.3
/usr/share/man/man3/Devel::Cover::DB::File.3
/usr/share/man/man3/Devel::Cover::DB::IO.3
/usr/share/man/man3/Devel::Cover::DB::IO::Base.3
/usr/share/man/man3/Devel::Cover::DB::IO::JSON.3
/usr/share/man/man3/Devel::Cover::DB::IO::Sereal.3
/usr/share/man/man3/Devel::Cover::DB::IO::Storable.3
/usr/share/man/man3/Devel::Cover::DB::Structure.3
/usr/share/man/man3/Devel::Cover::Dumper.3
/usr/share/man/man3/Devel::Cover::Html_Common.3
/usr/share/man/man3/Devel::Cover::Op.3
/usr/share/man/man3/Devel::Cover::Pod.3
/usr/share/man/man3/Devel::Cover::Report::Compilation.3
/usr/share/man/man3/Devel::Cover::Report::Html.3
/usr/share/man/man3/Devel::Cover::Report::Html_basic.3
/usr/share/man/man3/Devel::Cover::Report::Html_minimal.3
/usr/share/man/man3/Devel::Cover::Report::Html_subtle.3
/usr/share/man/man3/Devel::Cover::Report::Json.3
/usr/share/man/man3/Devel::Cover::Report::Sort.3
/usr/share/man/man3/Devel::Cover::Report::Text.3
/usr/share/man/man3/Devel::Cover::Report::Text2.3
/usr/share/man/man3/Devel::Cover::Report::Vim.3
/usr/share/man/man3/Devel::Cover::Statement.3
/usr/share/man/man3/Devel::Cover::Subroutine.3
/usr/share/man/man3/Devel::Cover::Test.3
/usr/share/man/man3/Devel::Cover::Time.3
/usr/share/man/man3/Devel::Cover::Truth_Table.3
/usr/share/man/man3/Devel::Cover::Tutorial.3
/usr/share/man/man3/Devel::Cover::Util.3
/usr/share/man/man3/Devel::Cover::Web.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cover.1
/usr/share/man/man1/cpancover.1
/usr/share/man/man1/gcov2perl.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
