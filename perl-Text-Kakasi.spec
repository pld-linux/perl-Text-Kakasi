#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Kakasi
Summary:	A KAKASI library module for Perl
Summary(cs.UTF-8):	Modul s KAKASI knihovnou pro Perl
Summary(da.UTF-8):	Et KAKASI-modul for Perl
Summary(de.UTF-8):	Ein KAKASI-Bibliothek Modul für Perl
Summary(es.UTF-8):	Módulo de la Biblioteca KAKASI para Perl
Summary(fr.UTF-8):	Un module de bibliothèque Kakasi pour Perl
Summary(it.UTF-8):	Modulo di libreria KAKASI per Perl
Summary(ja.UTF-8):	Perl 用の KAKASI ライブラリモジュール
Summary(ko.UTF-8):	펄을 위한 KAKASI 라이브러리 모줄
Summary(nb.UTF-8):	Et KAKASI-modul for Perl
Summary(pl.UTF-8):	Interfejs Perla do biblioteki KAKASI
Summary(pt.UTF-8):	Um módulo da biblioteca KAKASI para o Perl
Summary(ru.UTF-8):	Модуль библиотеки KAKASI для Perl
Summary(sv.UTF-8):	En KAKASI-bibliotekmodul för Perl
Summary(zh_CN.UTF-8):	Perl 的 KAKASI 库模块。
Name:		perl-Text-Kakasi
Version:	2.04
Release:	1
# README says just GPL, but module itself GPL v2+
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a9e381cb93edfd707124a63c60f96b1
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

%description -l cs.UTF-8
Modul Text-Kakasi poskytuje rozhraní ke knihovně libkakasi do jazyka Perl.
KAKASI je filtr pro konverze japonských znaků Hiragana, Katakana nebo Romaji.

%description -l da.UTF-8
Modulet Text-Kakasi giver et grænseflade for Perl til libkakasi (et
KAKASI-bibliotek).  KAKASI er et sprogbearbejdningsfilter for at
konvertere Kanjitegn til Hiragana, Katakana eller Romaji.

%description -l de.UTF-8
Das Text-Kakasi-Modul unterstützt ein libkakasi (eine KAKASI-Bibliothek)
Interface für Perl.  KAKASI ist ein Sprachprozessfilter zur Umwandlung der
Kanji-Schriftzeichen in Hirahana, Katakana oder Romaji.

%description -l es.UTF-8
El módulo Text-Kakasi proporciona una interfaz de libkakasi (biblioteca
KAKASI) para Perl. KAKASI es un filtro del proceso de lenguaje para
convertir carácteres Kanji a los Hiragana, Katana o Romaji.

%description -l fr.UTF-8
Le module Text-Kakasi fournit une interface libkakasi (bibliothèque Kakasi)
pour Perl. Kakasi est un filtre de processeur de langage pour convertir les
caractères Kanji en caractères Hiragana, Katakana ou Romaji.

%description -l it.UTF-8
Il modulo Text-Kakasi fornisce un'interfacia libkakasi (una libreria
KAKASI) per Perl. KAKASI è un filtro di elaborazione delle lingue per
convertire i caratteri Kanji in Hirigana, Katakana o Romanji.

%description -l ja.UTF-8
このモジュールは、高橋裕信さんの作成されたソフトウェアKAKASIをperl
から用いるためのものです。

このモジュールを使うためには、最新版のKAKASI(2.3.0以降)が必要です。
最新版に関しては、<http://kakasi.namazu.org/>を参照してください。

%description -l pl.UTF-8
Ten moduł dostarcza interfejs libkakasi dla Perla. libkakasi to część
pakietu KAKASI. KAKASI to filtr konwertujący znaki Kanji na Hiragana,
Katakana lub Romaji, który może być przydatny przy czytaniu japońskich
dokumentów. Więcej informacji o KAKASI znajduje się na stronie
<http://kakasi.namazu.org/>.

%description -l pt.UTF-8
O módulo Text-Kakasi oferece uma interface da libkakasi (uma biblioteca
de KAKASI) para o Perl. O KAKASI é um filtro de processamento para
converter os caracteres Kanji para Hiragana, Katakana ou Romaji.

%description -l ru.UTF-8
Модуль Text-Kakasi содержит библиотеку libkakasi, которая предоставляет
интерфейс KAKASI для Perl. Фильтр KAKASI предназначен для преобразования
текста и кодировки Kanji в Hiragana, Katakana или Romaji.
%description -l sv.UTF-8
Modulen Text-Kakasi ger ett gränssnitt för Perl till libkakasi (ett
KAKASI-bibliotek).  KAKASI är ett språkbearbetningsfilter för att
konvertera Kanjitecken till Hiragana, Katakana eller Romaji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc README
%lang(ja) %doc README.jp
%{perl_vendorarch}/Text/*.pm
%dir %{perl_vendorarch}/auto/Text/Kakasi
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Kakasi/*.so
%{_mandir}/man3/*
