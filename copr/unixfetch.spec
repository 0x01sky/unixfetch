Name:           unixfetch
Version:        1.1.0
Release:        1%{?dist}
Summary:        Simple system info fetch tool
License:        MIT
BuildArch:      noarch

%description
unixfetch is a lightweight system information tool for Unix-like systems.

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 unixfetch %{buildroot}%{_bindir}/unixfetch

%files
%{_bindir}/unixfetch

%changelog
* Tue Apr 21 2026 <0x01sky@git.me> - 0.1-1
- Initial COPR package
