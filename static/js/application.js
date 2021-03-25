var suebox = document.querySelector('input[id=sue]');
var databox = document.querySelector('input[id=data]')
var startdate = document.querySelector('section[id=start-date]')
var branch = document.querySelector('section[id=branch]')
var position = document.querySelector('select[id=position')

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

  // If the applicant selects Ast to Reg. Manager, display a list of branches. Otherwise, hide them.
  position.addEventListener('change', function() {
    if (position.selectedIndex == 3){
      branch.classList.remove('hidden');
    }
    else {
      branch.classList.add('hidden');
    }
  })