('keypress', function () {
    var Dyslexia = {
        storage: 'dyslexiaState',
        cssClass: 'dyslexia',
        currentState: null,
        check: checkDyslexia,
        getState: getDyslexiaState,
        setState: setDyslexiaState,
        toogle: toogleDyslexia,
        updateView: updateViewDyslexia
    };

    window.toggleDyslexia = function () { Dyslexia.toogle(); };

    Dyslexia.check();

    function checkDyslexia() {
        this.updateView();
    }

    function getDyslexiaState() {
        return localStorage.getItem(this.storage) === 'true';
    }

    function setDyslexiaState(state) {
        localStorage.setItem(this.storage, '' + state);
        this.currentState = state;
        this.updateView();
    }

    function updateViewDyslexia() {
        var body = document.body;

        if (this.currentState === null)
            this.currentState = this.getState();

        if (this.currentState)
            body.classList.add(this.cssClass);
        else
            body.classList.remove(this.cssClass);
    }

    function toogleDyslexia() {
        this.setState(!this.currentState);
    }
})();
