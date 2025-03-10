Summary:	An extension to use emoji codes in your Sphinx documentation
Summary(pl.UTF-8):	Rozszerzenie umożliwiające używanie kodów emoji w dokumentacji generowanej Sphinksem
Name:		python3-sphinxemoji
Version:	0.2.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxemoji/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxemoji/sphinxemoji-%{version}.tar.gz
# Source0-md5:	b6acecfa315545218e1a1a7022a027d1
URL:		https://pypi.org/project/sphinxemoji/
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-modules >= 1:3
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An extension to use emoji codes in your Sphinx documentation.

%description -l pl.UTF-8
Rozszerzenie umożliwiające używanie kodów emoji w dokumentacji
generowanej Sphinksem.

%prep
%setup -q -n sphinxemoji-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/sphinxemoji
%{py3_sitescriptdir}/sphinxemoji-%{version}-py*.egg-info
