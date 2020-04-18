import unittest
from lib.find_info import parse_pdf_links_from_html, find_in_pdf


class TestFind(unittest.TestCase):
    def test_find_pdf_links(self):
        links_list = parse_pdf_links_from_html(find_pdf_test_html)

        agendbundel = False
        energie_en_democratie = False
        for link in links_list:
            if link["name"] == "Agendabundel" and link[
                "url"] == "https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&id=ffbcd3ff-ea2c-43b6-87d7-a50fd0df7ef5":
                agendbundel = True
            if link["name"] == "Energie en democratie - essay Marcel Boogers oktober 2019.pdf" and link[
                "url"] == "https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&id=fadd97d3-5e67-4099-a943-3964f1231005":
                energie_en_democratie = True
        self.assertTrue(agendbundel)
        self.assertTrue(energie_en_democratie)


    def test_find_in_pdf(self):
        result = find_in_pdf("../test/test_agenda.pdf", ["Opening"])
        self.assertIn("Opening", result)
        self.assertIn(0, result["Opening"])

    def test_find_in_pdf_multiple(self):
        result = find_in_pdf("../test/test_agenda.pdf", ["Opening", "Burgemeester"])
        self.assertIn("Opening", result)
        self.assertIn("Burgemeester", result)
        self.assertIn(0, result["Opening"])
        self.assertIn(1, result["Burgemeester"])
        self.assertIn(2, result["Burgemeester"])





