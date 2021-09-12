<template>
    <div> 
        <span @click="changeLocale('br')" class="flag-icon flag-icon-br m-2"></span>
        <span @click="changeLocale('en')" class="flag-icon flag-icon-us m-2"></span>
        <span @click="changeLocale('es')" class="flag-icon flag-icon-es m-2"></span>
    </div>
</template>

<script>
export default {
    methods: {
        changeLocale(locale){
            this.$root.$i18n.locale = locale;
        }
    }
}
</script>

<style scoped>

.m-2{
    margin: 2px;
}


@import "https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.5.0/css/flag-icon.min.css";


</style>