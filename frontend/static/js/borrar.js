let loading = document.getElementById('loading');
const resultsPre = document.getElementById('resultados-pre');
const clearAllButton = document.getElementById('borrar-todo');

clearAllButton.addEventListener('click', () => {
  loading.style.display = 'flex';

  function fetchData() {
    var apiUrl = 'http://localhost:5000/api/v1/mascotas';
    fetch(apiUrl, {
      method: 'DELETE'
    })
      .then(response => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Error en la solicitud DELETE');
        }
      })
      .then(data => {
        resultsPre.innerText = formatXML(data).replace(/></g, '>\n<');
      })
      .catch(error => {
        resultsPre.innerText = 'Error: ' + error.message;
      })
      .finally(() => {
        loading.style.display = 'none';
        resultsPre.style.display = 'flex';
      });
  }
  fetchData();
});
