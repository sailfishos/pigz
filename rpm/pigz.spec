Name:          pigz
Summary:       Parallel implementation of gzip
Version:       2.3.3
Release:       1
Group:         Applications/File
License:       zlib
URL:           http://zlib.net/pigz/
Source0:       %{name}-%{version}.tar.gz
Patch0:        001-Makefile-Fix-undefined-reference-to-adler32.patch

BuildRequires: zlib-devel >= 1.2.6

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
pushd %{name}
make %{?jobs:-j%jobs}
popd

%install
rm -rf %{buildroot}

install -D -m 0755 %{name}/pigz %{buildroot}/%{_bindir}/pigz
install -D -m 0755 %{name}/unpigz %{buildroot}/%{_bindir}/unpigz

%files
%defattr(-,root,root,-)
%{_bindir}/pigz
%{_bindir}/unpigz