find_pdf_test_html = """

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iBabs Online</title>


    <!-- Fonts.. -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800" rel="stylesheet">
    <link href="/Content/libs?v=tjhK1elZkS6ORfgAa7f7_e47gVatRwBb3buCSykOzSQ1" rel="stylesheet"/>

    <link href="/Content/css?v=NZxkNInUyjJVVO-bsOmsCcor5rtKFn4p667JqCDOfrw1" rel="stylesheet"/>


    

        <link href="/Content/Sites/utrecht.css" rel="stylesheet" type="text/css" />

    <script src="/Scripts/modernizr-2.8.3.js"></script>
        <script type="text/javascript">
            var appInsights = window.appInsights || function (config) {
                function i(config) { t[config] = function () { var i = arguments; t.queue.push(function () { t[config].apply(t, i) }) } } var t = { config: config }, u = document, e = window, o = "script", s = "AuthenticatedUserContext", h = "start", c = "stop", l = "Track", a = l + "Event", v = l + "Page", y = u.createElement(o), r, f; y.src = config.url || "https://az416426.vo.msecnd.net/scripts/a/ai.0.js"; u.getElementsByTagName(o)[0].parentNode.appendChild(y); try { t.cookie = u.cookie } catch (p) { } for (t.queue = [], t.version = "1.0", r = ["Event", "Exception", "Metric", "PageView", "Trace", "Dependency"]; r.length;) i("track" + r.pop()); return i("set" + s), i("clear" + s), i(h + a), i(c + a), i(h + v), i(c + v), i("flush"), config.disableExceptionTracking || (r = "onerror", i("_" + r), f = e[r], e[r] = function (config, i, u, e, o) { var s = f && f(config, i, u, e, o); return s !== !0 && t["_" + r](config, i, u, e, o), s }), t
            }({
                instrumentationKey: "401c8ccf-8e13-4157-8f7a-f0af8ea51a97"
            });

            window.appInsights = appInsights;

            // Add telemetry initializer
            appInsights.queue.push(function () {

                appInsights.context.addTelemetryInitializer(function (envelope) {

                    /* filter our Ajax requests with signalr in url*/

                    if (envelope.name === Microsoft.ApplicationInsights.Telemetry.RemoteDependencyData.envelopeType && envelope.data.baseData.name.indexOf("/signalr/") > -1) {

                        return false;

                    }
                });
            });

            // end of insertion

            appInsights.trackPageView();
        </script>
</head>
<body>
    <div id="wrapper">
        <header id="header">
            <div class="container">
                <div class="row">
                    <div class="col-xs-4">
                            <div id="logo"></div>
                    </div>
                    <div class="col-xs-8">

                    </div>
                </div>
            </div>
        </header>
        <nav id="navigation" class="navbar navbar-default navbar-static-top">
            <div class="container">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a aria-label="Zoeken" href="/Utrecht" class="searchButton">
                    <i class="fa fa-search" aria-hidden="true" title="Zoeken"></i>
                </a>
                <div id="navbar" class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li id="nav-item-dashboard"><a href="/Utrecht">Dashboard</a></li>
                        <li id="nav-item-calendar"><a href="/Calendar/Index/Utrecht">Kalender</a></li>
                            <li id="nav-item-report"><a href="/Reports/Index/Utrecht">Overzichten</a></li>
                                                    <li id="nav-item-people"><a href="/People/Index/Utrecht">Wie is wie</a></li>
                                                                            <li id="nav-item-help"><a href="/Help/Index/Utrecht">Vraagbaak</a></li>
                                                    <li id="nav-item-contact"><a href="/Contact/Index/Utrecht">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <div id="content">
            <div class="container">
                <div class="container-inner">
                    <div id="breadcrumb">
                        <ul>
                            
                            
    <li>
        <a href="/Calendar/Index/Utrecht">Kalender</a>
    </li>
    <li>
        <span>Commissie Mens en Samenleving</span>
    </li>

                        </ul>
                    </div>
                    <div id="changeFonts">
                        <ul>
                            <li>
                                <a href="#"
                                   data-size="14">A</a>
                            </li>
                            <li>
                                <a href="#"
                                   data-size="16">A</a>
                            </li>
                            <li>
                                <a href="#"
                                   data-size="18">A</a>
                            </li>
                        </ul>
                    </div>
                    <div class="clearfix"></div>
                    


<div class="row">
    <aside class="col-sm-4 col-md-3">
        <a class="backButton margin-top margin-bottom"
           href="/Calendar/Index/Utrecht">
            Terug naar kalender
        </a>
        <div class="widget">
            <h4>Agenda&#39;s</h4>
            <ul class="list-group" id="AgendaYearList">
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2020"
                               aria-expanded="false"
                               aria-controls="year2020">
                                <span style="font-size: 1.1em;">2020</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-up"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse in"
                             id="year2020">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2020"
                                style="margin-left: 15px;">
                                    <li class="agenda-link list-group-item">
            <strong>
                donderdag 23 april
            </strong>
            <br/>
            <span class="agenda-link-subtitle"></span>
    </li>
    <li class="agenda-link list-group-item">
            <a href="/Agenda/Details/Utrecht/f46d8b14-f1a6-40dc-8622-91b548758893">
                <span class="agenda-link-title">donderdag 2 april</span>
            </a>
    </li>
    <li class="agenda-link list-group-item">
            <a href="/Agenda/Details/Utrecht/51c43fb8-761c-4953-bea9-2edf1a7e1ae2">
                <span class="agenda-link-title">donderdag 26 maart</span>
            </a>
    </li>
    <li class="agenda-link list-group-item">
            <a href="/Agenda/Details/Utrecht/83f4ae2d-2664-40cd-a234-99810820d01b">
                <span class="agenda-link-title">donderdag 19 maart</span>
            </a>
    </li>
    <li class="agenda-link list-group-item">
            <a href="/Agenda/Details/Utrecht/894e8314-acf8-455e-9a06-8e83db927783">
                <span class="agenda-link-title">donderdag 13 februari</span>
            </a>
    </li>
    <li class="agenda-link list-group-item">
            <a href="/Agenda/Details/Utrecht/b9ec7323-2e45-4227-a380-0e2006bc18e9">
                <span class="agenda-link-title">donderdag 16 januari</span>
            </a>
    </li>
    <li class="agenda-link list-group-item">
            <a href="/Agenda/Details/Utrecht/20273d72-9b59-426a-946c-efce7e871dca">
                <span class="agenda-link-title">donderdag 16 januari</span>
            </a>
    </li>

                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2019"
                               aria-expanded="false"
                               aria-controls="year2019">
                                <span style="font-size: 1.1em;">2019</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2019">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2019"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2018"
                               aria-expanded="false"
                               aria-controls="year2018">
                                <span style="font-size: 1.1em;">2018</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2018">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2018"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2017"
                               aria-expanded="false"
                               aria-controls="year2017">
                                <span style="font-size: 1.1em;">2017</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2017">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2017"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2016"
                               aria-expanded="false"
                               aria-controls="year2016">
                                <span style="font-size: 1.1em;">2016</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2016">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2016"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2015"
                               aria-expanded="false"
                               aria-controls="year2015">
                                <span style="font-size: 1.1em;">2015</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2015">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2015"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2014"
                               aria-expanded="false"
                               aria-controls="year2014">
                                <span style="font-size: 1.1em;">2014</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2014">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2014"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2013"
                               aria-expanded="false"
                               aria-controls="year2013">
                                <span style="font-size: 1.1em;">2013</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2013">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2013"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2012"
                               aria-expanded="false"
                               aria-controls="year2012">
                                <span style="font-size: 1.1em;">2012</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2012">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2012"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2011"
                               aria-expanded="false"
                               aria-controls="year2011">
                                <span style="font-size: 1.1em;">2011</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2011">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2011"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2010"
                               aria-expanded="false"
                               aria-controls="year2010">
                                <span style="font-size: 1.1em;">2010</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2010">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2010"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2009"
                               aria-expanded="false"
                               aria-controls="year2009">
                                <span style="font-size: 1.1em;">2009</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2009">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2009"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
                    <li class="clearfix agenda-year list-group-item">
                        <div class="agenda-label">
                            <a role="button"
                               data-toggle="collapse"
                               href="#year2008"
                               aria-expanded="false"
                               aria-controls="year2008">
                                <span style="font-size: 1.1em;">2008</span>
                                <span class="collapse-icon pull-right">
                                    <i class="fa fa-angle-down"></i>
                                </span>
                            </a>
                        </div>
                        <div class="details collapse "
                             id="year2008">
                            <ul class="list-group"
                                data-agenda-url="/Agenda/RetrieveAgendasForYear/Utrecht?agendatypeId=5&amp;year=2008"
                                style="margin-left: 15px;">
                                
                            </ul>
                        </div>
                    </li>
            </ul>
        </div>
    </aside>
    <section class="col-sm-8 col-md-9 maincontent">
        <div id="agenda">
            <div class="page-title">
                <h2>Commissie Mens en Samenleving</h2>
                <h4></h4>
                <strong>donderdag 23 april 2020</strong>
                <span>09:30 - 21:00</span>
            </div>
            <div class="details-top">
                <div class="detail-row row">
                    <div class="col-sm-3 detail-row-label">Locatie:</div>
                    <div class="col-sm-9 detail-row-text">Digitaal</div>
                </div>
                <div class="detail-row row">
                    <div class="col-sm-3 detail-row-label">Voorzitter:</div>
                    <div class="col-sm-9 detail-row-text">Voorzitter commissie</div>
                </div>
                                                    <div class="detail-row row">
                        <div class="col-sm-3 detail-row-label">Toelichting:</div>
                        <div class="col-sm-9 detail-row-text"><p>Uitnodiging voor de openbare vergadering van de commissie Mens en Samenleving, die wordt gehouden op 23 april 2020. Deze vergadering vindt digitaal plaat.. Op de agenda is indicatief het behandeltijdstip opgenomen. De leden van het college zijn uitgenodigd om aanwezig te zijn bij de behandeling van de onderwerpen die betrekking hebben op hun portefeuille.</p>
</div>
                    </div>

                    <div class="detail-row row">
                        <div class="col-sm-3 detail-row-label">Agenda documenten:</div>
                        <div class="col-sm-9 detail-row-text">
                            <ul class="attachments">
<li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=ffbcd3ff-ea2c-43b6-87d7-a50fd0df7ef5" class="unread" data-document-id="ffbcd3ff-ea2c-43b6-87d7-a50fd0df7ef5" aria-label="Open pdf Agendabundel">Agendabundel</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=02491fae-8494-4aff-b7db-f6569144057e" class="unread" data-document-id="02491fae-8494-4aff-b7db-f6569144057e" aria-label="Open pdf Dagschema 23 april 2020.xls">Dagschema 23 april 2020.xls</a>
</li>                            </ul>
                        </div>
                    </div>
            </div>
            <div class="agenda-title-row row">
                <div class="col-xs-8">
                    <h3>Agendapunten</h3>
                </div>
                <div class="col-xs-4">
                    <button class="btn btn-ibo pull-right"
                            style="display: none">
                        <i class="fa fa-download"></i>
                    </button>
                </div>
            </div>
            <div class="agendapunten">
                <ul class="list-group">
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">1</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#9dd57f2c-2709-476f-9461-dd726044f54a"
                                       aria-expanded="true"
                                       aria-controls="9dd57f2c-2709-476f-9461-dd726044f54a">
                                        Opening
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                                    <div class="details collapse in"
                                         id="9dd57f2c-2709-476f-9461-dd726044f54a">
                                                                                    <div class="explanation">
                                                <p><p>Aanvang: 9.30 uur</p>
</p>
                                            </div>
                                                                                                                                                                                                                                                                                    </div>
                            </div>
                        </li>
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">2</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#c9c356de-6dcb-4288-b911-b284bde4fccf"
                                       aria-expanded="true"
                                       aria-controls="c9c356de-6dcb-4288-b911-b284bde4fccf">
                                        Vaststellen agenda en inventarisatie te bespreken agendapunten
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                            </div>
                        </li>
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">3</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#591ddd06-e040-429d-b3b0-7bb03443ceae"
                                       aria-expanded="true"
                                       aria-controls="591ddd06-e040-429d-b3b0-7bb03443ceae">
                                        Verslagen
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                                    <div class="details collapse in"
                                         id="591ddd06-e040-429d-b3b0-7bb03443ceae">
                                                                                    <div class="explanation">
                                                <p><ul>
<li>Het geheime conceptverslag van de besloten commissie Mens en Samenleving van 30 januari 2020, met bijlage, ter vaststelling</li>
<li>Het conceptverslag van de openbare commissie Mens en Samenleving van 13 februari 2020, ter vaststelling</li>
<li>Het conceptverslag van de openbare commissie Mens en Samenleving van 2 april 2020, ter vaststelling</li>
<li>Het vastgestelde verslag van de Adviescommissie Controle en Financiën van 23 januari 2020, ter informatie</li>
</ul>
</p>
                                            </div>
                                                                                                                            <hr/>
                                            <div class="attachments-wrapper">
                                                <ul class="attachments">
<li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=a944f0d1-39c8-4ac2-9ed6-2585cad98f3a" class="unread" data-document-id="a944f0d1-39c8-4ac2-9ed6-2585cad98f3a" aria-label="Open pdf Concept Verslag commissie Mens en Samenleving, 2020-02-13.pdf">Concept Verslag commissie Mens en Samenleving, 2020-02-13.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=d46a422c-3fa6-4ddb-95d5-d4a6c3870174" class="unread" data-document-id="d46a422c-3fa6-4ddb-95d5-d4a6c3870174" aria-label="Open pdf Concept Verslag commissie Mens en Samenleving, 2020-04-02.pdf">Concept Verslag commissie Mens en Samenleving, 2020-04-02.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=620b4ea0-5103-4a22-befe-950c18f8f352" class="unread" data-document-id="620b4ea0-5103-4a22-befe-950c18f8f352" aria-label="Open pdf Notulen Adviescommissie CF 23-01-2020.docx">Notulen Adviescommissie CF 23-01-2020.docx</a>
</li>                                                </ul>
                                            </div>
                                                                                                                                                                                                    </div>
                            </div>
                        </li>
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">4.1</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#10712214-bd05-4986-b950-a4a2f40c15b7"
                                       aria-expanded="true"
                                       aria-controls="10712214-bd05-4986-b950-a4a2f40c15b7">
                                        Toezeggingen/moties/brievenlijst 
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                                    <div class="details collapse in"
                                         id="10712214-bd05-4986-b950-a4a2f40c15b7">
                                                                                    <div class="explanation">
                                                <p><p>Ter vaststelling</p>
</p>
                                            </div>
                                                                                                                            <hr/>
                                            <div class="attachments-wrapper">
                                                <ul class="attachments">
<li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=6a6f85ef-e46b-4ab5-910e-393f473ccfba" class="unread" data-document-id="6a6f85ef-e46b-4ab5-910e-393f473ccfba" aria-label="Open pdf Stavaza Moties-toezeggingen-brieven M&amp;S per 16-04-2020.xlsx">Stavaza Moties-toezeggingen-brieven M&amp;S per 16-04-2020.xlsx</a>
</li>                                                </ul>
                                            </div>
                                                                                                                                                                                                    </div>
                            </div>
                        </li>
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">4.2</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#c6e53bf7-0c95-4e53-8471-a79b977f9574"
                                       aria-expanded="true"
                                       aria-controls="c6e53bf7-0c95-4e53-8471-a79b977f9574">
                                        Lange Termijn Agenda
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                                    <div class="details collapse in"
                                         id="c6e53bf7-0c95-4e53-8471-a79b977f9574">
                                                                                    <div class="explanation">
                                                <p><p>Ter informatie</p>
</p>
                                            </div>
                                                                                                                            <hr/>
                                            <div class="attachments-wrapper">
                                                <ul class="attachments">
<li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=be901620-8787-4117-941f-0b6f81d4bfec" class="unread" data-document-id="be901620-8787-4117-941f-0b6f81d4bfec" aria-label="Open pdf Lange Termijn Agenda  M&amp;S d.d. 15 april 2020.xlsx">Lange Termijn Agenda  M&amp;S d.d. 15 april 2020.xlsx</a>
</li>                                                </ul>
                                            </div>
                                                                                                                                                                                                    </div>
                            </div>
                        </li>
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">5</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#a6110087-d59c-4f50-9d86-9d8687e3d124"
                                       aria-expanded="true"
                                       aria-controls="a6110087-d59c-4f50-9d86-9d8687e3d124">
                                        Raadsvoorstel Agenda en Uitvoeringsprogramma ‘Utrecht voor iedereen toegankelijk’
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                                    <div class="details collapse in"
                                         id="a6110087-d59c-4f50-9d86-9d8687e3d124">
                                                                                    <div class="explanation">
                                                <p><p>9.45 - 11.45 uur.<br />
Indicatieve behandeltijd: 90 min. ( + 30 min. pauze/schorsing na 1e termijn).<br />
Beleidsveld: Welzijn/ Maatschappelijke Ontwikkeling - wethouder Van Ooijen</p>
<p>Het college stelt de raad voor het volgende te besluiten:</p>
<ol>
<li>De agenda ‘Utrecht voor iedereen toegankelijk’ vast te stellen, waarmee wordt ingezet op<br />
de volgende drie kansen:</li>
<li>sneller concreet resultaat,</li>
<li>samenwerken met de stad ,</li>
<li>niet alleen fysiek, maar ook sociaal toegankelijk.</li>
</ol>
<p>Met de agenda ‘Utrecht voor iedereen toegankelijk’ wordt uitvoering gegeven aan de verplichting van het verdrag om een Lokale Inclusie Agenda op te stellen. Hierin staat hoe de gemeente Utrecht het VN-verdrag in praktijk brengt. Ook moet de gemeente in de plannen over de Wmo, Participatiewet en Jeugdwet zichtbaar maken hoe<br />
Het uitvoeringsprogramma vertaalt de ambitie en kansen uit de agenda naar concrete acties en laat zien wat de gemeente al doet en blijft doen én wat zij besluit om nieuw op te pakken.<br />
Het college heeft verder de nadere regels ‘Subsidie voor de toegankelijkheid van ondernemingen en organisaties’ vastgesteld. Met de subsidie toegankelijkheid kunnen ondernemingen en organisaties subsidie vragen voor het verbeteren van de toegankelijkheid.</p>
</p>
                                            </div>
                                                                                                                            <hr/>
                                            <div class="attachments-wrapper">
                                                <ul class="attachments">
<li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=d0e23172-c108-4eed-86d5-0c30d0ca9840" class="unread" data-document-id="d0e23172-c108-4eed-86d5-0c30d0ca9840" aria-label="Open pdf Dossier 828 voorblad.pdf">Dossier 828 voorblad.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=14247fe1-9413-48cd-8b2d-141c7eae5688" class="unread" data-document-id="14247fe1-9413-48cd-8b2d-141c7eae5688" aria-label="Open pdf Voorstel_12057.pdf">Voorstel_12057.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=48073751-990d-40d9-aa24-6fcc4d57368d" class="unread" data-document-id="48073751-990d-40d9-aa24-6fcc4d57368d" aria-label="Open pdf Agenda ‘Utrecht voor iedereen toegankelijk’.pdf">Agenda ‘Utrecht voor iedereen toegankelijk’.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=c83f2256-53c9-480a-90c4-214abe6c51d4" class="unread" data-document-id="c83f2256-53c9-480a-90c4-214abe6c51d4" aria-label="Open pdf Uitvoeringsprogramma ‘Utrecht voor iedereen toegankelijk’.pdf">Uitvoeringsprogramma ‘Utrecht voor iedereen toegankelijk’.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=c1481c9e-e0aa-46e6-9c46-5e0deef9098f" class="unread" data-document-id="c1481c9e-e0aa-46e6-9c46-5e0deef9098f" aria-label="Open pdf Nadere regels Subsidie toegankelijkheid ondernemingen en organisaties.pdf">Nadere regels Subsidie toegankelijkheid ondernemingen en organisaties.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=9126f105-63e3-4cad-bacc-0bb70f616560" class="unread" data-document-id="9126f105-63e3-4cad-bacc-0bb70f616560" aria-label="Open pdf Besluitenhistorie bij &#39;Utrecht voor iedereen toegankelijk&#39;.pdf">Besluitenhistorie bij &#39;Utrecht voor iedereen toegankelijk&#39;.pdf</a>
</li>                                                </ul>
                                            </div>
                                                                                                                                                                                                    </div>
                            </div>
                        </li>
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">6</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#c7adc926-ff20-4857-bb0f-d379d20573ca"
                                       aria-expanded="true"
                                       aria-controls="c7adc926-ff20-4857-bb0f-d379d20573ca">
                                        Raadsbrief U10 Governance 2020 - 2025
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                                    <div class="details collapse in"
                                         id="c7adc926-ff20-4857-bb0f-d379d20573ca">
                                                                                    <div class="explanation">
                                                <p><p>20.00 - 21.00 uur<br />
Indicatieve behandeltijd: 60 min.<br />
Beleidsveld: Bestuurlijke zaken - Burgemeester Van Zanen</p>
<p>Geagendeerd door C. Bos (Stadsbelang Utrecht), J. Wijmenga (ChristenUnie), P. van Corler (GroenLinks), H. van Deún (PVV), H. Dekker (D66), R. van der Zweth (PvdA), M. van Dalen (VVD)</p>
<p>Het college heeft ingestemd met de notitie U10 Governance 2020-2025. Als alle U10 colleges instemmen is de notitie de basis voor een hernieuwd U10-convenant. De U10 is en blijft een collegeregeling.<br />
Een poging om in de huidige regeling middels U10-beraden de positie van de gemeenteraden te borgen is niet gelukt. In de notitie heeft de positie van de raden aandacht, maar die moet vooral lokaal worden uitgewerkt. De notitie gaat uit van “stimuleren, dat de besluitvorming over regionale voorstellen plaatsvindt op basis van consent (toestemmen)’’. Dat plaatst de raad in een rol die de Eerste Kamer ook heeft. De raad mag akkoord gaan of juist niet. De bevoegdheid van de raad kan daardoor worden aangetast.</p>
<p>Dat is wellicht bespreekbaar, als de raad eerst de kaders heeft vastgesteld die voor het college de basis zijn voor de regionale afstemming. Dan is vervolgens de afweging te maken, in hoeverre een regionaal voorstel aan de gestelde lokale kaders beantwoord. Dat zal niet altijd geheel het geval zijn, maar dan is wel duidelijk waar er water in de wijn moet worden gedaan in verband met wensen of eisen van andere gemeenten.</p>
<p>De agenderende fracties willen graag met elkaar en het college bespreken hoe de bevoegdheid van de raad geborgd wordt in de regionale samenwerking. Daarmee hoeft niet gewacht te worden om een nadere uitwerking van het convenant. Dit jaar bespreken we in de raad immers belangrijke kaders (RSU, mobiliteitsplan e.d.) die een grote relatie hebben met regionale plannen als REP en RES. Het is van groot belang en het heeft ook urgentie dat het lokale besluitvormingsvormingsproces zorgvuldig wordt ingericht en daarmee de positie van de raad wordt geborgd.</p>
<p>Hierbij dient een lokale invulling te komen op de volgende punten uit de brief:</p>
<ol>
<li>de momenten en de wijze te benoemen waarop de Utrechtse raad besluiten moeten nemen;</li>
<li>heldere voorstellen te formuleren met oog voor ieders rol en verantwoordelijkheden (wat is daar voor nodig gelet op de impuls die al loopt rond de kwaliteit van stukken);</li>
<li>tijdig de voorstellen in roulatie te brengen, zodat raden hun eigen agenda kunnen plannen: wat is de planning welke we in Utrecht in 2020 hanteren voor de komende stukken?</li>
<li>te werken met uniformiteit in besluitvorming (een besluit vragen is overal een besluit krijgen) en af te stappen van het concept couleur lokale (onverlet de noodzaak van duiding van regionale voorstellen door elk college m.b.t. de gemeentelijke kaders en ambities). Ofwel op welke wijze worden stukken In Utrecht vergezeld van de tussen colleges afgesproken duiding m.b.t. Utrechtse kaders en ambities. Is de raadsbrief bij deze governance notitie een voorbeeld van die duiding en heeft deze dan de juiste inhoud.</li>
</ol>
</p>
                                            </div>
                                                                                                                            <hr/>
                                            <div class="attachments-wrapper">
                                                <ul class="attachments">
<li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=b411c5c7-e8c4-4a2e-b199-9e6249d8717d" class="unread" data-document-id="b411c5c7-e8c4-4a2e-b199-9e6249d8717d" aria-label="Open pdf Dossier 859 voorblad.pdf">Dossier 859 voorblad.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=270aac80-744b-40f7-aa33-d39b72f6f9fa" class="unread" data-document-id="270aac80-744b-40f7-aa33-d39b72f6f9fa" aria-label="Open pdf Raadsbrief U10 Governance 2020-2025.pdf">Raadsbrief U10 Governance 2020-2025.pdf</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=c0e80e29-371d-4164-bae0-e05d96231436" class="unread" data-document-id="c0e80e29-371d-4164-bae0-e05d96231436" aria-label="Open pdf U10 Governance 2020 - 2025.pdf">U10 Governance 2020 - 2025.pdf</a>
</li>                                                </ul>
                                            </div>
                                                                                                                                                                                                    </div>
                            </div>
                        </li>
                        <li class="clearfix">
                            <div class="col-xs-2 col-md-1 cal-agendapunt-nr">6.1</div>
                            <div class="col-xs-10 col-md-11">
                                <div class="cal-agendapunt-label">
                                    <a role="button"
                                       data-toggle="collapse"
                                       href="#e38214ef-b1d9-4e8f-8886-fa2e0746f963"
                                       aria-expanded="true"
                                       aria-controls="e38214ef-b1d9-4e8f-8886-fa2e0746f963">
                                        Overige documenten bij U10 Governance
                                        <span class="collapse-icon pull-right">
                                            <i class="fa fa-angle-up"></i>
                                        </span>
                                    </a>
                                </div>
                                    <div class="details collapse in"
                                         id="e38214ef-b1d9-4e8f-8886-fa2e0746f963">
                                                                                                                                                                    <hr/>
                                            <div class="attachments-wrapper">
                                                <ul class="attachments">
<li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=9abd6f1d-cf1d-404b-aca0-17ce5fd5f44a" class="unread" data-document-id="9abd6f1d-cf1d-404b-aca0-17ce5fd5f44a" aria-label="Open pdf Verslag RIB U10 Govenance.docx">Verslag RIB U10 Govenance.docx</a>
</li><li class="pdf">
    <a href="https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&amp;id=fadd97d3-5e67-4099-a943-3964f1231005" class="unread" data-document-id="fadd97d3-5e67-4099-a943-3964f1231005" aria-label="Open pdf Energie en democratie - essay Marcel Boogers oktober 2019.pdf">Energie en democratie - essay Marcel Boogers oktober 2019.pdf</a>
</li>                                                </ul>
                                            </div>
                                                                                                                                                                                                    </div>
                            </div>
                        </li>
                </ul>
            </div>
        </div>
    </section>
</div>
                </div>
            </div>
        </div>
        
    </div>

    <script src="/Scripts/libs?v=er4ck2euGrTc6eCsvVjzcyiAkiQ9AIFtuilXomeLJXA1"></script>

    <script src="/bundles/localization/nl?v=3w_lslyFCpT2HVLWIC6arWsfd-6JOEAJATlqXets1pA1"></script>

    <script src="/Scripts/scripts?v=JJIDK3_aJziZhX5PvbCWXNgYGmAerVjWHmJhrESR-Zo1"></script>


    

    <script>
        $(function() {
            ibabs.setActiveNavigationItem("nav-item-calendar");

            google.charts.load('current', { 'packages': ['corechart'] });


            ibabs.agenda.init();

                
            var docArray = [];
                         docArray.push('ffbcd3ff-ea2c-43b6-87d7-a50fd0df7ef5');
                         docArray.push('02491fae-8494-4aff-b7db-f6569144057e');
            ibabs.document.checkReadDocuments(docArray);
            

                var agendaItemDocArray = [];
                     agendaItemDocArray.push('a944f0d1-39c8-4ac2-9ed6-2585cad98f3a');
                     agendaItemDocArray.push('d46a422c-3fa6-4ddb-95d5-d4a6c3870174');
                     agendaItemDocArray.push('620b4ea0-5103-4a22-befe-950c18f8f352');
                     agendaItemDocArray.push('6a6f85ef-e46b-4ab5-910e-393f473ccfba');
                     agendaItemDocArray.push('be901620-8787-4117-941f-0b6f81d4bfec');
                     agendaItemDocArray.push('d0e23172-c108-4eed-86d5-0c30d0ca9840');
                     agendaItemDocArray.push('14247fe1-9413-48cd-8b2d-141c7eae5688');
                     agendaItemDocArray.push('48073751-990d-40d9-aa24-6fcc4d57368d');
                     agendaItemDocArray.push('c83f2256-53c9-480a-90c4-214abe6c51d4');
                     agendaItemDocArray.push('c1481c9e-e0aa-46e6-9c46-5e0deef9098f');
                     agendaItemDocArray.push('9126f105-63e3-4cad-bacc-0bb70f616560');
                     agendaItemDocArray.push('b411c5c7-e8c4-4a2e-b199-9e6249d8717d');
                     agendaItemDocArray.push('270aac80-744b-40f7-aa33-d39b72f6f9fa');
                     agendaItemDocArray.push('c0e80e29-371d-4164-bae0-e05d96231436');
                     agendaItemDocArray.push('9abd6f1d-cf1d-404b-aca0-17ce5fd5f44a');
                     agendaItemDocArray.push('fadd97d3-5e67-4099-a943-3964f1231005');
                ibabs.document.checkReadDocuments(agendaItemDocArray);

        });
    </script>


        <script src="/Scripts/Sites/utrecht.min.js"></script>

    <script>
        var uiCulture = 'nl';
        var culture = 'nl';
        var uiLanguage = 'nl';
        $(function () {
            ibabs.dataTables.init();

            $('#changeFonts').on('click',
                'a',
                function (e) {
                    e.preventDefault();

                    ibabs.changeFonts($(this));
                });
        });
    </script>
</body>
</html>
"""