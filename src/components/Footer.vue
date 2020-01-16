<template>
  <div class=" bg-brown">
    <footer>
      <div class="container-fluid">
        <b-row
          align-v="center"
          class="footer pt-3"
        >
          <b-col
            xl="2"
            lg="3"
            md="3"
            sm="12"
          >
            <div class="footer-title text-center">
              Taxi Aktiv Köln <br>
              Nick Active
            </div>
          </b-col>
          <b-col
            xl="8"
            lg="8"
            md="8"
            sm="12"
            class="p-0 text-center"
          >
            <a
              :href="`/${$i18n.locale}/jobs`"
             
              class=" footer-link"
            >ВАКАНСИИ</a>
            <a
              href=""
              class=" footer-link"
            >AGB</a>
            <a
              href=""
              class=" footer-link"
            >DATENSHUTZ</a>
            <a
              href=""
              class=" footer-link"
            >Отказ от ответственности</a>
          </b-col>
          <b-col
            xl="2"
            lg="12"
            md="12"
            class="text-center"
          >
            <a
              
              href="#"   
            >
              <img
                class="ico"
                src="../img/icons/you.svg"
                alt=""
              >
            </a>
            <a
              
              href="#"
            > <img
              class="ico"
              src="../img/icons/inst.svg"
              alt=""
            ></a>
            <a
              
              href="#"
            ><img
              class="ico"
              src="../img/icons/fb.svg"
              alt=""
            ></a>
          </b-col>
          <b-col xl="12 my-3">
            <div class="text-center akman">
              © MPNETWORK copyright 2020
            </div>
          </b-col>
        </b-row>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
    name: "Footer",
};
</script>

<style>
.bg-brown {
  background-color: #534E4E !important;
}
.akman {
  font-weight: 300;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #9D9D9D;
}

.footer-title {
 font-weight: 500;
 font-size: 24px;
 line-height: 28px;
 color: #C4C4C4;
}
.footer-title::before {
 content: "";
 position: absolute;
 width: 51px;
 height: 60px;
 left: 120px;
 top: 17px;
 border-left: 2px solid rgba(255, 236, 1, 0.27);
 transform: rotate(50deg);
}
.footer-title::after {
 content: "";
 position: absolute;
 width: 51px;
 height: 60px;
 left: 150px;
 top: 17px;
 border-left: 2px solid rgba(255, 236, 1, 0.27);
 transform: rotate(50deg);
}
.footer-link {
 padding: 10px 20px;
 font-weight: 300;
 font-size: 14px;
 line-height: 16px;
 letter-spacing: 0.04em;
 text-transform: uppercase;
 color: #C4C4C4;
 border-right: 0.5px solid #FFEC01;
}
.footer-link:hover {
  color: aliceblue
}
@media (max-width: 900px) {
 .footer-link{
    margin: 5px auto;
    display: block !important;
    text-align: center !important;
    width: 80%;
    border-left: 0.5px solid #FFEC01;
}
}
@media (max-width: 775px) {
  .footer-title::after, .footer-title::before {
   display: none;
}  
}
.ico {
  width: 35px;
  height: 40px;
  margin: 10px;
}
</style>
