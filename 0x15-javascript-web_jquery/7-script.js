$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  $('#character').html(data.name);
});