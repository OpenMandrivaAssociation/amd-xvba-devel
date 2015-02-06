Name:		amd-xvba-devel
Summary:	X-Video Bitstream Acceleration SDK by AMD
Version:	0.74
Release:	1.404002
Group:		Development/C
Source0:	http://developer.amd.com/Downloads/xvba-sdk-0.74-404001.tar.gz
URL:		http://developer.amd.com
License:	BSD
BuildArch:	noarch
Requires:	fglrx-devel

%description
This package contains the AMD Embedded Solutions X-Video Bitstream
Acceleration software development kit for Linux.

This software is being released with no warranty or support for the
general public. AMD Embedded Solutions customers may contact their
support representative for technical inquiries. Please reference the
accompanying LICENSE for terms and conditions.

Limited testing has been conducted on RS780, E4690, HD5770, and G-Series.

%prep
%setup -c -q

%build

%install
install -m 644 -D include/amdxvba.h %{buildroot}%{_includedir}/amdxvba.h

%files
%{_includedir}/amdxvba.h
%doc LICENSE README doc/*.pdf


%changelog
* Mon Nov 21 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.74-1.404001
+ Revision: 732155
- imported package amd-xvba-devel

