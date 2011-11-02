Name:		texlive-musixguit
Version:	1.2.2
Release:	1
Summary:	Easy notation for guitar music, in MusixTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musixguit
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides commands for typesetting notes for guitar,
especially for simplifying guitar notation with MusixTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/musixguit/musixguit.sty
%doc %{_texmfdistdir}/doc/latex/musixguit/README
%doc %{_texmfdistdir}/doc/latex/musixguit/musixguit_de.pdf
%doc %{_texmfdistdir}/doc/latex/musixguit/musixguit_de.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
