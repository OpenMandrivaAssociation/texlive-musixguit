%global tl_name musixguit
%global tl_revision 21649

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.2
Release:	%{tl_revision}.1
Summary:	Easy notation for guitar music, in MusixTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/musixguit
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixguit.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands for typesetting notes for guitar,
especially for simplifying guitar notation with MusixTeX.

