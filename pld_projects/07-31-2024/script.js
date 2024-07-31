$('document').ready(function () {
  $('#randomWis').click(function () {
    $.getJSON('https://uselessfacts.jsph.pl/api/v2/facts/random', function (data) {
      $('#fact').text(data.text)
    });
  });
});
