Name:          pigz
Summary:       Parallel implementation of gzip
Version:       2.3.3
Release:       1
License:       zlib
URL:           https://github.com/sailfishos/pigz
Source0:       %{name}-%{version}.tar.gz
Patch0:        001-Makefile-Fix-undefined-reference-to-adler32.patch

BuildRequires: zlib-devel >= 1.2.6

%description
%{summary}

%prep
%autosetup -p1 -n %{name}-%{version}

%build
pushd %{name}
%make_build
popd

%install
install -D -m 0755 %{name}/pigz %{buildroot}/%{_bindir}/pigz
install -D -m 0755 %{name}/unpigz %{buildroot}/%{_bindir}/unpigz

%files
%{_bindir}/pigz
%{_bindir}/unpigz

