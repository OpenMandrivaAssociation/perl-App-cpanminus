%define upstream_name    App-cpanminus
%define upstream_version 1.7004
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(App::cpanminus::script\\)'
%define __noautoprov 'perl\\(JSON.*|perl\\(CPAN.*|perl\\(Module.*|perl\\(HTTP.*|perl\\(Exporter.*|perl\\(File.*|perl\\(Parse.*|perl\\(String.*|perl\\(A\\)|perl\\(My\\)|perl\\(YourModule\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Get, unpack, build and install modules from CPAN

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Install)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(LWP)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
cpanminus is a script to get, unpack, build and install modules from CPAN.

Why? It's dependency free, requires zero configuration, and stands alone.
When running, it requires only 10MB of RAM.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_bindir}/cpanm
%{perl_vendorlib}/App
%{_mandir}/man1/cpanm.1*
%{_mandir}/man3/*


