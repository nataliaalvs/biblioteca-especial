const toggle = document.getElementById('toggleDark');

//  toggle.addEventListener('click', function (e) {
//      this.classList.toggle('bi-moon-fill');

//      if (this.classList.toggle('bi-brightness-high-fill')) {
//      } else {
//          button.addEventListener('click', function (e) {
//          });
//      }
//  });


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

// creating square
var colors = ['#fc45cd', '#cc002a', '#ff099a', '#ff00e4', '#ff0808', '#b300ff', '#6f00ff', '#009fff', '#00ffe2', '#00fba0', '#00ff73', '#00ff3b', '#2ccb13', '#aff70d', '#f808ff', '#ff6a00', '#a600ff','#0000ff', '#00d4ff', '#23ff00', '#008aff', '#ff00c6', '#67ff73', '#f1ff0c', '#ff67dd', '#ff000'];
var boxes = document.querySelectorAll(".card-color");

for (i = 0; i < boxes.length; i++) {
  // Pick a random color from the array 'colors'.
  boxes[i].style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
//   boxes[i].style.width = '100px';
//   boxes[i].style.height = '100px';
  boxes[i].style.display = 'inline-block';
}

var color = localStorage.getItem("color");
