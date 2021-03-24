var suebox = document.querySelector('input[id=sue]');
var databox = document.querySelector('input[id=data]')
var startdate = document.querySelector('section[id=start-date]')

// If both checkboxes are checked, display the start date picker.
suebox.addEventListener('change', function() {
    if (this.checked && databox.checked) {
      startdate.classList.remove('hidden');
    }
  });

databox.addEventListener('change', function() {
    if (this.checked && suebox.checked) {
      startdate.classList.remove('hidden');
    }
  });