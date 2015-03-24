%global vendor MidoNet
%global srcname networking-midonet
%global docpath doc/build/html

Name:           python-%{srcname}		
Version:        2015.2.2
Release:	    1%{?dist}
Summary:        %{vendor} OpenStack Neutron driver	

License:        ASL 2.0
URL:	        https://pypi.python.org/pypi/%{srcname}
Source0:	    https://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	python2-devel
BuildRequires:	python-oslolog
BuildRequires:  python-neutron
Requires:	    python-babel
Requires:       python-pbr

%description
This package provides %{vendor} networking driver for OpenStack Neutron


%prep
%setup -q -n %{srcname}-%{upstream_version}


%build
%configure
rm requirements.txt test-requirements.txt
%{__python2} setup.py build
%{__python2} setup.py build_sphinx
rm %{docpath}/.buildinfo


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT


%files
%doc LICENSE
%doc %{docpath}
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
