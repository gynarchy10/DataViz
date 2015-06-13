
fetch('./api/c3Data.json')
  .then(
    function(response) {
      if (response.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' +
          response.status);
        return;
      }

      // Examine the text in the response
      response.json().then(function(data) {
        console.log(data);
        var chart = c3.generate({
            data: {
                columns: data.columns,
                type: 'bar',
                groups: data.groups,
                order: null
            },
            grid: {
                y: {
                    lines: [{value:0}]
                }
            }
        });
      });
    }
  )
  .catch(function(err) {
    console.log('Fetch Error :-S', err);
  });
