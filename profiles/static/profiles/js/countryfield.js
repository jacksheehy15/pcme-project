// Taken from Boutiqu Ado https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/149abda4318106704ac8d3118b8e5a63ef070619/profiles/static/profiles/js/countryfield.js
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});