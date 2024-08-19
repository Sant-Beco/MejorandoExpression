//sweetalert

// Subir publicaciòn


// const publicacion_boton_publicar = document.getElementById('publicacion_boton_publicar');

// publicacion_boton_publicar.addEventListener('click', function() {
//   Swal.fire({
//     title: "¿Deseas postear esta publicaciòn?",
//     footer: "Recuerda que tu publicaciòn debe ser coherente con las reglas de negocio de Cultural Expression",
//     icon: "danger",
//     showCancelButton: true,
//     confirmButtonColor: "#0ff",
//     cancelButtonColor: "#f00",
//     confirmButtonText: "Aceptar"
//   }).then((result) => {
//     if (result.isConfirmed) {
//       Swal.fire({
//         title: "Publicaciòn exitosa",
//         text: "¡Tù publicaciòn se ha publicado exitosamente!", 
//         icon: "success"
//       });
//     }
//   });
// });


// // ---------------------------------------------------------------



// // Publicar convocatoria


// const convocatoria_boton_publicar = document.getElementById('convocatoria_boton_publicar');

// convocatoria_boton_publicar.addEventListener('click', function() {
// Swal.fire({
//   title: "¿Deseas postear esta convocatoria?",
//   footer: "Recuerda que tu publicaciòn debe ser coherente con las reglas de negocio de Cultural Expression",
//   showCancelButton: true,
//   confirmButtonColor: "#0ff",
//   cancelButtonColor: "#f00",
//   confirmButtonText: "Aceptar"
// }).then((result) => {
//   if (result.isConfirmed) {
//     Swal.fire({
//       title: "Publicaciòn exitosa",
//       text: "Tù convocatoria se ha publicado exitosamente.", 
//       icon: "success"
//     });
//   }
// });
// });


// //--------------------------------------------


// // Postear producto

// const producto_boton_publicar = document.getElementById('producto_boton_publicar');

// producto_boton_publicar.addEventListener('click', function() {
// Swal.fire({
//   title: "¿Deseas postear este anuncio de producto?",
//   footer: "Recuerda que tu publicaciòn debe ser coherente con las reglas de negocio de Cultural Expression",
//   showCancelButton: true,
//   confirmButtonColor: "#0ff",
//   cancelButtonColor: "#f00",
//   confirmButtonText: "Aceptar"
// }).then((result) => {
//   if (result.isConfirmed) {
//     Swal.fire({
//       title: "Publicaciòn exitosa",
//       text: "Tù anuncio se ha publicado exitosamente",
//       icon: "success"
//     });
//   }
// });
// }); 

//--------------------------------------------


// Eliminar post

const eliminar_post = document.getElementById('eliminar_post');

eliminar_post.addEventListener('click', function() {
Swal.fire({
  title: "¿Deseas eliminar este post?",
  icon: "warning",
  showCancelButton: true,
  confirmButtonColor: "#0ff",
  cancelButtonColor: "#f00",
  confirmButtonText: "Aceptar"
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire({
      title: "¡Post eliminada exitosamente!", 
      icon: "success"
    });
  }
});
});