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
¤³¤Î¥â¥¸¥å¡¼¥ë¤Ï¡¢¹â¶¶Íµ¿®¤µ¤ó¤ÎºîÀ®¤µ¤ì¤¿¥½¥Õ¥È¥¦¥§¥¢KAKASI¤òperl
¤«¤éÍÑ¤¤¤ë¤¿¤á¤Î¤â¤Î¤Ç¤¹¡£

¤³¤Î¥â¥¸¥å¡¼¥ë¤ò»È¤¦¤¿¤á¤Ë¤Ï¡¢ºÇ¿·ÈÇ¤ÎKAKASI(2.3.0°Ê¹ß)¤¬É¬Í×¤Ç¤¹¡£
ºÇ¿·ÈÇ¤Ë´Ø¤·¤Æ¤Ï¡¢<http://kakasi.namazu.org/>¤ò»²¾È¤·¤Æ¤¯¤À¤µ¤¤¡£

%description -l pl
Ten modu³ dostarcza interfejs libkakasi dla perla. libkakasi to czê¶æ
pakietu KAKASI. KAKASI to filtr konwertuj±cy znaki Kanji na Hiragana,
Katakana lub Romaji, który mo¿e byæ przydatny przy czytaniu japoñskich
dokumentów. Wiêcej informacji o KAKASI znajduje siê na stronie
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
