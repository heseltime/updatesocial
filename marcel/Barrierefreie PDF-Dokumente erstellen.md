# Barrierefreie PDF-Dokumente erstellen

# 0. Einleitung

> Auch das Umwandeln bereits existierender PDFs in barrierefreie PDF-Dokumente wird hier nur am Rande behandelt. Dieses Vorgehen ist in der Regel zu aufwendig, daher nicht zukunftstauglich und aufgrund der Anforderungen etwas für Spezialisten. Sie erlangen zwar das notwendige Grundlagenwissen für diesen Arbeitsprozess, wir liefern aber keine Anleitung zur Umsetzung mit Acrobat oder anderen Programmen. Hierfür stehen entsprechende Handbücher zu den am Markt verfügbaren Programmen zur Verfügung. (S. 22)
> 
- **Theoretischer Teil:** Kapitel 1-6
- **Praktischer Teil:** Kapitel 7-14
- **Website zum Buch:** [https://barrierefrei-publizieren.de](https://barrierefrei-publizieren.de/)

# 1. Einstieg Theorie

# 2. Barrierefreiheit Grundlagen

- Wahrscheinlich **wichtigstes** Kapitel.

> In einer vollständig inklusiven Gesellschaft sind barrierefreie Dokumente und Inhalte keine Besonderheit, sondern der Normalzustand. (S.34)
> 
- Der Begriff “Accessibility” (Zugänglichkeit) ist besser als “Barrierefreiheit”, letzterer ist aber am geläufigsten verbreitet. (S. 34f)

> Gute, barrierefreie Dokumente bieten einen erheblichen **Mehrwert für alle Nutzer*innen**. (S. 35)
> 

> Die Verbindung von Usability und Accessibility hat sich in der Webentwicklung schon vor vielen Jahren durchgesetzt. Der Grund hierfür war maßgeblich die Verbreitung von  martphones und Tablets, auf denen statische Webseiten ungenügend nutzbar waren. Sich an das genutzte Display dynamisch anpassende Inhalte in Form von responsiven Webseiten waren die Folge. Diese Technologie bot gleichzeitig eine sehr gute Grundlage barrierefreie Zugänge zu schaffen, quasi als Nebenprodukt. (S. 37)
> 

> **Ausblick in die Zukunft**
Die neue Spezifikation des PDF-Formates (2.0) bietet die Möglichkeit, andere Technologien zu nutzen, beispielsweise HTML und CSS. Unter der Begriffen Next-Generation PDF / PDFng / rPDF findet derzeit eine Weiterentwicklung des Formates statt, das künftig innerhalb einer PDF-Date verschiedene Darstellungsformen des Inhaltes ermöglichen soll. Dami wäre es möglich, in einer PDF-Datei verschiedene Ansichten, optimiert für verschiedene Geräte oder Nutzungsformen, zu implementieren. Basis für diese Technologie sind letztendlich barrierefreie PDF-Dokumente. (S. 39)
> 

> Die meisten Menschen, die ich bisdato getroffen habe, gehen davon aus, dass die Erstellung von barrierefreien Dokumenten mehr Geld kostet. Laut meiner langjährigen Erfahrung ist aber das Gegenteil der Fall. (S. 42)
> 
- **Anwendungsfall: Kopieren aus einem PDF (S. 43).**
    - Aus jeder einzelnen Zeile wird ein eigener Absatz.
    - Trennstriche werden eingefügt, wo ein Zeilenumbruch im Wort war.
    - Je nach Schriftart können Umlaute oder Ligaturen verschwinden.
- Wirtschaftlich wichtigster Grund für barrierefreie PDFs: **Besserer Zugang für Suchmaschinen!**
    
    > Normale PDFs sind für Google & Co. meist ein Buch mit sieben Siegeln. Barrierefreie PDF-Dokumente hingegen sind ein sehr gutes Mittel, Inhalte gezielt auffindbar zu machen. (S. 44)
    > 
- Wirtschaftliche Nachteile nicht barrierefreier PDFs: (S. 44)
    - Britische Unternehmen verlieren monatlich 1,8 Mrd. Pfund aufgrund unzugänglicher Inhalte.
    - Buchhaltungen investieren viele Ressourcen in das Erfassen und Extrahieren von Inhalten.
    - Nichteinhaltungen gesetzlicher Vorgaben können zu Strafen führen.
- Barrierefrei sein ist wie mit dem Schwangersein - ganz oder gar nicht. (S. 45)

> Markus Erle, in Fachkreisen anerkannter Experte für barrierefreie PDFs, hat eine schöne Analogie dafür geschaffen, was das Fehlen bestimmter Kriterien für barrierefreie Inhalte bedeutet: Angenommen, Sie wollen über eine Hängebrücke gehen, die einen tiefen Abgrund überquert, und unten befindet sich ein Fluss, in dem Krokodile schwimmen. Ist die Brücke intakt, sollte eine Überquerung problemlos möglich sein - in Übertragung der problemfreie, uneingeschränkte Zugang zu einem Dokument. Fehlt sichtbar eine Latte (ein Kriterium für ein barrierefreies Dokument ist nicht erfüllt), sind Sie vielleicht leicht skeptisch, aber eine Überquerung wird mit leicht flauem Magen dennoch möglich sein - wenn Sie aber Pech haben, erwischen Sie die Lücke. Noch kritischer wird es, wenn mehrere Latten fehlen. Verteilen sich diese Lücken gleichmäßig, so mag auch das noch gut gehen auch wenn die Chancen für einen Absturz rapide steigen. Fehlen mehrere Latten am Stück, kann eine Überquerung unmöglich sein - das Dokument ist nicht zugänglich, obwohl vielleicht viele Kriterien für ein barrierefreies Dokument erfüllt sind. Da hilft es auch nicht, wenn die vorhandenen Latten auch Hochglanz poliert sind, also einzelne Kriterien mit Bravour erfüllt oder gar übererfüllt sind. (S. 45)
> 
- PDFs gleichzeitig größte Stärke und Schwäche (was Barrierefreiheit angeht) ist die zuverlässige pixelgenaue Anzeige von Inhalten. Dynamische Alternativen: HTML, Word-Dateien. (S. 46)
- **Tagged PDF**: (S. 47ff)
    - Seit PDF Version 1.4.
    - Ursprünglich um PDFs in HTML oder XML zu konvertieren.
    - Stellt Basis für barrierefreie PDFs dar.
    - **PDF vermittelt nur die Erscheinung, nicht die Bedeutung** (Lehre der Bedeutung = **Semantik**).
    - Tags verleihen Inhalt Bedeutung (z.B.: Textstelle ist eine Überschrift oder eindeutige Lesereihenfolge)
    - PDF-Tags haben zwei Grundfunktionen:
        - Semantische Auszeichnung der Inhalte.
        - Definition der Lesereihenfolge.
    - Beispiele für Tags:
        - Hauptüberschrift: \<H1>
        - Absatz: \<P>
        - Bild: \<Figure>
    - Ein barrierefreies PDF ist immer ein Tagged PDF, aber ein Tagged PDF muss nicht immer barrierefrei sein!
    - Das PDF enthält die Reihenfolge seiner Inhalte in seinem Quellcode, auch **Content Stream** genannt.
- Adobe Acrobat hat ein Navigationsfenster namens “Reihenfolge”. Dieses bildet aber nicht die für Barrierefreiheit relevante Reihenfolge ab. Stattdessen kann man das Navigationsfenster “Tags” benutzen. (S. 53)
- Viele Tagged PDFs sind nicht barrierefrei. In diesen sind oft alle Inhalte als nomale Absätze <P> gekennzeichnet. Das kann man sich so vorstellen, als würde man den kompletten Text einer Zeitung als Fließtext in einer .txt-Datei lesen. (S. 53)

> Daraus lässt sich aber auch eine wichtige Erkenntnis ableiten: Barrierefreie Dokumente bedürfen der Mitarbeit der Inhaltsersteller*innen und **können nicht immer automatisch auf Knopfdruck generiert werden**. (S. 53)
> 
- **PDF/UA** (Universal Accessiblity) ist die Bezeichnung für Tagged PDFs, die richtig getagged sind (=barrierefrei). Sie lehnt sich an **WCAG** (Web Content Accessibility Guidelines). Unser Ziel ist es PDFs nach der PDF/UA Norm zu erstellen. (S. 53)
- Warum PDF? (S. 55ff)
    - Großteil der PDFs werden am Monitor konsumiert, dieser ist im Querformat, macht PDF also überhaupt noch Sinn?
    - PDFs benötigen ein ZUsatzprogramm (Viewer) zum Betrachten.
    - Alternativen: HTML (+ CSS), EPUB, Word, Writer, Rich Text Format, Bildformate, Audioformate
    - Aber: **PDF already too big to fail?**
    - 

# 3. Wege zum barrierefreien PDF

# 4. Nutzung barrierefreie PDFs

# 5. Richtlinien, Normen, Gesetze

# 6. Anforderungen im Detail

# 7. Einstieg Praxis

# 8. Leitlinien für Design und Redaktion

# 9. InDesign

# 10. Word

# 11. Excel, PowerPoint

# 12. LibreOffice

# 13. Prüfung

# 14. Nachbearbeitung