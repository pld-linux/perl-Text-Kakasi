#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	A KAKASI library module for Perl
Summary(cs):	Modul s KAKASI knihovnou pro Perl
Summary(da):	Et KAKASI-modul for Perl
Summary(de):	Ein KAKASI-Bibliothek Modul f�r Perl
Summary(es):	M�dulo de la Biblioteca KAKASI para Perl
Summary(fr):	Un module de biblioth�que Kakasi pour Perl
Summary(it):	Modulo di libreria KAKASI per Perl
Summary(ja):	Perl �Ѥ� KAKASI �饤�֥��⥸�塼��
Summary(ko):	���� ���� KAKASI ���̺귯�� ����
Summary(nb):	Et KAKASI-modul for Perl
Summary(pl):	Interfejs Perla do biblioteki KAKASI
Summary(pt):	Um m�dulo da biblioteca KAKASI para o Perl
Summary(ru):	������ ���������� KAKASI ��� Perl
Summary(sv):	En KAKASI-bibliotekmodul f�r Perl
Summary(zh_CN):	Perl �� KAKASI ��ģ�顣
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
Modul Text-Kakasi poskytuje rozhran� ke knihovn� libkakasi do jazyka Perl.
KAKASI je filtr pro konverze japonsk�ch znak� Hiragana, Katakana nebo Romaji.

%description -l da
Modulet Text-Kakasi giver et gr�nseflade for Perl til libkakasi (et
KAKASI-bibliotek).  KAKASI er et sprogbearbejdningsfilter for at
konvertere Kanjitegn til Hiragana, Katakana eller Romaji.

%description -l de
Das Text-Kakasi-Modul unterst�tzt ein libkakasi (eine KAKASI-Bibliothek)
Interface f�r Perl.  KAKASI ist ein Sprachprozessfilter zur Umwandlung der
Kanji-Schriftzeichen in Hirahana, Katakana oder Romaji.

%description -l es
El m�dulo Text-Kakasi proporciona una interfaz de libkakasi (biblioteca
KAKASI) para Perl. KAKASI es un filtro del proceso de lenguaje para
convertir car�cteres Kanji a los Hiragana, Katana o Romaji.

%description -l fr
Le module Text-Kakasi fournit une interface libkakasi (biblioth�que Kakasi)
pour Perl. Kakasi est un filtre de processeur de langage pour convertir les
caract�res Kanji en caract�res Hiragana, Katakana ou Romaji.

%description -l it
Il modulo Text-Kakasi fornisce un'interfacia libkakasi (una libreria
KAKASI) per Perl. KAKASI � un filtro di elaborazione delle lingue per
convertire i caratteri Kanji in Hirigana, Katakana o Romanji.

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

%description -l pt
O m�dulo Text-Kakasi oferece uma interface da libkakasi (uma biblioteca
de KAKASI) para o Perl. O KAKASI � um filtro de processamento para
converter os caracteres Kanji para Hiragana, Katakana ou Romaji.

%description -l ru
������ Text-Kakasi �������� ���������� libkakasi, ������� �������������
��������� KAKASI ��� Perl. ������ KAKASI ������������ ��� ��������������
������ � ��������� Kanji � Hiragana, Katakana ��� Romaji.
%description -l sv
Modulen Text-Kakasi ger ett gr�nssnitt f�r Perl till libkakasi (ett
KAKASI-bibliotek).  KAKASI �r ett spr�kbearbetningsfilter f�r att
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
