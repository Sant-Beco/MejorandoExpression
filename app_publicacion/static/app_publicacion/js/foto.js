document.getElementById('uploadInput').addEventListener('change', function(event) {
  var file = event.target.files[0];
  if (!file) {
      return;
  }

  var reader = new FileReader();
  reader.onload = function(e) {
      var preview = document.getElementById('imagePreview');
      preview.innerHTML = '';
      var img = document.createElement('img');
      img.src = e.target.result;
      img.classList.add('preview-image');
      preview.appendChild(img);
  };
  reader.readAsDataURL(file);
});
