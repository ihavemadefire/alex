document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('isbn-lookup-form');
  if (!form) return;

  form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const csrfToken = formData.get('csrfmiddlewaretoken');

    const response = await fetch(form.action, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Accept': 'application/json',
      },
      body: formData,
    });

    const data = await response.json();
    const resultDiv = document.getElementById('lookup-result');

    if (data.success) {
      resultDiv.innerHTML = `
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">${data.title}</h5>
            <p class="card-text">Author: ${data.creator}</p>
            <p class="card-text">ISBN: ${data.isbn}</p>
            <button class="btn btn-primary" id="add-book-button">Add to My Library</button>
          </div>
        </div>
      `;

      document.getElementById('add-book-button').addEventListener('click', async () => {
        const addResponse = await fetch("/media/books/add/", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
          },
          body: JSON.stringify(data),
        });

        const addData = await addResponse.json();
        resultDiv.innerHTML = `<div class="alert alert-success">${addData.message}</div>`;
      });
    } else {
      resultDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
    }
  });
});
