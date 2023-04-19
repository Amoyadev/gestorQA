// Encuentra el campo de búsqueda y la tabla
const search = document.getElementById('search-input');
const table = document.querySelector('table');

// Encuentra el encabezado de la tabla
const tableHeader = document.getElementById('tabla-encabezado');

// Agrega un evento "keyup" al campo de búsqueda
search.addEventListener('keyup', function(event) {
  // Obtén el valor del campo de búsqueda y conviértelo a minúsculas
  const value = event.target.value.toLowerCase();

  // Encuentra todas las filas de datos de la tabla
  const rows = table.querySelectorAll('tbody tr');

  // Itera sobre todas las filas y oculta aquellas que no coincidan con el valor de búsqueda
  rows.forEach(row => {
    const columns = row.querySelectorAll('td');
    let found = false;
    columns.forEach(column => {
      if (column.innerText.toLowerCase().includes(value)) {
        found = true;
      }
    });
    if (found) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });

  // Muestra el encabezado de la tabla
  tableHeader.style.display = '';
  // Encuentra todas las filas de la tabla
  const allRows = table.querySelectorAll('tr');
  // Si todas las filas están ocultas, oculta también el encabezado
  let allHidden = true;
  allRows.forEach(row => {
    if (row.style.display !== 'none') {
      allHidden = false;
    }
  });
  if (allHidden) {
    tableHeader.style.display = 'none';
  }
});