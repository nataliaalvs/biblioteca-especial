document.body.onload = () => {
    if (localStorage.getItem('fontSize') != undefined || localStorage.getItem('fontSize') != null ||  localStorage.getItem('fontSize') < 7){
        window.changeFontSize('none');
    } 
}

('keypress', function () {
    var minSize = 0.5;
    var maxSize = 1.5;
    var defaultSize = 1;
    var paramSizing = 0.1;
    console.log('vamos mudar essa font')
    var FontSize = {
        storage: 'fontSize',
        currentSize: null,
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
        localStorage.setItem(this.storage, String(size.toFixed(2)));
        this.currentSize = size;
        
        this.updateView();        
    }

    function updateViewFontSize() {
        
        var body = document.body;
        var elSizing = body.querySelectorAll('.font-sizing');
        elSizing = removeDuplicates(elSizing);
        for (let i = 0; i < elSizing.length; i++) {
            const el = elSizing[i];
            // Geral settings
            el.style.wordWrap = 'break-word';
            if(el.nodeName === 'H1' || el.nodeName === 'H2' || el.nodeName === 'H3' || el.nodeName === 'H4' || el.nodeName === 'H5' || el.nodeName === 'H6') {
                switch (el.nodeName) {
                    case 'H1':
                        el.style.setProperty( 'font-size', 'calc(40px + '+String(this.get() * 100) + '%)', 'important' );
                        // el.style.setProperty( 'line-height', 'calc(9.5px + '+String(this.get() * 70) + '%)', 'important' );
                        break;

                    case 'H2':
                        el.style.setProperty( 'font-size', 'calc(35px + '+String(this.get() * 100) + '%)', 'important' );
                        el.style.setProperty( 'line-height', 'calc(2px + '+String(this.get() * 70) + '%)', 'important' );
                        break;
                        /*ANTES ESTAVAM TODOS OS CALC IGUAIS AO DO H2, COM 35PX, LINE HEIGTH DE 1.2REM E O SEGUNDO FONT-SIZE COM 60PX*/

                    // case 'H2':
                    case 'H3':
                        el.style.setProperty( 'font-size', 'calc(30px + '+String(this.get() * 100) + '%)', 'important' );
                        // el.style.setProperty( 'font-size', 'calc(60px + '+String(this.get() * 100) + '%)', 'important' );
                        break;

                    // case 'H2':
                    case 'H4':
                            el.style.setProperty( 'font-size', 'calc(25px + '+String(this.get() * 100) + '%)', 'important' );
                            // el.style.setProperty( 'font-size', 'calc(60px + '+String(this.get() * 100) + '%)', 'important' );
                            break;

                    // case 'H4':
                    case 'H5':
                        el.style.setProperty( 'font-size', 'calc(20px + '+String(this.get() * 100) + '%)', 'important' );
                        // el.style.setProperty( 'font-size', 'calc(calc(1rem + 0.3vw) + '+String(this.get() * 100) + '%)', 'important' );
                        // el.style.setProperty( 'line-height', 'calc(1.2rem + '+String(this.get() * 40) + '%)', 'important' );
                        break;

                    // case 'H2':
                    case 'H6':
                        el.style.setProperty( 'font-size', 'calc(35px + '+String(this.get() * 100) + '%)', 'important' );
                        el.style.setProperty( 'font-size', 'calc(60px + '+String(this.get() * 100) + '%)', 'important' );
                        break;
                
                    default:
                        break;
                }
                
                
            } else {                
                el.style.setProperty( 'font-size', 'calc(18px + '+String(this.get() * 50) + '%)', 'important' );
                el.style.setProperty( 'line-height', 'calc(20px + '+String(this.get() * 40) + '%)', 'important' );
            }
        }        
        
    }

    function changingFontSize(type) {
        console.log(this.get())
        if (this.get() == null || this.get() < minSize){
            this.currentSize = defaultSize;
            this.set(defaultSize)
        } else {
            this.currentSize = this.get();            
        }

        if(type === 'plus'){
            if (this.get() < maxSize) 
                this.set(this.currentSize + paramSizing)
        }else if(type === 'less'){
            if (this.get() > minSize) 
                this.set(this.currentSize - paramSizing)
    
        }
        
        
        
    }
    function removeDuplicates(arr) {
        var unique = [];
        arr.forEach(element => {
            if (!unique.includes(element)) {
                unique.push(element);
            }
        });
        return unique;
    }
})();

