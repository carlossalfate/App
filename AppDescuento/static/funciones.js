document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.getElementById("overlay");
  const modal = document.getElementById("modal");
  const activarNotificacionesBtn = document.getElementById('activar-notificaciones');
  const cerrarModalBtn = document.getElementById('cerrar-modal');

  if (activarNotificacionesBtn && overlay) {
      activarNotificacionesBtn.addEventListener('click', function() {
          overlay.style.display = 'flex';
      });
  }

  if (cerrarModalBtn) {
      cerrarModalBtn.addEventListener('click', function() {
          overlay.style.display = 'none';
      });
  }

  if (overlay) {
      overlay.addEventListener("click", function(event) {
          if (event.target === this) {
              this.style.display = 'none';
          }
      });
  }

  if (modal) {
      modal.addEventListener("click", function(event) {
          event.stopPropagation();
      });
  }

  mostrarProductosDelCarrito();
  actualizarTotal();
});
function addToCart(productId, productName, productPrice, productDiscount = 0, productImage) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¿Seguro que desea añadir este producto al carrito?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, añadir al carrito',
        cancelButtonText: 'No, cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            const discountDecimal = productDiscount / 100; // Convierte a decimal
            const product = {
                  id: productId,
                  name: productName,
                  price: productPrice,
                  discount: discountDecimal,
                  image: productImage // Añade la imagen aquí
            };

            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            cart.push(product);
            localStorage.setItem('cart', JSON.stringify(cart));

            $('#cartModal').modal('show');
            mostrarProductosDelCarrito();
            actualizarTotal();

            // Muestra el mensaje de éxito después de añadir al carrito
            Swal.fire(
                'Añadido!',
                'El producto ha sido añadido al carrito.',
                'success'
            );
        } else {
            // Mensaje de no añadido
            Swal.fire(
                'Cancelado',
                'El producto no ha sido añadido al carrito.',
                'error'
            );
        }
    });
}

function mostrarProductosDelCarrito() {
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  const cartTable = document.getElementById('cart-table');

  if (cart.length === 0) {
      document.getElementById('cart-content').style.display = 'none';
      document.getElementById('empty-cart-message').style.display = 'block';
  } else {
      document.getElementById('cart-content').style.display = 'block';
      document.getElementById('empty-cart-message').style.display = 'none';

      const cartTableBody = cartTable.getElementsByTagName('tbody')[0];
      cartTableBody.innerHTML = '';

      cart.forEach((product, index) => {
          const row = cartTableBody.insertRow();

          const imageCell = row.insertCell(0);
          const img = document.createElement('img');
          img.src = product.image;
          img.alt = product.name;
          img.style.width = '50px';
          imageCell.appendChild(img);

          const nameCell = row.insertCell(1);
          nameCell.textContent = product.name;

          const priceCell = row.insertCell(2);
          priceCell.textContent = `$${product.price}`;

          const discountCell = row.insertCell(3);
          discountCell.textContent = `${(product.discount * 100).toFixed(2)}%`;

          const totalCell = row.insertCell(4);
          totalCell.textContent = `$${(product.price * (1 - product.discount)).toFixed(2)}`;

          const deleteCell = row.insertCell(5);
          const deleteButton = document.createElement('button');
          deleteButton.textContent = 'Eliminar';
          deleteButton.className = 'btn btn-danger';
          deleteButton.onclick = function() {
              eliminarDelCarrito(index);
          };
          deleteCell.appendChild(deleteButton);
      });
  }
}

function actualizarTotal() {
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  let totalSinDescuento = 0;
  let totalDescuento = 0;

  cart.forEach(product => {
      totalSinDescuento += product.price;
      totalDescuento += product.price * product.discount;
  });

  const totalConDescuento = totalSinDescuento - totalDescuento;
  document.getElementById('total-price').textContent = `CLP$${Math.round(totalConDescuento)}`;
  document.getElementById('total-discount').textContent = `${((totalDescuento / totalSinDescuento) * 100).toFixed(2)}%`;
  document.getElementById('total-saved').textContent = `CLP$${Math.round(totalDescuento)}`;
}

function eliminarDelCarrito(index) {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  if (index > -1 && index < cart.length) {
      cart.splice(index, 1);
      localStorage.setItem('cart', JSON.stringify(cart));
      mostrarProductosDelCarrito();
      actualizarTotal();
  }
}

function realizarPago() {
  if (JSON.parse(localStorage.getItem('cart')).length === 0) {
      alert('Tu carrito está vacío');
      return;
  }
  
  $('#paymentModal').modal('show');
}

    document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const paymentMethod = document.getElementById('payment-method').value;

    alert(`Gracias por tu compra. Has elegido pagar con ${paymentMethod}.`)
        .then(() => {
            // Después de que el usuario cierra el mensaje, realiza las siguientes acciones
            $('#paymentModal').modal('hide'); // Cierra el modal

        localStorage.removeItem('cart');
        mostrarProductosDelCarrito();
        actualizarTotal();
    });
});