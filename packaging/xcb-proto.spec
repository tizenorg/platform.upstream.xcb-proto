Name:         	xcb-proto
Version:        1.10
Release:        1
License:        MIT
Summary:        X C Binding - protocol descriptions
Url:            http://www.x.org
Group:          Development/X11 Protocols
Source0:        %{name}-%{version}.tar.bz2
Source1001: 	xcb-proto.manifest

BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(xorg-macros)
Requires:	python-xcb-proto

%description
The xcb-proto package provides the XML-XCB protocol 
descriptions that libxcb uses to generate the majority of 
its code and API.

%package -n python-xcb-proto
Summary:        Python libraries mandatory for XML-XCB Development
Group:          Development/X11 Protocols
Requires:       python = %{py_ver}

%description -n python-xcb-proto
Language-independent Python
libraries that used to parse an XML description and create objects
used by Python code generators in individual language bindings.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs



%files
%manifest %{name}.manifest
%license COPYING
%{_datadir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml

%files -n python-xcb-proto
%manifest %{name}.manifest
%python_sitelib/xcbgen/
