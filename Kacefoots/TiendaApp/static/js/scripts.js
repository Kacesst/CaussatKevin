/*!
* Start Bootstrap - Landing Page v6.0.6 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function agregarAlCarrito(productoId) {
    // Realizar una solicitud AJAX para agregar el producto al carrito
    // utilizando el ID del producto
    
    // Crear el objeto XMLHttpRequest
    var xhr = new XMLHttpRequest();
    
    // Configurar la solicitud
    xhr.open('POST', '/agregar_producto/' + productoId + '/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    
    // Manejar la respuesta de la solicitud
    xhr.onload = function() {
        if (xhr.status === 200) {
            // La solicitud fue exitosa
            // Redirigir al usuario a la página de confirmación
            window.location.href = '/confirmacion/';
        } else {
            // La solicitud falló
            // Mostrar un mensaje de error al usuario
            alert('No se pudo agregar el producto al carrito. Por favor, inténtalo de nuevo.');
        }
    };
    
    // Enviar la solicitud
    xhr.send();
}

