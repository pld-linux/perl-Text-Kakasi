#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	A KAKASI library module for Perl
Summary(cs):	Modul s KAKASI knihovnou pro Perl
Summary(da):	Et KAKASI-modul for Perl
Summary(de):	Ein KAKASI-Bibliothek Modul für Perl
Summary(es):	Módulo de la Biblioteca KAKASI para Perl
Summary(fr):	Un module de bibliothèque Kakasi pour Perl
Summary(it):	Modulo di libreria KAKASI per Perl
Summary(ja):	Perl ÍÑ¤Î KAKASI ¥é¥¤¥Ö¥é¥ê¥â¥¸¥å¡¼¥ë
Summary(ko):	ÆŞÀ» À§ÇÑ KAKASI ¶óÀÌºê·¯¸® ¸ğÁÙ
Summary(nb):	Et KAKASI-modul for Perl
Summary(pl):	Interfejs Perla do biblioteki KAKASI
Summary(pt):	Um módulo da biblioteca KAKASI para o Perl
Summary(ru):	íÏÄÕÌØ ÂÉÂÌÉÏÔÅËÉ KAKASI ÄÌÑ Perl
Summary(sv):	En KAKASI-bibliotekmodul för Perl
Summary(zh_CN):	Perl µÄ KAKASI ¿âÄ£¿é¡£
Name:		perl-Text-Kakasi
Version:	1.05
Release:	4
# README says just GPL, but module itself GPL v2+
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.daionet.gr.jp/~knok/kakasi/Text-Kakasi-%{version}.tar.gz
# Source0-md5:	6c50ca6dce1fcc2f01446f6e305571a5
URL:		http://www.daionet.gr.jp/~knok/kakasi/
BuildRequires:	kakasi-devel >= 2.3.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	kakasi-dict
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI. KAKASI is the language processing filter to convert Kanji
characters to Hiragana, Katakana or Romaji and may be helpful to read
Japanese documents. More information about KAKASI is available at
<http://kakasi.namazu.org/>.

%description -l cs
Modul Text-Kakasi poskytuje rozhraní ke knihovnì libkakasi do jazyka Perl.
KAKASI je filtr pro konverze japonskıch znakù Hiragana, Katakana nebo Romaji.

%description -l da
Modulet Text-Kakasi giver et grænseflade for Perl til libkakasi (et
KAKASI-bibliotek).  KAKASI er et sprogbearbejdningsfilter for at
konvertere Kanjitegn til Hiragana, Katakana eller Romaji.

%description -l de
Das Text-Kakasi-Modul unterstützt ein libkakasi (eine KAKASI-Bibliothek)
Interface für Perl.  KAKASI ist ein Sprachprozessfilter zur Umwandlung der
Kanji-Schriftzeichen in Hirahana, Katakana oder Romaji.

%description -l es
El módulo Text-Kakasi proporciona una interfaz de libkakasi (biblioteca
KAKASI) para Perl. KAKASI es un filtro del proceso de lenguaje para
convertir carácteres Kanji a los Hiragana, Katana o Romaji.

%description -l fr
Le module Text-Kakasi fournit une interface libkakasi (bibliothèque Kakasi)
pour Perl. Kakasi est un filtre de processeur de langage pour convertir les
caractères Kanji en caractères Hiragana, Katakana ou Romaji.

%description -l it
Il modulo Text-Kakasi fornisce un'interfacia libkakasi (una libreria
KAKASI) per Perl. KAKASI è un filtro di elaborazione delle lingue per
convertire i caratteri Kanji in Hirigana, Katakana o Romanji.

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

%description -l pt
O módulo Text-Kakasi oferece uma interface da libkakasi (uma biblioteca
de KAKASI) para o Perl. O KAKASI é um filtro de processamento para
converter os caracteres Kanji para Hiragana, Katakana ou Romaji.

%description -l ru
íÏÄÕÌØ Text-Kakasi ÓÏÄÅÒÖÉÔ ÂÉÂÌÉÏÔÅËÕ libkakasi, ËÏÔÏÒÁÑ ĞÒÅÄÏÓÔÁ×ÌÑÅÔ
ÉÎÔÅÒÆÅÊÓ KAKASI ÄÌÑ Perl. æÉÌØÔÒ KAKASI ĞÒÅÄÎÁÚÎÁŞÅÎ ÄÌÑ ĞÒÅÏÂÒÁÚÏ×ÁÎÉÑ
ÔÅËÓÔÁ É ËÏÄÉÒÏ×ËÉ Kanji × Hiragana, Katakana ÉÌÉ Romaji.
%description -l sv
Modulen Text-Kakasi ger ett gränssnitt för Perl till libkakasi (ett
KAKASI-bibliotek).  KAKASI är ett språkbearbetningsfilter för att
konvertera Kanjitecken till Hiragana, Katakana eller Romaji.

%prep
%setup -q -n Text-Kakasi-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%lang(ja) %doc README.jp*
%{perl_vendorarch}/Text/Kakasi.pm
%dir %{perl_vendorarch}/auto/Text/Kakasi
%{perl_vendorarch}/auto/Text/Kakasi/Kakasi.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Kakasi/Kakasi.so
%{_mandir}/man3/Text::Kakasi.3pm*
