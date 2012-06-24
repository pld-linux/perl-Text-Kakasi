%include	/usr/lib/rpm/macros.perl
Summary:	kakasi library module for perl
Summary(pl):	Interfejs perla do biblioteki kakasi
Name:		perl-Text-Kakasi
Version:	1.05
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.daionet.gr.jp/~knok/kakasi/Text-Kakasi-%{version}.tar.gz
URL:		http://www.daionet.gr.jp/~knok/kakasi/
BuildRequires:	kakasi-devel >= 2.3.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI. KAKASI is the language processing filter to convert Kanji
characters to Hiragana, Katakana or Romaji and may be helpful to read
Japanese documents. More information about KAKASI is available at
<http://kakasi.namazu.org/>.

%description -l ja
���Υ⥸�塼��ϡ��ⶶ͵������κ������줿���եȥ�����KAKASI��perl
�����Ѥ��뤿��Τ�ΤǤ���

���Υ⥸�塼���Ȥ�����ˤϡ��ǿ��Ǥ�KAKASI(2.3.0�ʹ�)��ɬ�פǤ���
�ǿ��Ǥ˴ؤ��Ƥϡ�<http://kakasi.namazu.org/>�򻲾Ȥ��Ƥ���������

%description -l pl
Ten modu� dostarcza interfejs libkakasi dla perla. libkakasi to cz��
pakietu KAKASI. KAKASI to filtr konwertuj�cy znaki Kanji na Hiragana,
Katakana lub Romaji, kt�ry mo�e by� przydatny przy czytaniu japo�skich
dokument�w. Wi�cej informacji o KAKASI znajduje si� na stronie
<http://kakasi.namazu.org/>.

%prep
%setup -q -n Text-Kakasi-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%lang(ja) %doc README.jp.gz
%{perl_sitearch}/Text/Kakasi.pm
%dir %{perl_sitearch}/auto/Text/Kakasi
%{perl_sitearch}/auto/Text/Kakasi/Kakasi.bs
%attr(755,root,root) %{perl_sitearch}/auto/Text/Kakasi/Kakasi.so
%{_mandir}/man3/Text::Kakasi.3pm.gz
