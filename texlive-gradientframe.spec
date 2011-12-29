# revision 21387
# category Package
# catalog-ctan /macros/latex/contrib/gradientframe
# catalog-date 2011-02-13 15:43:06 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-gradientframe
Version:	0.2
Release:	1
Summary:	Simple gradient frames around objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gradientframe
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gradientframe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gradientframe.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gradientframe.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of drawing graded frames around
objects. The gradients of the frames are drawn using the color
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gradientframe/gradientframe.sty
%doc %{_texmfdistdir}/doc/latex/gradientframe/README
%doc %{_texmfdistdir}/doc/latex/gradientframe/gradientframe.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gradientframe/gradientframe.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
