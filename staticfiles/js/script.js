// script.js
/*
const modal = document.getElementById("myModal");
const btn = document.getElementById("open-modal-button");
const span = document.getElementsByClassName("close")[0];
const modalContent = document.getElementById("modal-form-content");

btn.onclick = function() {
  $.ajax({
    url: "/member-form/",
    type: "GET",
    success: function(data) {
      modalContent.innerHTML = data;
      modal.style.display = "block";
    },
    error: function() {
      alert("Error loading form.");
    }
  });
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$(document).on('submit', '#myform', function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/my-form/',
        data: $(this).serialize(),
        success: function(response){
            $('#modal-form-content').html('<p>' + response.message + '</p>');
        },
        error: function(response){
            $('#modal-form-content').html(response.responseJSON.errors);
        }
    });
});
*/