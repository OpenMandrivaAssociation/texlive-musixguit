Name:		texlive-musixguit
Version:	21649
Release:	1
Summary:	Easy notation for guitar music, in MusixTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musixguit
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for typesetting notes for guitar,
especially for simplifying guitar notation with MusixTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/musixguit/musixguit.sty
%doc %{_texmfdistdir}/doc/latex/musixguit/README
%doc %{_texmfdistdir}/doc/latex/musixguit/musixguit_de.pdf
%doc %{_texmfdistdir}/doc/latex/musixguit/musixguit_de.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
