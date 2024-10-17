Name:		texlive-ntheorem
Version:	27609
Release:	2
Summary:	Enhanced theorem environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ntheorem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Enhancements for theorem-like environments: easier control of
layout; proper placement of endmarks even when the environment
ends with \end{enumerate} or \end{displaymath} (including
support for amsmath displayed-equation environments); and
support for making a list of theorems like \listoffigures.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
