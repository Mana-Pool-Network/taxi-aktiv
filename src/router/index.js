/* eslint-disable indent */
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import i18n from '../i18n';
Vue.use(VueRouter);

const routes = [{
    path: '/',
    redirect: `/${i18n.locale}`
}, {
    path: '/:lang',
    component: {
        render(c) { return c('router-view') }
    },
    children: [{
            path: "/",
            name: "home",
            component: Home,
            props: true,
        },
        {
            path: "services",
            name: "services",
            component: () =>
                import ("../views/Services.vue"),
        },
        {
            path: "limousine-service",
            name: "limousineservice",
            component: () =>
                import ("../views/service/LimousineService.vue"),
        },
        {
            path: "shuttle-service",
            name: "shuttleservice",
            component: () =>
                import ("../views/service/ShuttleService.vue"),
        },
        {
            path: "female-service",
            name: "femaleservice",
            component: () =>
                import ("../views/service/FemaleService.vue"),
        },
        {
            path: "medical-service",
            name: "medicalservice",
            component: () =>
                import ("../views/service/MedicalService.vue"),
        },
        {
            path: "about-us",
            name: "aboutus",
            component: () =>
                import ("../views/AboutUs.vue"),
        },
        {
            path: "about-company",
            name: "aboutcompany",
            component: () =>
                import ("../views/aboutus/AboutCompany.vue"),
        },
        {
            path: "driver-training",
            name: "DriverTraining",
            component: () =>
                import ("../views/aboutus/AboutDriverTraining.vue"),
        },
        {
            path: "software",
            name: "Software",
            component: () =>
                import ("../views/aboutus/AboutSoftware.vue"),
        },
        {
            path: "contacts",
            name: "contacts",
            component: () =>
                import ("../views/Contacts.vue"),
        },
        {
            path: "flot",
            name: "flot",
            component: () =>
                import ("../views/Flot.vue"),
        },
        {
            path: "ecology",
            name: "ecology",
            component: () =>
                import ("../views/Ecology.vue"),
        },
        {
            path: "jobs",
            name: "jobs",
            component: () =>
                import ("../views/Jobs.vue"),
        },
        {
            path: "responsibility",
            name: "responsibility",
            component: () =>
                import ("../views/Responsibility.vue"),
        },
        {
            path: "datenshutz",
            name: "datenshutz",
            component: () =>
                import ("../views/Datenshutz.vue"),
        },
    ]
}];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;