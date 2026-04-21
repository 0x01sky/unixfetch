Name:           unixfetch
Version:        1.1.0
Release:        1%{?dist}
Summary:        A simple system info fetch tool

License:        MIT
URL:            https://github.com/0x01sky/unixfetch
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

%description
A lightweight system information tool for Unix-like systems.

%prep
%autosetup

%build


%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 unixfetch %{buildroot}/usr/bin/unixfetch

%files
/usr/bin/unixfetch

%changelog
* Tue Apr 21 2026 Sky <0x01sky@git.me> - 0.1-1
- Initial package
