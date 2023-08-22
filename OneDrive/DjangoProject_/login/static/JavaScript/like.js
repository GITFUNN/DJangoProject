document.getElementById("likeForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el comportamiento predeterminado del formulario
  
    // Realiza aquí cualquier otro procesamiento o envío del formulario que necesites
  
    // Opcional: Puedes mostrar un mensaje o realizar otra acción después del envío del formulario
  
    // Finalmente, puedes mantener la posición de la pantalla utilizando el método scrollTo
    window.scrollTo({
      top: window.scrollY, // Mantén la posición actual
      behavior: "smooth" // Opcional: animación de desplazamiento suave
    });
  });