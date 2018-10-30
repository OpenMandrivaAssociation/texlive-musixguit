# revision 21649
# category Package
# catalog-ctan /macros/latex/contrib/musixguit
# catalog-date 2011-03-07 21:34:56 +0100
# catalog-license lppl1.3
# catalog-version 1.2.2
Name:		texlive-musixguit
Version:	1.2.2
Release:	11
Summary:	Easy notation for guitar music, in MusixTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/musixguit
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2.2-2
+ Revision: 754235
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2.2-1
+ Revision: 719089
- texlive-musixguit
- texlive-musixguit
- texlive-musixguit
- texlive-musixguit

