%define module QWizard

Summary:	A Question and Answer Wizard
Name:		perl-%{module}
Version:	3.15
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HARDAKER/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n %{module}-%{version}

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

