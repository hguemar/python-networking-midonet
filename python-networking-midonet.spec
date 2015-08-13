%global vendor  MidoNet
%global srcname networking-midonet

Name:           python-%{srcname}
version:        XXX
Release:        XXX
Summary:        %{vendor} OpenStack Neutron driver

License:        ASL 2.0
URL:            https://www.midonet.org/
Source0:        https://pypi.python.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       python-neutron
Conflicts:      python-neutron-plugin-midonet

%description
This package provides %{vendor} networking driver for OpenStack Neutron

%prep
%setup -q -n %{srcname}-%{upstream_version}

%build
CFLAGS="%{optflags}" %{__python2} setup.py build

%install
CFLAGS="%{optflags}" PBR_VERSION="%{version}" SKIP_PIP_INSTALL=1 %{__python2} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{python2_sitelib}/midonet
%{python2_sitelib}/networking_midonet-%{version}-py%{python2_version}.egg-info
%{_bindir}/midonet-db-manage

%changelog
