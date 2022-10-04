 const toggle = document.getElementById('toggleDark');

 toggle.addEventListener('click', function (e) {
     this.classList.toggle('bi-moon-fill');

     if (this.classList.toggle('bi-brightness-high-fill')) {
     } else {
         button.addEventListener('click', function (e) {
         });
     }
 });



('keypress', function () {
    var Contrast = {
        storage: 'contrastState',
        cssClass: 'contrast',
        currentState: null,
        check: checkContrast,
        getState: getContrastState,
        setState: setContrastState,
        toogle: toogleContrast,
        updateView: updateViewContrast
    };

     window.toggleContrast = function () { Contrast.toogle(); };

     Contrast.check();

     function checkContrast() {
         this.updateView();
     }

    function getContrastState() {
         return localStorage.getItem(this.storage) === 'true';
    }

    function setContrastState(state) {
        localStorage.setItem(this.storage, '' + state);
        this.currentState = state;
         this.updateView();
    }

    function updateViewContrast() {
        var body = document.body;

         if (this.currentState === null)
             this.currentState = this.getState();

         if (this.currentState)
             body.classList.add(this.cssClass);
         else
             body.classList.remove(this.cssClass);
    }

     function toogleContrast() {
         this.setState(!this.currentState);
     }
})();
