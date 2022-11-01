('keypress', function () {
    console.log('vamos mudar essa font')
    var FontSize = {
        storage: 'fontSize',
        currentSize: 13,
        check: checkFontSize,
        get: getFontSize,
        set: setFontSize,
        updateView: updateViewFontSize,
        change: changingFontSize

    };

    window.changeFontSize = function (type) { FontSize.change(type); };
    FontSize.check();

    function checkFontSize() {
        this.updateView();
    }

    function getFontSize() {
        return Number(localStorage.getItem(this.storage));
    }

    function setFontSize(size) {
        localStorage.setItem(this.storage, String(size));
        this.currentSize = size;
        this.updateView();
    }

    function updateViewFontSize() {
        var body = document.body;
        var elSizing = body.querySelectorAll('.font-sizing')        
        for (let i = 0; i < elSizing.length; i++) {
            const el = elSizing[i];            
            el.style.fontSize = String(this.currentSize) + 'px';
        }
    }

    function changingFontSize(type) {
        console.log(type)
        if(type === 'plus')
            this.currentSize = this.currentSize + 1;
        else if(type === 'less')
            this.currentSize = this.currentSize - 1;
        
        this.set(this.currentSize)
    }
})();
