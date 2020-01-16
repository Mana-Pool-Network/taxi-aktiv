import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import i18n from './i18n';
import VueRecaptcha from "vue-recaptcha";
import Vwow from "v-wow";


Vue.use(Vwow);
Vue.use(VueRecaptcha);
Vue.use(BootstrapVue);
Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
    let language = to.params.lang;
    if (!language) {
        language = "de";
    }
    i18n.locale = language;
    next();
})

new Vue({
    router,
    store,
    i18n,
    render: h => h(App)
}).$mount("#app");