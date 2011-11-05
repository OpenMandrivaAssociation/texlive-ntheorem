# revision 21607
# category Package
# catalog-ctan /macros/latex/contrib/ntheorem
# catalog-date 2011-02-18 13:25:28 +0100
# catalog-license lppl
# catalog-version 1.31
Name:		texlive-ntheorem
Version:	1.31
Release:	1
Summary:	Enhanced theorem environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ntheorem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Enhancements for theorem-like environments: easier control of
layout; proper placement of endmarks even when the environment
ends with \end{enumerate} or \end{displaymath} (including
support for amsmath displayed-equation environments); and
support for making a list of theorems like \listoffigures.

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
%{_texmfdistdir}/tex/latex/ntheorem/ntheorem.std
%{_texmfdistdir}/tex/latex/ntheorem/ntheorem.sty
%doc %{_texmfdistdir}/doc/latex/ntheorem/README
%doc %{_texmfdistdir}/doc/latex/ntheorem/ntheorem.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ntheorem/ntheorem.drv
%doc %{_texmfdistdir}/source/latex/ntheorem/ntheorem.dtx
%doc %{_texmfdistdir}/source/latex/ntheorem/ntheorem.ins
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
