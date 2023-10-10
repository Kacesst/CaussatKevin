// Asegúrate de que jQuery se carga primero
$(document).ready(function() {
  // Llamado de prueba
  agregarAlCarrito(1);

  // Manejar clic en la imagen para mostrar en grande
  $('.card-img-top').click(function() {
      const imagenSrc = $(this).attr('src');
      $('#imagen-grande').attr('src', imagenSrc);
      $('#imagen-en-grande').css('display', 'block');
  });

  // Función para cerrar la imagen en grande
  function cerrarImagen() {
      $('#imagen-en-grande').css('display', 'none');
  }

  // Función para agregar producto al carrito
  function agregarAlCarrito(productoId) {
      console.log('Agregando producto:', productoId);

      fetch(`/agregar-producto/${productoId}/`)
          .then(response => response.json())
          .then(data => {
              // Actualizar carrito en frontend
              console.log('Producto agregado', data);

              // Puedes realizar acciones adicionales en el frontend aquí
          });
  }

  // Manejar clic en el botón "Agregar al carrito"
  $('.agregar-carrito').click(function() {
      const productoId = $(this).data('producto-id');

      $.ajax({
          url: '/agregar_al_carrito/',
          method: 'POST',
          data: {
              productoId: productoId,
              csrfmiddlewaretoken: '{{ csrf_token }}' // Asegúrate de que el token CSRF esté disponible en tu template
          },
          success: function(response) {
              console.log('Producto agregado al carrito');
              // Aquí puedes realizar cualquier acción adicional que desees, como actualizar la cantidad en el carrito o mostrar un mensaje de confirmación.
          },
          error: function(xhr, status, error) {
              console.error(error);
          }
      });
  });
});
