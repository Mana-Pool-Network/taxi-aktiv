<template>
  <div class="responsibility">
    <div class="content">
      <main class="container mt-5 mb-5">
        <div class="container">
          <div class="aboutus-block text-center">
            <div class="aboutus-block__title">
              Datenshutz
            </div>
          </div>
        </div>
        <b-row>
          <b-col
            xl="12"
            lg="12"
          >
            <div class="responsibility-title text-center my-4">
              Datenschutzerklärung für die Nutzung von Facebook-Plugins (Like-Button)
            </div>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="ecology-text">
              Auf unseren Seiten sind Plugins des sozialen Netzwerks Facebook, 
              Anbieter Facebook Inc., 1 Hacker Way, Menlo Park, California 94025, USA, integriert. 
              Die Facebook-Plugins erkennen Sie an dem Facebook-Logo oder dem „Like-Button“ („Gefällt mir“) auf unserer Seite. 
              Eine Übersicht über die Facebook-Plugins finden Sie hier: <a
                class="responsibility-a"
                href="http://developers.facebook.com/docs/plugins/"
              >http://developers.facebook.com/docs/plugins/ </a>.
            </p><p class="ecology-text">
              Wenn Sie unsere Seiten besuchen, wird über das Plugin eine direkte Verbindung zwischen Ihrem Browser und dem 
              Facebook-Server hergestellt. Facebook erhält dadurch die Information, dass Sie 
              mit Ihrer IP-Adresse unsere Seite besucht haben.
            </p>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="ecology-text">
              Wenn Sie den Facebook „Like-Button“ anklicken während Sie in Ihrem Facebook-Account eingeloggt sind, 
              können Sie die Inhalte unserer Seiten auf Ihrem Facebook-Profil verlinken. 
              Dadurch kann Facebook den Besuch unserer Seiten Ihrem Benutzerkonto zuordnen. 
              Wir weisen darauf hin, dass wir als Anbieter der Seiten keine Kenntnis vom Inhalt der 
              übermittelten Daten sowie deren Nutzung durch Facebook erhalten. 
              Weitere Informationen hierzu finden Sie in der Datenschutzerklärung von Facebook unter <a
                class="responsibility-a"
                href="http://de-de.facebook.com/policy.php."
              >http://de-de.facebook.com/policy.php.</a>
            </p>
            <p class="ecology-text">
              Wenn Sie nicht wünschen, dass Facebook den Besuch unserer Seiten Ihrem Facebook-Nutzerkonto zuordnen kann, 
              loggen Sie sich bitte aus Ihrem Facebook-Benutzerkonto aus.
            </p>
          </b-col>
          <b-col
            xl="12"
            lg="12"
          >
            <div class="responsibility-title text-center my-4">
              Datenschutzerklärung für die Nutzung von Google Analytics
            </div>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="ecology-text">
              Diese Website nutzt Funktionen des Webanalysedienstes Google Analytics. 
              Anbieter ist die Google Inc. 1600 Amphitheatre Parkway Mountain View, CA 94043, USA. 
              Google Analytics verwendet sog. „Cookies“. Das sind Textdateien, die auf Ihrem Computer 
              gespeichert werden und die eine Analyse der Benutzung der Website durch Sie ermöglichen. 
              Die durch den Cookie erzeugten Informationen über Ihre Benutzung dieser Website werden in der 
              Regel an einen Server von Google in den USA übertragen und dort gespeichert.
            </p>
            <p class="ecology-text">
              Im Falle der Aktivierung der IP-Anonymisierung auf dieser Webseite wird Ihre IP-Adresse von Google 
              jedoch innerhalb von Mitgliedstaaten der Europäischen Union oder in anderen Vertragsstaaten des 
              Abkommens über den Europäischen Wirtschaftsraum zuvor gekürzt. Nur in Ausnahmefällen wird die volle 
              IP-Adresse an einen Server von Google in den USA übertragen und dort gekürzt. Im Auftrag des Betreibers
              dieser Website wird Google diese Informationen benutzen, um Ihre Nutzung der Website auszuwerten, um Reports 
              über die Websiteaktivitäten zusammenzustellen und um weitere mit der Websitenutzung und der Internetnutzung 
              verbundene Dienstleistungen gegenüber dem Websitebetreiber zu erbringen. Die im Rahmen von Google Analytics 
              von Ihrem Browser übermittelte IP-Adresse wird nicht mit anderen Daten von Google zusammengeführt.
            </p>
          </b-col>
          <b-col
            xl="6"
            lg="6"
          >
            <p class="ecology-text">
              Sie können die Speicherung der Cookies durch eine entsprechende Einstellung Ihrer Browser-Software verhindern; 
              wir weisen Sie jedoch darauf hin, dass Sie in diesem Fall gegebenenfalls nicht sämtliche Funktionen dieser Website 
              vollumfänglich werden nutzen können. Sie können darüber hinaus die Erfassung der durch das Cookie erzeugten und auf 
              Ihre Nutzung der Website bezogenen Daten (inkl. Ihrer IP-Adresse) an Google sowie die Verarbeitung dieser Daten durch 
              Google verhindern, indem sie das unter dem folgenden Link verfügbare Browser-Plugin herunterladen 
              und installieren: <a
                class="responsibility-a"
                href="http://tools.google.com/dlpage/gaoptout?hl=de"
              >http://tools.google.com/dlpage/gaoptout?hl=de</a> 
            </p>
          </b-col>
        </b-row>
      </main>
    </div>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Footer from "@/components/Footer.vue";
export default {
    name: "Datenshutz",
    components: {
        Footer
    }
};

</script>

<style>

</style>