%global tl_name gradientframe
%global tl_revision 21387

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Simple gradient frames around objects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gradientframe
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gradientframe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gradientframe.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gradientframe.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a means of drawing graded frames around objects.
The gradients of the frames are drawn using the color package.

