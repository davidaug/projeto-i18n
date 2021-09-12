import { createI18n } from 'vue-i18n';

const messages = {
    en : require('./en.json'),
    br: require('./br.json'),
    es: require('./es.json')
};

const i18n = createI18n (
    {
        locale: "br",
        fallbackLocale: "en",
        messages
    }
);

export default i18n;
