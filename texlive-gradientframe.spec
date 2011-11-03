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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a means of drawing graded frames around
objects. The gradients of the frames are drawn using the color
package.

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
%{_texmfdistdir}/tex/latex/gradientframe/gradientframe.sty
%doc %{_texmfdistdir}/doc/latex/gradientframe/README
%doc %{_texmfdistdir}/doc/latex/gradientframe/gradientframe.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gradientframe/gradientframe.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
