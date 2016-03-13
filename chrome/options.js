function toggle(radioButton) {
  if (window.localStorage == null) {
    alert('Local storage is required for changing providers');
    return;
  }

  window.localStorage.breadCrumbsServerURL = document.getElementById('serverURL').value;
}

function main() {
  if (window.localStorage == null) {
    alert("LocalStorage must be enabled for changing options.");
    document.getElementById('serverURL').disabled = true;
    return;
  }

  //"http://adelpozo.xyz/breadcrumbs"
  document.getElementById('serverURL').value = window.localStorage.breadCrumbsServerURL;
}

document.addEventListener('DOMContentLoaded', function () {
  main();
  document.querySelector('#savebtn').addEventListener('click', toggle);
});
