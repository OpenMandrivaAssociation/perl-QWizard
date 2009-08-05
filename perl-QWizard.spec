%define upstream_name    QWizard
%define upstream_version 3.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A Question and Answer Wizard
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HARDAKER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-CGI
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README examples
%{perl_vendorlib}/QWizard
%{perl_vendorlib}/QWizard.pm
%{perl_vendorlib}/QWizard_Widgets.pl
%{perl_vendorlib}/QWizard_Widgets.pod
%{perl_vendorlib}/auto/QWizard/Generator/autosplit.ix
%{_mandir}/*/*
