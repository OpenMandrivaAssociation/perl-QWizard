%define upstream_name    QWizard
%define upstream_version 3.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A Question and Answer Wizard
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HARDAKER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
The QWizard module allows script authors to concentrate on the content of the
forms they want their users to fill in without worrying about the display. It
allows "Question Wizard" like interfaces to be very easily created and the
results of the input easily acted upon. Scripts written which are entirely
based on QWizard inputs are able to be run from the command line which will
show a Gtk2, Tk window or as a ReadLine interactive session or as a CGI script
without modification.  Script writers do not need to know which interface is
being used to display the resulting form(s) as it should be transparent to the
script itself.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

chmod 644 examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc CHANGES README examples
%{perl_vendorlib}/QWizard
%{perl_vendorlib}/QWizard.pm
%{perl_vendorlib}/QWizard_Widgets.pl
%{perl_vendorlib}/QWizard_Widgets.pod
%{perl_vendorlib}/auto/QWizard/Generator/autosplit.ix
%{_mandir}/*/*


%changelog
* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 3.150.0-1mdv2010.0
+ Revision: 410099
- rebuild using %%perl_convert_version

* Mon Sep 22 2008 Oden Eriksson <oeriksson@mandriva.com> 3.15-1mdv2009.0
+ Revision: 286512
- fix deps
- import perl-QWizard


* Sun Sep 21 2008 Oden Eriksson <oeriksson@mandriva.com> 3.15-1mdv2009.0
- initial Mandriva release
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel >= 2.6.2
BuildRequires:	pkgconfig
BuildRequires:	ctemplate-devel
BuildRequires:	libzip-devel
BuildRequires:	sigc++2.0-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libgnome2-devel
BuildRequires:	mysql-devel
BuildRequires:	lua-devel
