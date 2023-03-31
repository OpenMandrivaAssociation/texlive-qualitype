Name:		texlive-qualitype
Version:	54512
Release:	2
Summary:	The QualiType font collection
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qualitype
License:	ofl gpl2+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qualitype.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qualitype.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These 45 fonts were created by QualiType. With the kind
permisison of John Colletti, these fonts have been released as
free and open-source.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/qualitype
%doc %{_texmfdistdir}/doc/fonts/qualitype

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
