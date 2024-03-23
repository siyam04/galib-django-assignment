let offset = 0
const limit = 12; // Number of products to fetch per request

window.addEventListener('scroll', function() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      fetchMoreProducts();
    }
});

function fetchMoreProducts() {
    fetch(`http://localhost:8000/api/products/?offset=${offset}&limit=${limit}`)
      .then(response => response.json())
      .then(data => {
        data.forEach(product => {
          const productHtml = `
            <div class="product">
               <p>${product.id}</p>
               <h3>${product.name}</h3>
               <p>${product.price}</p>
               <p>${product.description}</p>
               <p>${product.seller.username}</p>
               <hr>
            </div>
          `;
          document.getElementById('product-list').insertAdjacentHTML('beforeend', productHtml);
        });
        offset += data.length;
      })
      .catch(error => console.error('Error fetching more products:', error));
}
