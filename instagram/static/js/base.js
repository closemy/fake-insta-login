function changeLanguage(lang) {
    var elements = document.querySelectorAll('[data-lang]');

    for (var i = 0; i < elements.length; i++) {
        var el = elements[i];
        var translations = JSON.parse(el.dataset.lang);
        var translatedText = translations[lang];
        el.innerText = translatedText;
    }
}
document.addEventListener('DOMContentLoaded', function () {
    changeLanguage('tr');
});



    
    
