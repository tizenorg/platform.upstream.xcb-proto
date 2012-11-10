Name:         	xcb-proto 
Version:        1.8
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(xorg-macros)
Requires:	python-xcb-proto

%description
%{summary}.


%package -n python-xcb-proto
Summary:        Python libraries mandatory for XML-XCB Development
Group:          Development/Libraries/X11
Requires:       python = %{py_ver}

%description -n python-xcb-proto
Language-independent Python
libraries that used to parse an XML description and create objects
used by Python code generators in individual language bindings.

%prep
%setup -q

%build

%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs



%files
%{_datadir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml

%files -n python-xcb-proto
%python_sitelib/xcbgen/
